import json
import pprint
import csv



with open ('data_followers_2.json') as infile:
	file = infile.read()
	james = json.loads(file)

#pprint.pprint (james)
for obj in james:
	pprint.pprint (obj)
'''
created_at
description
followers_count
friends_count
location
name
screen_name
statuses_count
'''



count = 0
twitter_followers = []
for obj in james:
	count += 1
	print (count)
	tmp = {}
	tmp['name'] = (obj['name'])
	tmp['created_at'] = (obj['created_at'])
	tmp['location'] = (obj['location'])
	tmp['username'] = (obj['screen_name'])
	tmp['followers_count'] = (obj['followers_count'])
	tmp['friends_count'] = (obj['friends_count'])
	tmp['description'] = (obj['description'])
	tmp['statuses_count'] = (obj['statuses_count'])
	tmp['url'] = (obj['url'])
	print (tmp)
	twitter_followers.append(tmp)


#pprint.pprint (twitter_followers)



f = csv.writer(open("PL_twitter_Followers.csv", "w"))

f.writerow(['name','created_at','location','username','followers_count','friends_count','description','statuses_count','url'])

for obj in twitter_followers:
	f.writerow([obj['name'],obj['created_at'],obj['location'],obj['username'],obj['followers_count'],obj['friends_count'],obj['description'],obj['statuses_count'],obj['url']])

