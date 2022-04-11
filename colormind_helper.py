import requests
data = '{"input":[[44,43,44],[90,83,82],"N","N","N"],"model":"default"}'
response = requests.post('http://colormind.io/api/', data=data)
results = response.json()
generated = results['result']
print(generated[0])


def color_to_rgb(color_name):
    """
    takes a color name and returns a rgb
    reference: https://data-flair.training/blogs/project-in-python-colour-detection/
    """
    pass
