try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Toy Robot',
    'author': 'Lauchlin Wilkinson',
    'url': 'https://github.com/lokulin/toy-robot-python',
    'download_url': 'https://github.com/lokulin/toy-robot-python',
    'author_email': 'lauchlin@lauchlin.com',
    'version': '0.1',
    'install_requires': [],
    'packages': ['toyrobot'],
    'scripts': [],
    'name': 'toyrobot'
}

setup(**config)
