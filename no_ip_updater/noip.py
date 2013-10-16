#!/usr/bin/env python
# coding: UTF-8

import sys
import base64
import urllib2

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
	
	userData = "Basic " + (username + ":" + password).encode("base64").rstrip()
	
	req = urllib2.Request(url)
	req.add_header("Authorization", userData)
	
	try:
		res = urllib2.urlopen(req)
	except urllib2.HTTPError:
		logging.error( " authentication error" )
		exit(2)
	
	# Returns the server response
	return res.read()


# Messages displayed according to the No-IP server response
messages = {
		"good":    "[SUCESS] Host atualizado com sucesso.",
		"nochg":   "[SUCESS] O Host já está atualizado.",
		"nohost":  "[ERROR] O Host fornecido não existe.",
		"badauth": "[ERROR] Combinação de usuário e senha inválida.",
		"badagent":"[ERROR] \"Cliente desativado\"", # Não sei o significado :(
		"!donator":"[ERROR] A solicitação de update foi enviada com"+
			" um recurso que está indisponível para o usuário especificado.",
		"abuse":   "[ERROR] O usuário está bloqueado.",
		"911":     "[ERROR] Um erro fatal aconteceu."
		}

def get_response(response):
	"""
	Return a message according to the No-IP response
	"""
	for m in range(len(messages.keys())):
		key = messages.keys()[m]
		message = messages[key]
		if response.find(key) == 0:
			return message


def updateHosts(username, password, ip, hosts, https=True):
	"""
	Updates one or more hosts, printing corresponding messages.
	"""
	
	print "ip: {}".format(ip)
	
	# If multiple hosts
	if type(hosts) in (list, tuple):
		for host in hosts:
			print "\nhost: {}".format(host)
			resp = update(username, password, host, ip, https )
			print get_response(resp)
	
	# If one host
	elif type(hosts) == str:
		print "host: {}".format(hosts)
		resp = update(username, password, hosts, ip, https )
		print get_response(resp)



