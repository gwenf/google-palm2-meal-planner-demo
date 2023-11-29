# FoodieAIdvisor

An AI-powered, interactive terminal application designed to manage your ingredients inventory, understand your personal tastes, and recommend recipes that tantalize your palate while reducing food waste.

[Workshop steps if you are following along.](WORKSHOP.md)

[Definitions for terms used in, and related to, this project.](DEFINITIONS.md)

## Features

- **User Onboarding**: Initial questions about food preferences and dietary restrictions.
- **Inventory Management**: Keep track of the ingredients you have.
- **Recipe Recommendations**: Uses the Google Palm API to suggest three recipes based on the ingredients you possess and your personal preferences.
- **Update User Preferences**: Add or delete your food preferences and dietary restrictions at any time.
- **SQLite Database**: Lightweight, serverless, self-contained SQL database engine.

## Getting Started

### Prerequisites

- Python 3.11+
- SQLite

### Installation

Make sure Python is installed on your computer. This project has been tested with Python version 3.11.

Check your Python version:
`python --version`

1. Clone the repository:

```
git clone https://github.com/yourusername/FoodieAIdvisor.git
cd FoodieAIdvisor
```

2. Create a virtual environment:

```
python -m venv venv
source venv/bin/activate
```

3. Install required packages:

With Pip:
```
pip install -r requirements.txt
```

With Poetry (make sure Poetry is installed on your system):
```
poetry install
```

4. Run the `db_setup.py` to set up the SQLite database:

```
python meal_planner/db_setup.py
```

5. Start the terminal application:

```
python main.py
```

*Remember to replace placeholder URLs, paths, and other specifics with actual details of your project.*

## Usage

The terminal application will guide you through:

1. Onboarding: Add your initial preferences.
2. Inventory Management: Update your current ingredients.
3. Recipe Recommendations: Based on your ingredients and preferences.
4. Manage Preferences: Update or delete your food preferences and restrictions.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Important Links

- [Google Palm API](https://developers.google.com/products)
- [SQLite](https://www.sqlite.org/index.html)
