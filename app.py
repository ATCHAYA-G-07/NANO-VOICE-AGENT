from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():

    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():

    user_message = request.json["message"].lower()

    if "hello" in user_message:

        reply = "👋 Hello! I am Nano Voice Agent."

    elif "laptop" in user_message:

        reply = "💻 Lenovo, ASUS and HP are great for coding."

    elif "phone" in user_message:

        reply = "📱 Samsung and iPhone are trending now."

    elif "headphones" in user_message:

        reply = "🎧 Sony and JBL headphones are very popular."

    elif "ai" in user_message:

        reply = "🤖 AI means Artificial Intelligence."

    else:

        reply = "🚀 I am learning more every day."

    return jsonify({
        "reply": reply
    })


if __name__ == "__main__":

    app.run(debug=True)