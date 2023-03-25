# Restopolis Balance Checker

Restopolis Balance Checker is a small Python script that retrieves the balance of your Restopolis card from the University of Luxembourg's student portal. 

## Installation

1. Clone the package to your local machine.
2. Install the required dependencies by running the following command in your terminal:

    ```
    pip install -r requirements.txt
    ```

3. Set the environment variables `RESTOPOLIS_USERNAME` and `RESTOPOLIS_PASSWORD` with your Uni.lu credentials.

## Usage

To use the script, run the following command in your terminal:

```
python restopolis_balance_provider.py
```

This will print the balance of your Restopolis card to the console.

## Troubleshooting

If you encounter any issues while running the script, make sure that your Uni.lu username and password are correct and that the environment variables `RESTOPOLIS_USERNAME` and `RESTOPOLIS_PASSWORD` are set correctly. If the issue persists, please submit a bug report in the Issues section of this repository.

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

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
