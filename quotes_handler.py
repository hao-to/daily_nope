import json
import os
import random

# Folder where the JSON quote files are stored
QUOTES_DIR = "quotes"


def get_categories():
    """
    Returns available categories as a dictionary.
    Keys are numbers as strings, values are category names.
    This is used to show a selection menu in the CLI or Web app.
    """
    return {
        "1": "affirmation 🧘‍",
        "2": "motivation 🏁",
        "3": "preppin 📋",
        "4": "gratitude 🙏",
        "5": "inner_truths 🪞"
    }


def load_quotes(category_name):
    """
    Loads quotes from the corresponding JSON file.

    Args:
        category_name (str): The name of the category, e.g., 'motivation'.

    Returns:
        list: A list of quotes as strings.
    """
    filename = f"{category_name}.json"
    filepath = os.path.join(QUOTES_DIR, filename)

    try:
        with open(filepath, "r", encoding="utf-8") as file:
            data = json.load(file)
            return data.get("quotes", [])  # get list under "quotes" key
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading file {filename}: {e}")
        return []


def get_random_quote(quotes):
    """
    Picks a random quote from a list.

    Args:
        quotes (list): A list of strings (quotes).

    Returns:
        str: A random quote from the list.
    """
    if not quotes:
        return "No quotes found."
    return random.choice(quotes)
