"""
    All the function for the manipulation and creation of pokemon card
"""
from os import sep

from PIL import Image
from ImageFont import truetype
from ImageDraw import Draw

from math import floor


def from_dict(data_dict):
    """Generate an image from a dictionary"""

    # * Definition of the path for the base image
    gen = data_dict['generation']
    img_type = data_dict['type']
    stage = data_dict['stage']

    base_path = 'resources' + sep + 'img' \
                + sep + gen \
                + sep + img_type \
                + sep + stage + '.png'

    tmp_img = Image.open(base_path)
    x_max, y_max = tmp_img.size

    # * Add text
    # ?  define fonts

    path_font_folder = 'resources' + sep + 'fonts' + sep

    path_font_name = path_font_folder + 'GillSansStd-Bold.otf'
    font_name = truetype(path_font_name, 25)
    font_hp_str = truetype(path_font_name, 11)

    path_font_hp = path_font_folder + 'FuturaStd-CondensedBold.otf'
    font_hp_nbr = truetype(path_font_hp, 25)

    path_info = path_font_folder + 'GillSansStd.otf'
    font_info = truetype(path_info, 9)

    # ? Define colors
    black = (0, 0, 0)

    tmp_draw = Draw(tmp_img)
    # ? Name
    tmp_draw.text((100, 31), data_dict['name'], font=font_name, fill=black)

    # ? Health point text
    tmp_draw.text((x_max-110, 44), 'HP', font=font_hp_str, fill=black)
    # ? Health point numbers
    tmp_draw.text((x_max-95, 31), data_dict['health'], font=font_hp_nbr, fill=black)

    # ? Information under visual
    set_nb = data_dict['set_number']
    if len(set_nb) == 2:
        set_nb = 'O' + set_nb
    str_info = 'NO. ' + set_nb + ' ' + img_type + ' Pokemon '
    str_info += 'HT ' + data_dict['height'] + ' WT ' + data_dict['weight']

    size_str = font_info.getsize(str_info)[0]
    x_info = floor(x_max/2 - size_str/2)
    y_info = floor(y_max/2)
    tmp_draw.text((x_info, y_info), str_info, font=font_info, fill=black)

    # * Show the image
    tmp_img.show()
