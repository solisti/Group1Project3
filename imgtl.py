try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import translate
from translate import Translator

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

#takes text extracted from txt file and translates them, outputs translated version into a txt file called "translated.txt"
def translate_text(image_path):
    translator = Translator(to_lang="en", from_lang="zh")

    with open(image_path + '/script.txt', encoding='utf-8') as f:
        contents = f.readlines()

    with open(image_path + '/translated.txt', 'a') as n:
        for line in contents:
            n.writelines(translator.translate(line) + "\n")

path = input('file path: ')
nums = input('# of files: ')

print("******starting******")

for n in range(1, int(nums)+1):
    text = ocr_core(path + "/" + str(n) + ".png")
    writefile(path, text)
    print("image " + str(n) + " is done")

print("~~~~~finished~~~~~")

translate_text(path)
