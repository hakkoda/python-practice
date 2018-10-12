try: 
    from setuptools import setup
except ImortError:
    from distutils.core import setup

config = {
    "description": "My Project",
    "author": "Jason Tennant",
    "url": "url to get it at",
    "download_url": "Where to download it",
    "author_email": "jason.tennant@outlook.com",
    "version": "0.1",
    "install_requires": ["nose"],
    "packages": ["LinkedList"],
    "scripts": [],
    "name": "LinkedList"
}

setup(**config)
