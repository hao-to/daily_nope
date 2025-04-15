# ☁️ The Daily Nope
![Built with Python](https://img.shields.io/badge/Built_with-Python_3.10-blue?logo=python&logoColor=white)
![License: MIT](https://img.shields.io/badge/License-MIT-brightgreen)
![Mood: Nope](https://img.shields.io/badge/Mood-Why_even_try-red)
![Snark Level](https://img.shields.io/badge/Snark-High-purple)
![Motivation](https://img.shields.io/badge/Motivation-None-black)

> Your personal CLI coach for unspirational self-improvement™.

Because sometimes, what you really need isn’t motivation –
but sarcasm, snacks, and a reason to laugh at your own chaos.

---

## 🤔 What is this?

The Daily Nope is a Python-powered CLI app that delivers snarky affirmations, confusing truths, and mildly chaotic prep-advice.

Choose your category:

- `affirmation` – You're enough. Just not for this.
- `motivation` – Get up. Or don’t. We won't judge.
- `preppin` – Prep like you mean it. Or like you have snacks.
- `gratitude` – Say thanks. Even if it's just to your coping mechanisms.
- `inner truths` – Spiritual-ish nonsense for existential flair.

---

## 🛠 How to use

1. Clone the repo:
```bash
git clone https://github.com/hao-to/daily_nope.git
cd daily_nope
```
2. Run the CLI:
```bash
python3 daily_nope.py
```

3. Choose a category and receive the nope you never asked for.


---

## 🖥️ How to use in the browser

Prefer clicking over typing? The Daily Nope now has a web version!

### 🚀 Run the Web App locally

1. Clone the repo:
   ```bash
   git clone https://github.com/hao-to/daily_nope.git
   cd daily_nope
   ```

2. (Optional) Create and activate a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
```

3. Install the requirements:
```bash
pip install -r requirements.txt
```

4. Start the Flask app:
```bash
python3 flask_app.py
```

5. Open your browser and enjoy the nope:
```bash
http://localhost:5050
```
✨ Bonus: You get slowly typed quotes, glowing buttons, and absolutely zero useful advice.

## 📂 Project Structure

```
daily_nope/
├── quotes/               # JSON files with quotes
│   ├── affirmation.json
│   ├── motivation.json
│   ├── preppin.json
│   ├── gratitude.json
│   └── inner_truths.json
├── static/
│   └── style.css         # CSS for the web version
├── templates/
│   └── index.html        # HTML template for the Flask app
├── quotes_handler.py     # Loads quotes and picks one
├── daily_nope.py         # CLI interface
├── flask_app.py          # Flask web server
├── requirements.txt      # Project dependencies
├── .gitignore
└── README.md             # You're reading it!
```
✨ Why?

Because toxic positivity is exhausting, and you're doing your best.
This is for the realists, the overwhelmed, the ironically hopeful, and those who have no idea what they’re doing (but still show up).

🖤 Contributions

Got your own sarcastic truths or ironic insights?
Feel free to fork and create a pull request – but keep it on theme:
no real motivation allowed.

📄 License

MIT – because even snark deserves freedom.