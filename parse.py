"""

Author: Ajay Lakshminarayanarao

Write a program in Python to parse the attached file tweets.txt and complete the following tasks:
1) Count how many tweet objects are present.
2) Identify the date on which these tweets were collected.
3) Choose the 10 most interesting fields available in this data.  (You choose according to your own judgment.)  Convert the attached file to a .csv file that contains ONLY those 10 columns.
4) Using the information available in the file, write a function to identify which tweets are probably not in the English language.

Requirements: Install unicodecsv to write utf-8 characters to csv file. ( pip install unicodecsv )

"""

from sys import argv
from sys import exit
import json
import unicodecsv as csv

def openfile():
    try:
	tweets_file = open(argv[1])
	return tweets_file
    except:
	print "Error opening file. Usage: python parse.py <filename>"
	raise



def readfile(f):
    lines=[]
    try:
	for line in f:
		json_line = json.loads(line)
		lines.append(json_line)
    except:
	print "Error in readfile()"
	raise
    return lines



def getTweetDate(lines):
    map_date={}
    for line in lines:
	print "Tweet ID ", line["id"]," collected at ", line["created_at"]



def generateCSV10fields(lines):
	f = open('tweets.csv','w')
	writer = csv.writer(f, delimiter='\t')
	rows=[]
	interestingFields=[['id'],['text'],['lang'],['favorite_count'],['retweet_count'],['user','name'],\
			  ['user','location'],['source'],['user','statuses_count'],['user','followers_count'],\
			  ['user','friends_count'],['created_at']];

	header=[]
	for field in interestingFields:
		header.append(''.join(field))
	rows.append(header)

	for line in lines:
		row=[]
		temp = line
		for field in interestingFields:
			for level in field:
				temp = temp[level]
			row.append(temp)
			temp=line
		rows.append(row)
	writer.writerows(rows)



def getNotEnglishTweets(lines):
	notEnglishTweets=[]
	for line in lines:
		if line['lang']!='en':
			notEnglishTweets.append(line)
	return notEnglishTweets



def main():
    try:
        tweets_file = openfile()
	lines = readfile(tweets_file)
	if len(lines) == 0:
		print "There are 0 tweets in input file"
		return 0
	tweet_count = len(lines)
	print "There are ",tweet_count," tweets in input file"
	map_date = getTweetDate(lines)
	generateCSV10fields(lines)
	"""generated file called tweets.txt"""
	notEnglishTweets = []
	""" notEnglistTweets is a list of tweet objects which are not in English language"""
	notEnglishTweets = getNotEnglishTweets(lines)
	return 0
    except Exception, err:
	print Exception, err
	return -1



if __name__ == "__main__":
    exit(main())
