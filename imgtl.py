from PIL import Image
import pytesseract
from translate import Translator
from PIL import ImageFont, ImageDraw, Image

# The next line may not be needed. It is needed if tesseract is not in your PATH
# (Check path for tesseract and modify the line below if needed)
pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'


def ocr_core(filename):
    """
    This function will handle the core OCR processing of images.
    """
    text = pytesseract.image_to_string(Image.open(filename), lang='chi_sim')
    return text

#writes text extracted from image into a txt file named "script.txt"
def writefile(image_path, strstr):
	wordlist = strstr.split()
	with open(image_path + '/script.txt', 'a') as f:
		f.writelines("\r".join(wordlist))

# takes text extracted from txt file and translates them, outputs translated
# version into a txt file called "translated.txt" and outputs an image
# file called Capture.JPG.
def translate_text(image_path):
    translator = Translator(to_lang="en", from_lang="zh")
    width = 1000
    height = 1000
    im = Image.new(mode="RGB", size=(width, height), color=(255, 255, 255))

    with open(image_path + '/script.txt', encoding='utf-8') as f:
        contents = f.readlines()

    with open(image_path + '/translated.txt', 'a') as n:
        for line in contents:
            n.writelines(translator.translate(line) + "\n")
            draw = ImageDraw.Draw(im)
            font = ImageFont.truetype("arial.ttf", 15)
            for i in range(9):
                draw.text((10, i*14), translator.translate(line),
                          fill=(0, 0, 0, 0), font=font)
        im.save("Capture.JPG")
        im.show()


# obtain input path and number of files from the user
path = input('file path: ')
nums = input('# of files: ')

# Change the translator provider
# Default is mymemory but it limits the number of translations per day.
# Template code to change provider:
# secret = '<your secret from Microsoft or DeepL>'
# translator = Translator(provider='<the name of the provider, eg. microsoft or deepl>', to_lang=to_lang, secret_access_key=secret)

# I signed up for DeepL account and got this access key but is seems not to be working because mymemory is still used
# secret = '4ab5c119-0001-6b9d-8f3a-a7963bbabbe3'
# translator = Translator(provider='deepl', to_lang="en", secret_access_key=secret)


print("******Starting******")

# This performs the OCR and writes a text file caled script.txt
for n in range(1, int(nums)+1):
    text = ocr_core(path + "/" + str(n) + ".png")
    writefile(path, text)
    print("OCR of image " + str(n) + " is done")

# This performs the translation step (it may take a while)
print("Now performing the translation.")
translate_text(path)

print("~~~~~~Finished~~~~~~")
