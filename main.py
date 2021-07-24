from PIL import Image
import pytesseract

img = Image.open('answer1.png')

text = pytesseract.image_to_string(img, lang='eng')
print(text)


