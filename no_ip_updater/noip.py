#!/usr/bin/env python
# coding: UTF-8

import sys
import base64
import urllib.request, urllib.error, urllib.parse

import logging

urlbase = "http://dynupdate.no-ip.com/nic/update?hostname={2}&myip={3}"
urlbase_https = "https://dynupdate.no-ip.com/nic/update?hostname={2}&myip={3}"

def update(username, password, host, ip, https=True):
	"""
	Update one host
	"""

	# Format the URL
	if https:
		url = urlbase_https.format(username, password, host, ip)
	else:
		url = urlbase.format(username, password, host, ip)

	# HTTP Request
	userData = "Basic " + base64.b64encode((username + ":" + password).encode('utf8')).decode('utf8').rstrip()

	req = urllib.request.Request(url)
	req.add_header("Authorization", userData)

	try:
		res = urllib.request.urlopen(req)
	except urllib.error.HTTPError as err:
		# logging.error(err)
		raise err

	# Returns the server response
	return res.read()


# Messages displayed according to the No-IP server response
messages = {
	"good":    "[SUCCESS] Host updated sucsessfully.",
	"nochg":   "[SUCCESS] No update needed to host.",
	"nohost":  "[ERROR] Host doesn't exist.",
	"badauth": "[ERROR] Username or password is invalid.",
	"badagent":"[ERROR] Client disabled. Client should exit and not perform any more updates without user intervention.", 
	"!donator":"[ERROR] An update request was sent including a feature that is not available to that particular user such as offline options.",
	"abuse":   "[ERROR] Username is blocked due to abuse.",
	"911":     "[ERROR] A fatal error on our side such as a database outage. Retry the update no sooner than 30 minutes"
}

def get_response(response):
	"""
	Return a message according to the No-IP response
	"""
	for key in messages.keys():
		message = messages[key]
		if response.find(key.encode('utf-8')) == 0:
			return message


def updateHosts(username, password, ip, hosts, https=True):
	"""
	Updates one or more hosts, printing corresponding messages.
	"""

	# If multiple hosts
	if type(hosts) in (list, tuple):
		for host in hosts:
			print("\nhost: {}".format(host))
			resp = update(username, password, host, ip, https )
			print(get_response(resp))

	# If one host
	elif type(hosts) == str:
		print("host: {}".format(hosts))
		resp = update(username, password, hosts, ip, https )
		print(get_response(resp))
