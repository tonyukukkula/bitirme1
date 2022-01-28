import os
from PIL import Image

def resizeIMG():
	for filename in os.listdir('yapacaginizisin'):
		img = Image.open('yapacaginizisin/' +filename)
		img = img.resize((1000,1000), Image.ANTIALIAS)
		img.save('yapacaginizisinresized/'+filename)
	return "islem bitti"

resizeIMG()
