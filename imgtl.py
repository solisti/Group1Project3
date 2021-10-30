import pytesseract
from PIL import Image
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
    width = 1000
    height = 1000
    im  = Image.new( mode = "RGB", size = (width, height), color = (255, 255, 255) )
    translator = Translator(to_lang="en", from_lang="zh")

    with open(image_path + '/script.txt', encoding='utf-8') as f:
        contents = f.readlines()

    with open(image_path + '/translated.txt', 'a') as n:
        for line in contents:
            n.writelines(translator.translate(line) + "\n")
            draw = ImageDraw.Draw(im)
            font = ImageFont.truetype("arial.ttf", 15)
            for i in range(9):
                draw.text((10, i*14), translator.translate(line), fill=(0,0,0,0), font=font)
        im.save("Capture.JPG");
        im.show();

path = input('file path: ')
nums = input('# of files: ')

print("******starting******")

for n in range(1, int(nums)+1):
    text = ocr_core(path + "/" + str(n) + ".png")
    writefile(path, text)
    print("image " + str(n) + " is done")

print("~~~~~finished~~~~~")

translate_text(path)
