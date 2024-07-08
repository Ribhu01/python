# Password Manager

A simple password manager built with Python and Tkinter. This application allows users to generate strong passwords,
save them securely, and retrieve them when needed.

## Features

- **Password Generation**: Automatically generate strong, random passwords with a mix of letters, numbers, and symbols.
- **Save Passwords**: Store passwords securely in a JSON file.
- **Retrieve Passwords**: Easily find saved passwords using the website name.
- **Copy Passwords**: Copy the generated password to the clipboard for easy use.

## Installation

1. **Clone the repository**
    ```sh
    git clone https://github.com/yourusername/password-manager.git
    cd password-manager
    ```

2. **Install the required packages**
    ```sh
    pip install pyperclip
    ```

## Usage

1. **Run the application**
    ```sh
    python password_manager.py
    ```

2. **Generate a password**
    - Click on the "Generate Password" button to create a new password.
    - The generated password will be displayed in the password entry field and copied to your clipboard.

3. **Save a password**
    - Enter the website name, email/username, and the generated password.
    - Click on the "Add" button to save the password.
    - The password will be stored in the `data.json` file.

4. **Retrieve a password**
    - Enter the website name for which you want to find the password.
    - Click on the "Search" button.
    - If the website exists in the `data.json` file, a message box will display the email/username and password for the website.

## Files

- **password_manager.py**: The main script for the password manager.
- **data.json**: The file where passwords are stored.
- **logo.png**: The logo image displayed in the application.

## Dependencies

- **Python 3.x**
- **tkinter**: Standard Python interface to the Tk GUI toolkit.
- **pyperclip**: A cross-platform clipboard module for Python.




