from PIL import Image, ImageFont, ImageDraw
import textwrap
from pyunsplash import PyUnsplash
import requests
import shutil
# Lembrar de instalar
# fonte docerr

from config import *

def get_pic(quote):
    
    
    # Get random pic from unsplash
    pu = PyUnsplash(api_key=UNSPLASH_ACCESS_KEY)
    
    photos = pu.photos(type_='random', count=1, featured=True, query="splash")
    [photo] = photos.entries
    print(photo.id, photo.link_download)

    response = requests.get(photo.link_download, allow_redirects=True, stream=True)
    # path to save image
    path = "img.jpg"

    if response.status_code == 200:
        with open(path, 'wb') as f:
            response.raw.decode_content = True
            shutil.copyfileobj(response.raw, f) 
            print('Image Downloaded Successfully') 
    

    image = Image.open("img.jpg")

    image_width, image_height = image.size
    print(image_width)
    y_text = image_height/2 -50
    font = ImageFont.truetype("fonts/raleway/Raleway-SemiBold.ttf", 200, encoding="unic")
    text_color = (255, 195, 0 )
    stroke_color = (0, 0, 0)

    canvas = ImageDraw.Draw(image)

    lines = textwrap.wrap(quote, width=30)
    for line in lines:
        line_width, line_height = font.getsize(line)
        canvas.text(((image_width - line_width) / 2, y_text),line, font=font, fill=text_color, stroke_width=2, stroke_fill=stroke_color)
        y_text += line_height

    image.save("result.jpg")