import requests
data = '{"input":[[44,43,44],[90,83,82],"N","N","N"],"model":"default"}'
response = requests.post('http://colormind.io/api/', data=data)
results = response.json()
generated = results['result']
print(generated)

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


