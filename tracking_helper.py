# Function: helper for tracking-flow

import sys

class Email:
	
	def __init__(self,from_address,to_address,text):
		self.from_address = from_address
		self.to_address = to_address
		self.text = text
	
	

# check each word in email for isPhraseTrackingPhre
def parseEmailforTrackingFlow(email):
	
	for word in str.split(email.text):
		if isTrackingPhrase(word):
			setupTrackingFlow(email,word)


def isTrackingPhrase(phrase):
	print "word: {}".format(phrase)
	
	# TODO: replace with regex
	if phrase.startswith('1Z'):
		return True
	else:
		return False
	
	
def setupTrackingFlow(email,word):
	
	print "setting shit up ..."
	print "from: {0}; to: {1}; tracking_id:{2}".format(email.to_address,email.from_address, word)
	
