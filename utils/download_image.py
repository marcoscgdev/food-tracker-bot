import os
import urllib.request as req
from PIL import Image

def download_image(imgurl):
	extension = imgurl.split(".")[-1]
	f_name = "predict_image_original." + extension
	req.urlretrieve(imgurl, f_name)

	im = Image.open(f_name)
	rgb_im = im.convert('RGB')
	new_img = rgb_im.resize((224,224))

	new_img.save("predict_image.jpg", "JPEG", optimize=True)

	os.remove(f_name) # Remove original image

	return "./predict_image.jpg"
