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
def clean_API_input(clean_input):
    """
    The function takes a user_input of rgb as a list and returns the input that the colormind API accepts
    ie.'{"input":[[44,43,44],"N","N","N","N"],"model":"default"}'
    string of a dictionary
    """
    data_dict = {}
    
    clean_input = convert_input(clean_input)
    color_dict = read_txt_to_dict()
    rgb_value = color_dict[clean_input]
    data_dict["input"] = [rgb_value, "N","N","N","N"]
    data_dict["model"] = "default"
    # print(data_dict)
    
    return data_dict


def get_palette(clean_API_input):
    """
    This function takes the clean input and post it to the colormind API to get the generated API
    """
    
    # response = requests.post("http://colormind.io/api/", data=clean_API_input)
    # results = response.json()
    # generated = results["result"]
    # print(generated)
    
    url = "http://colormind.io/api/"
    data = json.dumps(clean_API_input)
    data = bytes(data.encode("utf-8"))
    req = urllib.request.Request(url, data, method="POST")
    with urllib.request.urlopen(req) as response:
        palette = response.read()
        return palette


def final_palette(color_name):
    """
    Return a matching palette.
    """
    user_input = convert_input(color_name)
    # color_dict = read_txt_to_dict()
    # print(color_dict[convert_input(color_name)])
    palette_input = clean_API_input(user_input)
    print(get_palette(palette_input))

def main():
    """
    You can test all the functions here
    """
    final_palette("Wood Brown")



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
