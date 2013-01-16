from distutils.core import setup

#datafiles = [ ('/usr/bin/', ['update-no-ip']) ]
datafiles=[ ('.', ['update-no-ip']) ]

setup(name='no-ip-updater',
	  version='1.0',
	  description='Python Module to Update No-IP',
	  author='Kelvin Steiner',
	  author_email='kelvinsteinersantos@gmail.com',
	  packages=["no_ip_updater"],
	  data_files = datafiles
	  )