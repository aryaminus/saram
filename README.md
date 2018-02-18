# Saram - Image/PDF OCR conversion
Get OCR in txt form from an image or pdf extension supporting multiple files from directory using `pytesseract` with support for rotation in case of wrong orientation along.

**Currently in alpha state**

[![Saram features](https://i.imgur.com/M9dAwPq.gif)](https://i.imgur.com/M9dAwPq.gif)

**Note:**
Make sure you have a OCR tool like `tesseract` and certain data value for comparing OCR, eg `tesseract-data-eng` along with `Pillow` and `Wand` for image conversion and loading which will be fetched during pip install

## Installation

Install using PIP:
```
$ sudo pip install pahelee
$ saram <dirname>
```
***else***

Clone the source locally:
```
$ git clone https://github.com/aryaminus/saram
$ cd saram
$ git checkout py-module
$ python main.py <dirname>
```

## Todo
- [x] Add support for PDF by PDF -> image -> txt with converted image deletion after processing
- [x] Double check for orientation in case of image and PDF
- [x] Make a PIP package
- [ ] Add NLP to process the most repeated frequent characters to filer content
- [ ] Add Cloud Vision support for effective character recognization

## Reference
1. <a href="https://github.com/lucab85/PDFtoTXT" target="_blank">PDFtoTXT</a>
2. <a href="https://github.com/prabhakar267/ocr-convert-image-to-text" target="_blank">ocr-convert-image-to-text</a>
3. <a href="https://pastebin.com/QFMpp28T" target="_blank">Fix-image-rotation</a>
4. <a href="https://python-packaging.readthedocs.io/en/latest/minimal.html" target="_blank">python-packaging </a>


-----------------------------------------------------------------------------------------------------------

## Contributing

1. Fork it (<https://github.com/aryaminus/saram/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

**Enjoy!**