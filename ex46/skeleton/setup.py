try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
    
config = {
    'description': 'My Project',
    'author': 'Aung Kyaw Khaing',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'mitu16888@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['proj'],
    'scripts': [],
    'name': 'proj'
    }
setup(**config)
