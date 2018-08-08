try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup
	
config = [
	'description': 'My Project',
	'author': 'Margaret Baramuli',
	'url': 'URL to get it at',
	'download_url': 'where to download it',
	'author_email': 'mbaramul@iu.edu',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['NAME'],
	'scripts': [],
	'name': 'projectname'
]

setup(**config)