# daily_nope.py

from quotes_handler import get_categories, load_quotes, get_random_quote


def show_intro():
    """
    Prints the welcome message at the start of the program.
    """
    print("\n🖤 Welcome to The Daily Nope 🖤")
    print("Your personal coach for unspirational self-improvement.\n")


def show_menu(categories):
    """
    Displays the category selection menu.

    Args:
        categories (dict): Dictionary of categories (key = number, value = name)
    """
    print("Please make a selection:")
    print("Which category do you need 'help' with today?\n")
    for key, name in categories.items():
        print(f"{key} – {name}")
    print("q – quit")


def main():
    """
    Runs the main CLI loop.
    """
    categories = get_categories()
    show_intro()

    while True:
        show_menu(categories)
        choice = input("\nYour choice: ").strip()

        if choice.lower() == "q":
            print("\nThanks for stopping by. Stay nopeful. 👋")
            break

        category = categories.get(choice)
        if not category:
            print("⚠️ Invalid selection. Please try again.\n")
            continue

        quotes = load_quotes(category)
        quote = get_random_quote(quotes)
        print(f"\n💬 {quote}\n")

        again = input("Wanna try again? (y/n): ").strip().lower()
        if again != "y":
            print("\nMay your day be as average as expected. Bye!")
            break


if __name__ == "__main__":
    main()
