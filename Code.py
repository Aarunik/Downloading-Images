import urllib

def downloading_image():
    filename=raw_input("Enter the file name ")
    fullname=filename+".jpg"
    image_url=raw_input("Enter the image's url ")
    urllib.urlretrieve(image_url,fullname)

downloading_image()
