# FoodieAIdvisor - An AI-powered terminal-based recipe advisor
import sqlite3

from colorama import init, Fore, Back, Style
import pyfiglet
from google.cloud import aiplatform
from vertexai import preview

from meal_planner.db_setup import setup_database
from meal_planner.user_preferences import (
    update_user_preferences,
    delete_user_preferences,
)
from meal_planner.onboarding import onboard_user

DATABASE_PATH = "foodieaidvisor.db"

# Global Setup
# GOOGLE_API_ENDPOINT = "https://generativelanguage.googleapis.com/..."

###
# Initialization Functions
###
setup_database()


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


# User Management Functions


# Inventory Management Functions

# def add_ingredients():
#     """Allow the user to add ingredients to their inventory."""

# def list_ingredients():
#     """List all ingredients in the user's inventory."""

# def delete_ingredient():
#     """Allow the user to delete an ingredient from their inventory."""

# def set_expiration_date():
#     """Allow the user to set expiration dates for ingredients."""


# Recipe Recommendation Functions

# def get_recommendations():
#     """Fetch recipe recommendations based on user preferences and inventory."""

# def select_recipe():
#     """Let the user select a preferred recipe from recommendations."""

# def rate_recipe():
#     """Allow the user to rate a recipe after trying it."""


# Google Palm API Integration

# def fetch_from_google_palm(prompt):
#     """Fetch results from Google's Palm API."""
#     # Use the google-cloud-python client to communicate with the API
