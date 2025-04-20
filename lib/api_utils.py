import os

import requests
import yaml


def get_books_from_api():
    """Fetch books from API using the URL from config.yaml"""
    config_path = os.path.join("config", "config.yaml")

    # Load the configuration from the YAML file
    with open(config_path) as file:
        config = yaml.safe_load(file)

    api_url = config["base_url"] + "/BookStore/v1/Books"  # Using base_url from the config

    response = requests.get(api_url)
    if response.status_code == 200:
        return [book["title"] for book in response.json()["books"]]
    else:
        raise Exception(f"Failed to fetch books from API. Status code: {response.status_code}")
