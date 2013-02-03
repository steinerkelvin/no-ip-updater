from distutils.core import setup

import os

if os.name == "posix":
	datafiles = [ ('/usr/bin/', ['update-no-ip']) ]
else:
	datafiles=[ ('.', ['update-no-ip']) ]

setup(name='no-ip-updater',
	  version='1.0',
	  description='Python Module to Update No-IP',
	  author='Kelvin Steiner',
	  author_email='kelvinsteinersantos@gmail.com',
	  packages=["no_ip_updater"],
	  data_files = datafiles
	  )