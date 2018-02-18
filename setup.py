from distutils.core import setup
setup(
  name = 'dexter',
  packages = ['dexter'], # this must be the same as the name above
  version = '0.1',
  description = 'A library to fetch images from a directory and fetch OCR from it with orientation rotation and pdf support',
  author = 'Sunim Acharya',
  author_email = 'sunim.54@gmail.com',
  url = 'https://github.com/aryaminus/dexter', # use the URL to the github repo
  download_url = 'https://github.com/aryaminus/dexter/archive/0.1.tar.gz', # I'll explain this in a second
  keywords = ['ocr', 'image', 'pdf'], # arbitrary keywords
  classifiers = [],
        install_requires=[
          'io','os','subprocess','sys','time','PIL','pyocr','wand'
      ],
)