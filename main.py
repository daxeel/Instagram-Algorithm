from bs4 import BeautifulSoup
import urllib2
import json

username = 'daxeel_soni'
url = "https://www.instagram.com/%s/" % username
request = urllib2.urlopen(url)
soup = BeautifulSoup(request, "html.parser")

data = json.loads(soup.find_all('script')[6].string[21:-1])

# user_bio_keywords = data['entry_data']['ProfilePage'][0]['user']['biography'].split()
# for each in user_bio_keywords:
# 	try:str(each)
# 	except UnicodeEncodeError:user_bio_keywords.remove(each)

def get_hashtags():
	HASHTAGS = {}
	NO_OF_POSTS = 0

	posts = data['entry_data']['ProfilePage'][0]['user']['media']['nodes']

	if len(posts) >= 10:NO_OF_POSTS = 10
	else:NO_OF_POSTS = len(posts)

	for p_number in range(NO_OF_POSTS):
		try:post_caption_list = posts[p_number]['caption'].split()
		except KeyError:pass
		for each in post_caption_list:
			if each[0] == '#':
				if each[1::] in HASHTAGS:HASHTAGS[each[1::]] = HASHTAGS[each[1::]] + 1
				else:HASHTAGS[each[1::]] = 1

	HASHTAGS_SORTED = sorted(HASHTAGS.items(), key=lambda x: x[1], reverse=True)

	for each in HASHTAGS_SORTED:
		try:str(each[0])
		except UnicodeEncodeError:HASHTAGS_SORTED.remove(each)
	
	return HASHTAGS_SORTED


def get_users():
	hashtags = get_hashtags()

	print str(len(hashtags)) + " interests found! \n\n"

	USERS = []
	NO_TAGS = 0

	if len(hashtags) >= 10:NO_TAGS = 10
	else:NO_TAGS = len(hashtags)

	for each in range(NO_TAGS):

		print "Scanning intrest no - " + str(each+1) 
		print '-'*10

		each = hashtags[each]

		tag = each[0]
		url = "https://www.instagram.com/explore/tags/%s" % tag
		request = urllib2.urlopen(url)
		soup = BeautifulSoup(request, "html.parser")

		data = json.loads(soup.find_all('script')[6].string[21:-1])
		posts = data['entry_data']['TagPage'][0]['tag']['top_posts']['nodes']

		for post_no in range(each[1]):
			try:
				user_id = posts[post_no]['owner']['id']
				token = "XXX-XXX-XXX-XXX"
				api_req = "https://api.instagram.com/v1/users/" + user_id + "?access_token=" + token
				api_call = urllib2.urlopen(api_req)
				api_data = json.loads(api_call.read())
				username = api_data['data']['username']
				if username not in USERS:
					USERS.append(username)
			except:
				print "One intrest skipped."

	print str(len(USERS)) + " users found"
	print USERS

get_users()

