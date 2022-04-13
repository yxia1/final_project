import requests

data = '{"input":[[44,43,44],"N","N","N","N"],"model":"default"}'
response = requests.post("http://colormind.io/api/", data=data)
results = response.json()
generated = results["result"]
print(generated)

# 1. convert color name into rgb
def read_txt_to_dict():
    """
    The function open the txt file and read it into a dictionary with the color name as keys and rgb as values
    """
    f = open("data/colors.txt")
    d = dict()

    for line in f:
        row = line.strip()
        color = row.split(",")
        color_name = color[0]
        d[color_name] = list(map(int, color[3:]))
    return d

def convert_input(input):
    """
    this function takes out the blank space in users' input and makes it lower cases to match with the color dictionary keys
    """
    input = input.lower()
    input = input.replace(" ", "_")
    return input

#_____________________________________
# TO DO:
#_____________________________________

# 2. Generate color palette
## Communication with API Part
def clean_API_input(user_input):
    """
    the function takes a user_input of rgb as a list and returns the input that the colormind API accepts
    ie.'{"input":[[44,43,44],"N","N","N","N"],"model":"default"}'
    string of a dictionary
    """
    user_input = list(user_input)
    data = {}
    data.keys = "input"
    data.keys = "model"


def get_palette(clean_API_input):
    """
    this function takes the clean input and post it to the colormind api to get the generated API
    """
    pass

# 3. where everything comes together

def final(color_name):
    """
    return whatever we nee
    """


def main():
    """
    You can test all the functions here
    """
    color_dict = read_txt_to_dict()
    print(color_dict[convert_input('green')])



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
