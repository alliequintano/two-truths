from setuptools import setup

setup(
    name = 'src',
    version = '0.1.0',
    packages = ['src'],
    entry_points = {
        'console_scripts': [
            'two-truths = src.__main__:main'
        ]
    })