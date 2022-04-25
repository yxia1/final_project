# from crypt import methods
from flask import Flask, render_template, request, flash
from colormind_helper import get_palette

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/color/", methods=["GET", "POST"])

def generate_palette():
    if request.method == "POST":
        color_name = request.form["color"]
        generated_palette = get_palette(color_name)

        if generate_palette:
            return render_template("color_result.html",
            color1=generated_palette[0],
            color2=generated_palette[1],
            color3=generated_palette[2],
            color4=generated_palette[3],
            color5=generated_palette[4])
        else:
            # return "There is no such color."
            # flash('Looks like this color is not available :(')
            return render_template("color_form.html", error=True)
            
    return render_template("color_form.html", error=None)

@app.route("/app")

def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)
