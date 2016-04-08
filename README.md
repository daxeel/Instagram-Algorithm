# Instagram-Algorithm
A simple algorithm designed to get the relevant users to particular given user profile.

# Status
Version 1 developed. Working on making it more accurate.
Under development

# Algorithm
<img id="flowchart" src="https://raw.githubusercontent.com/daxeel/Instagram-Algorithm/master/Algoritm_Flowchart(V1).png">

# Test on your machine
To run this, you need Instagram consumer key. Follwo these steps.<br>
1. Go to https://www.instagram.com/developer.<br>
2. Login with your Instagram account.<br>
3. Go to "Manage Clients"<br>
4. Click on "Register a new client"<br>
5. Fill out the details and get the Consumer Key.<br>
Open terminal and follow this commands.
```sh
git clone https://github.com/daxeel/Instagram-Algorithm.git
cd Instagram-Algorithm
```
Open insta-cli.py in your text editor. Replace XXXX-XXXX-XXXX-XXXX with your cosumer key.
Now start script by entering this command in terminal.
```py
python insta-cli.py [INSTAGRAM_USERNAME]
```
For example,
```py
python insta-cli.py daxeel_soni
```
### Output
Output will be list of os usernames which are similar to given instagram username.
```sh

60 interests found! 

Scanning interest no - 1
----------
Scanning interest no - 2
----------
Scanning interest no - 3
----------
Scanning interest no - 4
----------
Scanning interest no - 5
----------
Scanning interest no - 6
----------
Scanning interest no - 7
----------
Scanning interest no - 8
----------
Scanning interest no - 9
----------
Scanning interest no - 10
----------

21 users found
---------------
[u'garvigujarati', u'malhar028', u'shagunchauhan', u'codergirl_', u'nellysugu', u'mindsetofgreatness', u'motivation.entrepreneur', u'modaecustomizacao', u'lovetutorialsx', u'spoonuniversity', u'houseofhighlights', u'sbwheels_goryaev', u'egeozmat', u'deepika__perfection', u'niralivakil98', u'starvingtime', u'savage.vids', u'flamingeos', u'natgeoyourshot', u'motivation', u'dressmybff']
```

# Programming Concepts Used
1. Web Scraping
2. Text Analysis
3. Data Mining
4. API Interaction
5. Error Handling
