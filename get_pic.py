from PIL import Image, ImageFont, ImageDraw
import textwrap
# Lembrar de instalar
# fonte dokcer


def get_pic(quote):
    image = Image.new('RGB', (800, 500), color=(0, 0, 0))
    # font = ImageFont.truetype('decarySans/DecarySans.ttf', 18)
    font = ImageFont.load_default()
    text_color = (200, 200, 200)
    text_start_height = 200
    # heigth, width
    # text_coord = (100,200)
    # image_editable = ImageDraw.Draw(image)
    # image_editable.text(text_coord, quote, text_color, font=font)
    write_text_on_image(image, quote, font, text_color, text_start_height)
    image.save('img_quote.png')

def write_text_on_image(image, text, font, text_color, text_start_height):
    draw = ImageDraw.Draw(image)
    image_width, image_height = image.size
    y_text = text_start_height
    lines = textwrap.wrap(text, width=40)
    for line in lines:
        line_width, line_height = font.getsize(line)
        draw.text(((image_width - line_width) / 2, y_text),line, font=font, fill=text_color)
        y_text += line_height