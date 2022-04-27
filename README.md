
# ColorPal 🎨


### The Big Idea

Looking for the perfect color palette? Let ColorPal help you!

Colors are all around us. But sometimes it is hard to imagine the perfect color combination. So, our project ColorPal is here to suggest the best 5-color paltte based on your main color. And if you are not happy with the combination, don't worry. Just press the refresh button and a new color combination will appear. You could try as many times as your heart desires!
## 🎀 Authors

- [@Carrie](https://www.github.com/yxia1)
- [@Martina](https://www.github.com/LSE2021)


## ⚡️ Main Features

- Home page describing the main function of the website
- Color page where users can input the name of their main color for the palette
- Result page with a generated color palette consisting of five colors and their respective HEX code



## 📌 The Details

ColorPal uses the Colormind API key to generate a five-color palette based on one given color. Please, visit the [Colormind API Documentation](http://colormind.io/api-access/) for more information.

The beauty of ColorPal is that users do not need to know the exact RGB code of their main color. When a user inputs a color name, the program will convert it to its relevant RGB color code. This is possible thanks to a database containing all color names and their RGB and HEX information. The returned RGB code is used as an input to the Colormind API key. 

Once the color palette has been generated, the user still has an opportunity to change it. A refresh button appears at the bottom of the screen, which allows for a generation of a new color palette based on the same input color.

The rest is a user-friendly HTML design, whcih allows for an easy usage by everyone. Enjoy!

## 📚 Libraries Used

Main python code libraries are detailed below:
```javascript
import json
from unittest import result
import urllib.parse
import urllib.request
import requests
import json
import urllib.parse
import urllib.request
```
Libraries used in building the app:
```javascript
from flask import Flask, render_template, request
```
## 🚀 Running the Website

- Server Running: just run the ```app.py``` file, click the local server and begin your ColorPal journey. You could use the bar at the top to hoover over the three tabs. Click on "ABOUT US" and you could see more information about the authors. Please, return with the back arrow before you proceed. Click on "COLOR" and input the name of your color or the HEX code. Then click "Generate" and a color palette will appear. 

- Web Running: we implemented a [Heroku](https://www.heroku.com/) website which is available online without running the Python code. Please, follow the links below: 
[Home](https://colorpal-co.herokuapp.com/)
[Color Generator](https://colorpal-co.herokuapp.com/color/)
[About](https://colorpal-co.herokuapp.com/about)

### Enjoy!