from flask import Flask, jsonify, request, render_template, url_for
import random
import requests, json

app = Flask(  # Create a flask app
    __name__,
    template_folder='templates',  # Name of html file folder
    static_folder='static'  # Name of directory for static files
)

# Variables for tasks
image_link = "https://scontent.ftlv21-1.fna.fbcdn.net/v/t31.18172-1/1502644_10152506946962507_2442851309927378964_o.png?stp=c49.0.148.148a_dst-png_p148x148&_nc_cat=111&ccb=1-7&_nc_sid=1eb0c7&_nc_ohc=d-R_wjIm2d8AX_NugPv&_nc_ht=scontent.ftlv21-1.fna&oh=00_AT8CSjiG8-biys_qQ9tU-yrxzJSp6HANxsz5c3mFVk-G2Q&oe=62FD0A1B"

user_bio = "hello. am monke. eat banan."

posts = {
    "https://play-lh.googleusercontent.com/T_vA5l9W1-XYTmgr3gCB2MBd7QmA-iG0wcm09_IFWNB-4gOpnS-tYNEmcalwdixSyw": "update! in shock. my uncle passed away and i get all of his property :(",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSvb2k9uozSEYzdJ8QXDHyni81lHdtNWX39rQ&usqp=CAU": "ha! funny picture. my best friend made it.",
    "https://i.scdn.co/image/ab67616d0000b273f7e413deedb59840b2b8c2c9": "school photo! how did it turn out?x",
    "https://cdn3.emoji.gg/emojis/2031-monke-serious.png": "say hi to my grandad! my idol, legend, champion banan muncher. i love you popsie."}


#####


@app.route('/')  # '/' for the default page
def home():
    return render_template('index.html', image_link=image_link, user_bio=user_bio, posts=posts)


@app.route('/about')  # '/' for the default page
def about():
    return render_template('about.html')


if __name__ == "__main__":  # Makes sure this is the main process
    app.run(debug=True)
