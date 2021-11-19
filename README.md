# Project 4 - PITT 
This is group 1's implementation of Project 4 for EECS 448. 

## Description
PITT stands for Project 4 Image Text Translator. The program is an image-to-text OCR reader and translation app. The input is an image file (various file formats, such as .jpg, .png, etc.) and the output is a JPG image file. The program works by taking in an image that has some text in it in various languages, reading the text with an OCR engine, and outputting the text to a .txt file. It then translates the text in the .txt file to English. The final outputs are a .txt file with translated text, and an image file that looks like the input file, except the original non-English text on the image is replaced with the translated version. The size and background color of the input and outpuf files match. The user has a choice of 3 fonts and 4 font colors for the output image file.

To use, an image file with text, and .ttf font files will be needed. Sample image files are provided in this repository (Chinese5.jpg with five lines of text, Chinese1.png with one line of text, huntext.png with one line of Hungarian text, and fyes.png which is for the test suite that tests the software function). We also provide three font files: Arial, Times New Roman, and Comic Sans.

## Getting Started

### Dependencies
* Python 3.6+
* Pillow or PIL
* tesseract-ocr
* pytesseract
* translate
* desired language data files from choice of over 130 languages (only English is included by default)

### Installing and running the software
 * The simplest way to use the software is to run the code in the Jupyter Notebook (the .ipynb file) in this repository (hosted by Google Colaboratory, or on your own system if you have dependencies for running .ipynb files). Click the "Play" button in each code block, sequentially. The advantage of using the .ipynb file in Colaboratory is that you do not have to install software or language packs on your own system. Otherwise, follow the instructions in the Jupyter Notebook to install the needed libraries and language packs in your own system, and run the imgtl.py file with the Python 3 interpreter. Instructions in the Jupyter Notebook are for Debian/Ubuntu Linux. Follow the links in the Jupyter Notebook to install in other systems.
 * For detailed documentation of the Python code, download the repository from GitHub, and open the HTML files inside Documentation/\_build/html using a web browser. Click on the index.html file or the imgtl.html file to see a descriptions of all the functions in the Python code file (imgtl.py).
 
## Authors
* Alexander Archer
* George Blue
* Alice Chen
* Edina Harsay
* Mac Hayes

## Version History
* 0.2 
 Beta Release

# Acknowledgements/Works Cited
* PIL (Pillow) tutorial: https://pillow.readthedocs.io/en/stable/handbook/tutorial.html
* tesseract OCR engine: https://tesseract-ocr.github.io/tessdoc/Home.html
* pytesseract, a Python wrapper for tesseract: https://pypi.org/project/pytesseract/
* translate: https://pypi.org/project/translate/
* Sphinx documentation generator: https://www.sphinx-doc.org/en/master/index.html
