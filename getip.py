#!/usr/bin/env python
# coding: UTF-8

import urllib2

def get_ip():
	ip = urllib2.urlopen("http://automation.whatismyip.com/n09230945.asp").read()#.readlines()[0]
	return ip



