#!/usr/bin/env python
# coding: UTF-8

import urllib2
import re

whatismyip_url = "http://automation.whatismyip.com/n09230945.asp"
dyndns_url = "http://checkip.dyndns.org/"

def whatismyip_get_ip():
	"""
	Retorna o IP externo atual, usando whatismyip
	"""
	ip = urllib2.urlopen(whatismyip_url).read()#.readlines()[0]
	return ip
	
def dyndns_get_ip():
	"""
	Retorna o IP externo atual
	"""
	text = urllib2.urlopen(dyndns_url).read()#.readlines()[0]
	
	#ip = re.findall( r'[0-9]+(?:\.[0-9]+){3}', text )
	ip = re.search( r'[0-9]+(?:\.[0-9]+){3}', text ).group()
	
	return ip
	
def get_ip():
	return dyndns_get_ip()

