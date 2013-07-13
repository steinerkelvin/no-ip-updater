#!/usr/bin/env python
# coding: UTF-8

import sys
import base64
import urllib2

import logging

# URL a ser formatada
urlbase = "http://dynupdate.no-ip.com/nic/update?hostname={2}&myip={3}"
urlbase_https = "https://dynupdate.no-ip.com/nic/update?hostname={2}&myip={3}"



def update(username, password, host, ip, https=True):
	"""
	Atualiza um host
	"""
	
	# Formata a URL
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
	
	# Retorna a respota
	return res.read()


# Mensagems exibidas para as respostas do No-IP
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
	Retorna uma mensagem de acordo com a resposta obtida do No-IP
	"""
	for m in range(len(messages.keys())):
		key = messages.keys()[m]
		message = messages[key]
		if response.find(key) == 0:
			return message


def updateHosts(username, password, ip, hosts, https=True):
	"""
	Atualiza um ou mais hosts, printando as mensagens de resposta
	"""
	# Se hosts for lista ou tupla
	if type(hosts) in (list, tuple):
		# Printa o IP
		print "ip: {}".format(ip)
		# Para cada host
		for host in hosts:
			# Printa o nome do host
			print "\nhost: {}".format(host)
			# Atualiza e printa a informação correspondente a resposta recebida
			resp = update(username, password, host, ip, https )
			print get_response(resp)
	
	# Se hosts for string
	elif type(hosts) == str:
		# Printa o IP
		print "ip: {}".format(ip)
		# Printa o nome do host
		print "host: {}".format(hosts)
		# Atualiza e printa a informação correspondente a resposta recebida
		resp = update(username, password, hosts, ip, https )
		print get_response(resp)



