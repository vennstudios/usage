try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'usage',
	'author': 'Erik E. Jansson',
	'url': 'URL',
	'download_url': 'Download_URL',
	'author_email':'erikejan@hotmail.com',
	'version':'0.1',
	'install_requires':['nose'],
	'packages':['usage'],
	'scripts':[]
	'name':'usage'
}

setup(**config)