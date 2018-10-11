import requests
import sys


def sendcred(url, key, uid):
	values = {'pass' : key,'id'	: uid}
	r = requests.post(url, values)
	page = r.text
	if(page != '1337'):
		sys.exit('remote server error')
