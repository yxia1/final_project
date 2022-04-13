import requests
data = '{"input":[[44,43,44],"N","N","N","N"],"model":"default"}'
response = requests.post('http://colormind.io/api/', data=data)
results = response.json()
generated = results['result']
print(generated)

def read_txt_to_dict():
    """
    The function open the txt file and read it into a dictionary with the color name as keys and rgb as values
    """
    f = open('data/colors.txt')
    d = dict()
    
    for line in f:
        row = line.strip()
        color = row.split(',')
        color_name= color[0]
        d[color_name] = list(map(int, color[3:]))
    return d

print(read_txt_to_dict())

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



def get_palette(clean_input):
    """
    this function takes the clean input and post it to the colormind api to get the generated API
    """
    pass

def rgb_to_hex(rgb):
    """
    This function takes a rgb color and returns its hex code.
    """
    return f'#''%02x%02x%02x' % rgb

def color_to_rgb(color_name):
    """
    takes a color name and returns a rgb as a list
    reference: https://data-flair.training/blogs/project-in-python-colour-detection/
    """
    pass

def get_palette(rgb):
    """
    the function takes an input of rgb and return the color palette from colormind
    """
    pass
