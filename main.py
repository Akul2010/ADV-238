import hashlib

filename="project_238_img.jpg"

with open(filename,'rb') as f:
	file_data=f.read()

image_hash=hashlib.sha256(file_data).hexdigest()

print(image_hash)
