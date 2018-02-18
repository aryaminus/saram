#from distutils.core import setup
from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(
  name = 'saram',
  packages = ['saram'], # this must be the same as the name above
  version = '0.2',
  description = 'A library to fetch images from a directory and fetch OCR from it with orientation rotation and pdf support',
  long_description = readme(),
  author = 'Sunim Acharya',
  author_email = 'sunim.54@gmail.com',
  url = 'https://github.com/aryaminus/saram', # use the URL to the github repo
  keywords = ['ocr', 'image', 'pdf'], # arbitrary keywords
  classifiers = [],
  install_requires=[
        'setuptools', 'Pillow', 'pyocr', 'Wand'
  ],
  include_package_data=True,
  zip_safe=False
)