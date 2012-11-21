#!/usr/bin/env python
# coding: UTF-8

import urllib2

whatismyip_url = "http://automation.whatismyip.com/n09230945.asp"

def get_ip():
	"""
	Retorna o IP externo atual
	"""
	ip = urllib2.urlopen(whatismyip_url).read()#.readlines()[0]
	return ip



