from colorama import init, Fore, Back, Style
import pyfiglet
import sqlite3

DATABASE_PATH = "foodieaidvisor.db"


def setup_terminal_ui():
    """Initialize colorama and other terminal UI settings."""

    init(autoreset=True)

    # Display the ASCII header using PyFiglet
    header = pyfiglet.figlet_format("FoodieAIdvisor", font="slant")
    print(Fore.CYAN + header)

    print(
        Fore.GREEN
        + "Welcome to FoodieAIdvisor - Your AI-powered Recipe Advisor!"
    )
    print(Fore.YELLOW + "Enter 'help' anytime to see available commands.\n")


def select_user():
    """Select or create a new user."""
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT username FROM users")
    users = cursor.fetchall()

    if users:
        print("Existing Users:")
        for index, user in enumerate(users, 1):
            print(f"{index}. {user[0]}")
        print(f"{len(users) + 1}. Create New User")
        choice = int(input("Select a user or create a new one: "))

        if 1 <= choice <= len(users):
            selected_user = users[choice - 1][0]
        else:
            selected_user = input("Enter a new username: ").strip()
            cursor.execute(
                "INSERT INTO users (username) VALUES (?)", (selected_user,)
            )
            conn.commit()

    else:
        selected_user = input("Enter a new username: ").strip()
        cursor.execute(
            "INSERT INTO users (username) VALUES (?)", (selected_user,)
        )
        conn.commit()

    # Fetch the user_id of the selected user
    cursor.execute("SELECT id FROM users WHERE username = ?", (selected_user,))
    user_id = cursor.fetchone()[0]

    cursor.execute("DELETE FROM active_user")  # Clear any previous active user
    cursor.execute(
        "INSERT INTO active_user (user_id, username) VALUES (?, ?)",
        (user_id, selected_user),
    )
    conn.commit()
    conn.close()

    return selected_user


def get_active_user_id():
    """Get the ID of the currently active user."""
    with sqlite3.connect(DATABASE_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT user_id FROM active_user LIMIT 1")
        result = cursor.fetchone()
        if result:
            return result[0]
        else:
            raise Exception(
                "No active user. Please select or create a user first."
            )
