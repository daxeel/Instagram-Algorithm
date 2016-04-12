#! /usr/bin/env python

############################## Credits #############################
# PROJECT      : Instagram Algorithm
# DESCRIPTION  : A simple algorithm designed to get the relevant instagram users from particular given user profile.
# AUTHOR       : Daxeel Soni
#
# Copyright (c) 2016, Daxeel Soni
# All rights reserved.

###################### IMPORT REQUIRED MODULES ######################
from bs4 import BeautifulSoup
import urllib2
import json
import sys
import time

######################## GET USER INTERESTS #########################
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

################### START GETTING SUGGESTED USERS ####################
def get_users():
	hashtags = get_hashtags()
	USERS = []
	FINAL_DATA = []
	NO_TAGS = 0
	if len(hashtags) >= 10:NO_TAGS = 10
	else:NO_TAGS = len(hashtags)
	for each in range(NO_TAGS):
		each = hashtags[each]
		tag = each[0]
		url = "https://www.instagram.com/explore/tags/%s" % tag
		request = urllib2.urlopen(url)
		soup = BeautifulSoup(request, "html.parser")
		data = json.loads(soup.find_all('script')[6].string[21:-1])
		posts = data['entry_data']['TagPage'][0]['tag']['top_posts']['nodes']
		for post_no in range(each[1]):
			TEMP = {}
			try:
				user_id = posts[post_no]['owner']['id']
				token = "INSTAGRAM ACCESS TOKEN"
				api_req = "https://api.instagram.com/v1/users/" + user_id + "?access_token=" + token
				api_call = urllib2.urlopen(api_req)
				api_data = json.loads(api_call.read())
				username = api_data['data']['username']
				profile_picture = api_data['data']['profile_picture']
				if username not in USERS:
					TEMP['username'] = username
					TEMP['profile_picture'] = profile_picture
					USERS.append(username)
			except:
				pass
			FINAL_DATA.append(TEMP)
	return json.dumps(FINAL_DATA)

################## INITIAL FUNCTION FOR BASIC SETUP ###################
def setup(username):
	global data
	url = "https://www.instagram.com/%s/" % username
	request = urllib2.urlopen(url)
	soup = BeautifulSoup(request, "html.parser")
	data = json.loads(soup.find_all('script')[6].string[21:-1])
	return get_users()

####################### SCRIPT STARTS FROM HERE ########################
data = setup('daxeel_soni')
print data
