import requests
data = '{"input":[[44,43,44],"N","N","N","N"],"model":"default"}'
response = requests.post('http://colormind.io/api/', data=data)
results = response.json()
generated = results['result']
print(generated)

def clean_input(user_input):
    """
    the function takes a user_input of rgb as a list and returns the input that the colormind API accepts
    ie.'{"input":[[44,43,44],"N","N","N","N"],"model":"default"}'
    string of a dictionary 
    """
    user_input = list(user_input)
    data = {}
    data.keys = "input"
    data.keys = "model"
    data["input"] = 

def get_palette(clean_input):
    """
    this function takes the clean input and post it to the colormind api to get the generated API
    """

def rgb_to_hex(rgb):
    """
    This function takes a rgb color and returns its hex code.
    """
    return f'#''%02x%02x%02x' % rgb
print(rgb_to_hex((255, 255, 195)))


def color_to_rgb(color_name):
    """
    takes a color name and returns a rgb as a list
    reference: https://data-flair.training/blogs/project-in-python-colour-detection/
    """
    pass

def get_palette(rgb):
    """
    the function takes an input of rgb 
    """
# 