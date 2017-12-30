#!/usr/bin/env python
# coding: UTF-8


'''
	no_ip_updater.getip
	===================

	Implements several APIs that let you see the public IP of your computer.

'''

__author__ = "Kelvin Steiner"
__email__ = "kelvinsteinersantos@gmail.com"


import urllib.request
import re
import base64


IP_REGEX = r'[0-9]+(?:\.[0-9]+){3}'


whatismyip_url = "http://automation.whatismyip.com/n09230945.asp"
dyndns_url = "http://checkip.dyndns.org/"
icanhazip_url = "http://icanhazip.com/"


def whatismyip_get_ip():
	"""
	Uses whatismyip API.
	( NO LONGER WORKS )
	"""
	ip =  urllib.request.urlopen( whatismyip_url ).read().decode('utf-8')#.readlines()[0]
	return ip

def dyndns_get_ip():
	"""
	Uses dyndns API.
	"""
	text =  urllib.request.urlopen( dyndns_url ).read().decode('utf-8')#.readlines()[0]

	ip = re.search( IP_REGEX , text ).group()

	return ip

def icanhazip_get_ip():
	"""
	Uses icanhazip API.
	"""
	text =  urllib.request.urlopen( icanhazip_url ).read().decode('utf-8')#.readlines()[0]

	ip = re.search( IP_REGEX , text ).group()
	return ip


def get_ip():
	'''
	Returns the current public IP.
	'''
	return dyndns_get_ip()
