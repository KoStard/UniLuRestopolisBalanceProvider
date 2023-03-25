# Restopolis Balance Checker

Restopolis Balance Checker is a small Python script that retrieves the balance of your Restopolis card from the University of Luxembourg's student portal. It also includes a simple Telegram bot that sends the balance to a predefined user ID once every evening.

## Installation

1. Clone the package to your local machine.
2. Install the required dependencies by running the following command in your terminal:

    ```
    pip install -r requirements.txt
    ```

3. Set the environment variables `RESTOPOLIS_USERNAME`, `RESTOPOLIS_PASSWORD`, `TELEGRAM_API_KEY`, and `PREDEFINED_CHAT_ID` with your Uni.lu credentials and Telegram bot information. In the beginning, you won't know the `PREDEFINED_CHAT_ID`, so just start the bot, call the `/start` command, and then check the console output for the `chat_id` value.

## Usage

To use the script, run the following command in your terminal:

```
python restopolis_balance_provider.py
```

This will print the balance of your Restopolis card to the console. To use the Telegram bot, run the following command in your terminal:

```
python simple_telegram_bot.py
```

This will start the bot and send the balance of your Restopolis card to the specified Telegram user once every evening after getting the /start command from the right user.

## Troubleshooting

If you encounter any issues while running the script or the bot, make sure that your Uni.lu username and password and Telegram bot credentials are correct and that the environment variables are set correctly. If the issue persists, please submit a bug report in the Issues section of this repository.

## Development

For development, it is recommended to use a Python virtual environment to manage dependencies. To create a new virtual environment and install the required dependencies, run the following commands in your terminal:

```
python -m venv env
source env/bin/activate
pip install -r requirements.txt
```

To tidy the dependencies from the virtual environment before freezing the requirements, you can use the `pip-autoremove` package:

```
pip-autoremove --freeze > requirements.txt
```

## Notes from learning

### How to understand what authentication is required for a website?
1. Open the website in your browser
2. Open the developer tools (F12)
3. Go to the network tab
4. Reload the page
5. Look for the request that is sent to the server when you log in. But in this case, I couldn't find it. After some discussions with ChatGPT, describing what I see when the login happens (the username and password is asked with a chrome native popup, not with a web page), I found this header from the response with 401 status code:
    ```
    WWW-Authenticate: NTLM
    ```
6. After this, it was just about finding the right library to use. I found this library (requests-ntlm), which let me log into it.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.