from PIL import Image
import pytesseract
from translate import Translator
from PIL import ImageFont, ImageDraw, Image

# The next line may not be needed. It is needed if tesseract is not in your PATH
# (Check path for tesseract and modify the line below if needed)
pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'

# This function handles the core OCR processing of the input image.


def ocr_core(filename, language):
    choice = 0
    if language == '1':
        choice = 'chi_sim'
    elif language == '2':
        choice = 'deu'
    elif language == '3':
        choice = 'hun'

    text = pytesseract.image_to_string(Image.open(filename), lang=choice)
    return text

# Writes text extracted from image into a txt file named "script.txt"
# which is saved in the same path as the input image file


def writefile(image_path, strstr):
	wordlist = strstr.split()
	with open(image_path + '/script.txt', 'a') as f:
		f.writelines("\r".join(wordlist))

# Takes lines of text extracted from txt file and translates them,
# outputs translated version into a txt file called "translated.txt"
# and an image file with the translated text called Capture.JPG.


def translate_text(image_path, imagename, language):
    # sets target language and input language for translator
    choice = 0
    if language == '1':
        choice = "zh"
    elif language == '2':
        choice = 'de'
    elif language == '3':
        choice = 'hu'
    translator = Translator(to_lang="en", from_lang=choice)

    # opens the OCR output file and reads each line into contents
    with open(image_path + '/script.txt', encoding='utf-8') as f:
        contents = f.readlines()

    # sets the dimensions and background color for the new image object
    oldimg = Image.open(image_path + "/" + imagename)
    # Grab the size of the input image
    # Later we can choose a font size depending on input image size
    width, height = oldimg.size
    width *= 2
    height *= 2

    # Grab a color sample, to reproduce the background in the output image
    # The code obtains an rgb tuple at position (x,y)
    # grabs pixel from upper left corner
    background = oldimg.getpixel((5, 5))

    newimg = Image.new(mode="RGB", size=(width, height), color=background)

    # Generates a txt file and JPG image file from the translated txt file
    with open(image_path + '/translated.txt', 'a') as n:
        for line in contents:   # iterates thru each line of text in "contents"
            # translate each line and write to file
            n.writelines(translator.translate(line) + "\n")
            draw = ImageDraw.Draw(newimg)
            # font size 15 should be scaled for image size
            font = ImageFont.truetype("arial.ttf", 12)
            # In the next line, first 2 numbers are pixels to right and down of upper corner
            draw.text((0, 28), translator.translate(
                line), fill=(0, 0, 0), font=font)
        newimg.save("Capture.JPG")
        newimg.show()  # I don't think this works

# Change the translator provider
# Default is mymemory but it limits the number of translations per day.
# Template code to change provider:
# secret = '<your secret from Microsoft or DeepL>'
# translator = Translator(provider='<the name of the provider, eg. microsoft or deepl>', to_lang=to_lang, secret_access_key=secret)


# Obtain input path and file name from the user
path = input('file path: ')
userfile = input('file name: ')

print("You have 3 choices for input language. Eneter 1 for Chinese, 2 for German, or 3 for Hungarian.")
inlanguage = input('Your choice: ')
print('\n')

print("******Starting******")

# Perform OCR on the input image file and let user know when finished this step
text = ocr_core(path + "/" + userfile, inlanguage)
writefile(path, text)
print("OCR of image " + userfile + " is done.")

# Perform the translation step
print("Now performing the translation.")
translate_text(path, userfile, inlanguage)

print("~~~~~~Finished~~~~~~")
