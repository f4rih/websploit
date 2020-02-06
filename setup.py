#!/usr/bin/python3
import codecs
from setuptools import setup, find_packages

WEBSPLOIT_VERSION = "4.0.4"
WEBSPLOIT_DOWNLOAD = ('https://github.com/websploit/websploit/tarball/' + WEBSPLOIT_VERSION)


def read_file(filename):
	"""
	Read a utf8 encoded text file and return its contents.
	"""
	with codecs.open(filename, 'r', 'utf8') as f:
		return f.read()

def read_requirements():
    with open('requirements.txt') as f: 
        return f.readlines() 


setup(
	name='websploit',
	packages=[
		'websploit',
		'websploit.ezcolor',
		'websploit.modules',
		'websploit.core',
		'websploit.core.base',
		'websploit.core.utils'],
	package_data={
          'websploit.core': [
              'utils/*',
          ],
      },

	version=WEBSPLOIT_VERSION,
	description='Websploit is a high level MITM framework',
	long_description=read_file('README.md'),
	long_description_content_type='text/markdown',
    # packages = find_packages(),
    entry_points ={ 
            'console_scripts': [ 
                'websploit = websploit.websploit:start_wsf'
            ] 
        },

	license='MIT',
	author='Fardin Allahverdinazhand',
	author_email='0x0ptim0us@gmail.com',
	url='https://github.com/websploit/websploit',
	download_url=WEBSPLOIT_DOWNLOAD,
	keywords=['python3', 'websploit', 'wsf', 'MITM', 'wifi', 'arp spoof'],
	classifiers=[
		'Intended Audience :: Developers',
		'License :: OSI Approved :: MIT License',
		'Programming Language :: Python :: 3.5',
		'Programming Language :: Python :: 3.6',
		'Programming Language :: Python :: 3.7',
		'Programming Language :: Python :: 3.8',
		'Natural Language :: English',
	],

	install_requires= read_requirements(),

)
