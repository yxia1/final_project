import json
from unittest import result
import urllib.parse
import urllib.request

import requests
import json
import urllib.parse
import urllib.request

# data = '{"input":[[44,43,44],"N","N","N","N"],"model":"default"}'
# response = requests.post("http://colormind.io/api/", data=data)
# results = response.json()
# generated = results["result"]
# print(generated)

# 1. convert color name into rgb
def read_txt_to_dict():
    """
    Thиs function opens a txt file containing all color information. Then it reads it into a dictionary with the color names as keys and rgb as values.
    """
    f = open("data/colors.txt")
    d = dict()

    for line in f:
        row = line.strip()
        color = row.split(",")
        color_name = color[0]
        d[color_name] = list(map(int, color[3:]))
    d["green"] = [0, 255, 0]
    d["purple"] = [125, 0, 125]
    d["orange"] = [255, 215, 0]
    return d

def convert_input(user_input):
    """
    This function converts the user color input into a usable format. 
    """
    # try and except might be helpful
    # raise errors
    user_input = user_input.lower()
    user_input = user_input.replace(" ", "_")
    return user_input

#_____________________________________
# TO DO:
#_____________________________________

# 2. Generate color palette
## Communication with API Part
def clean_API_input(rgb_value):
    """
    The function takes a user_input of rgb as a list and returns the input that the colormind API accepts
    ie.'{"input":[[44,43,44],"N","N","N","N"],"model":"default"}'
    string of a dictionary
    """
    data_dict = {}
    
    data_dict["input"] = [rgb_value, "N","N","N","N"]
    data_dict["model"] = "default"
    # print(data_dict)
    
    return data_dict


def post_color(clean_API_input):
    """
    This function takes the clean input and post it to the colormind API to get the generated API
    """
    
    url = "http://colormind.io/api/"
    data = json.dumps(clean_API_input)
    data = bytes(data.encode("utf-8"))
    req = urllib.request.Request(url, data, method="POST")
    with urllib.request.urlopen(req) as response:
        response_text = response.read().decode('utf-8')
        j = json.loads(response_text)
    return j



# 3. where everything comes together

def get_palette(color_name):
    """
    Return a matching palette.
    """
    color_dict = read_txt_to_dict()
    rgb_input = color_dict[convert_input(color_name)]

    palette_input = clean_API_input(rgb_input)
    palette = post_color(palette_input)
    result = palette["result"]
    # colors = (result[0], result[1], result[2], result[3], result[4])
    return result


def main():
    """
    You can test all the functions here
    """
    print(get_palette("beige"))


if __name__ == "__main__":
    main()

#_____________________________________
# Unused bits:
#_____________________________________


def rgb_to_hex(rgb):
    """
    This function takes a rgb color and returns its hex code.
    """
    # might need this for html
    return f"#" "%02x%02x%02x" % rgb
