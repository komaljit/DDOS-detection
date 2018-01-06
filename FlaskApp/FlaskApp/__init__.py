from flask import Flask

app= Flask(__name__)

@app.route('/')
def index():
    return """<html>
     <head><title>DDOS TEST</title></head>
     <body>
     <h1>DDOS DETECTION TEST</h1>
     <div style="text-align:center;">
     <img src="static/1.jpg">
     </div>
     </body>
     </htmml>"""

