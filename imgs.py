#@title Download and check the images you have just added
import os
import requests
from io import BytesIO
from PIL import Image

urls = [
    "https://i.imgur.com/UqrhwBx.jpeg",
    "https://i.imgur.com/pp8UcmF.jpg",
    "https://i.imgur.com/qxwltq3.jpg",
    "https://i.imgur.com/1voWlQ5.jpg",
    "https://i.imgur.com/T8m2Oix.jpg",
    "https://i.imgur.com/FSdOXEZ.jpg",
    "https://i.imgur.com/uZrWSlL.jpg",
    "https://i.imgur.com/CoQoTFq.jpg",
    "https://i.imgur.com/Q1ermC9.jpg",
    "https://i.imgur.com/n2c8jaf.jpg",
    "https://i.imgur.com/n2LxHS0.jpg",
    "https://i.imgur.com/s6b5cdA.jpg",
    "https://i.imgur.com/3L80jAv.jpg",
    "https://i.imgur.com/TJMSVDp.jpg",
    "https://i.imgur.com/B29El3c.jpg"
]

def image_grid(imgs, rows, cols):
 assert len(imgs) == rows*cols

 w, h = imgs[0].size
 grid = Image.new('RGB', size=(cols*w, rows*h))
 grid_w, grid_h = grid.size

 for i, img in enumerate(imgs):
  grid.paste(img, box=(i%cols*w, i//cols*h))
 return grid

def download_image(url):
 try:
  response = requests.get(url)
 except:
  return None
 return Image.open(BytesIO(response.content)).convert("RGB")

images = list(filter(None,[download_image(url) for url in urls]))
save_path = "./training_images"
if not os.path.exists(save_path):
 os.mkdir(save_path)
[image.save(f"{save_path}/{i}.png", format="png") for i, image in enumerate(images)]
image_grid(images, 1, len(images))
