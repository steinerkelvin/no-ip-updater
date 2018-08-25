from distutils.core import setup

import os

setup(
	name='no-ip-updater',
	version='1.1',
	description='Python Module to Update No-IP',
	author='Kelvin Santos',
	author_email='kelvinsteinersantos@gmail.com',
	packages=["no_ip_updater"],
	scripts = ["update-no-ip", "auto-update-no-ip"]
)
