from chatbot import chatbot
from flask import Flask, render_template, request

app = Flask(__name__)
app.static_folder = 'static'

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    #name = input("Enter Your name")
    #print('Welcome to WIWEB', name, 'Let me know how can i help you ?')
    userText = (request.args.get('msg'))
   # while True:
       # userText = input(name + ':')
    #    if userText == 'Bye' or userText == 'bye':
     #       chatbot.get_response(userText)
      #  break

   #userText = (request.args.get('msg'))
    return str(chatbot.get_response(userText))

if __name__ == "__main__":
    app.run(debug=True)