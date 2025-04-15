from flask import Flask, render_template, request
from quotes_handler import load_quotes, get_random_quote

app = Flask(__name__)

@app.route("/")
def home():
    category = request.args.get("category", "motivation")
    quotes = load_quotes(category)
    quote = get_random_quote(quotes)
    return render_template("index.html", quote=quote, category=category)

if __name__ == "__main__":
    app.run(debug=True, port=5050)
