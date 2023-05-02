"""
vscode-extension-details-extractor
=================================

A Python script that extracts the short description of one or more Visual Studio Code extensions.

This script uses the Visual Studio Marketplace API to retrieve the details of one or more extensions and extract their short descriptions. The short descriptions are then printed to the console.

Usage:
    vscode-extension-details-extractor <extension_id>...
"""
import argparse
import requests
from bs4 import BeautifulSoup


class Extension():
    """
    A class representing a Visual Studio Code extension.

    Attributes:
    - extension_id (str): the ID of the extension
    - url (str): the URL of the extension's marketplace page
    - details (str): the details of the extension
    - name (str): the name of the extension
    - second_row_wrapper (str): the second row wrapper of the extension
    - publisher (str): the publisher of the extension
    - publisher_link (str): the publisher link of the extension
    - rating (str): the rating of the extension
    - review_rating_wrapper (str): the review rating wrapper of the extension
    - review_rating (str): the review rating of the extension
    - rating_control (str): the rating control of the extension
    - rating_count (str): the rating count of the extension
    - short_desc (str): the short description of the extension
    - action (str): the action of the extension
    """

    def __init__(self, extension_id, details=None, name=None, second_row_wrapper=None, publisher=None, publisher_link=None, rating=None, review_rating_wrapper=None, review_rating=None, rating_control=None, rating_count=None, short_desc=None, action=None):
        self.extension_id = extension_id
        self.url = f"https://marketplace.visualstudio.com/items?itemName={extension_id}"
        self.details = details
        self.name = name
        self.second_row_wrapper = second_row_wrapper
        self.publisher = publisher
        self.publisher_link = publisher_link
        self.rating = rating
        self.review_rating_wrapper = review_rating_wrapper
        self.review_rating = review_rating
        self.rating_control = rating_control
        self.rating_count = rating_count
        self.short_desc = short_desc
        self.action = action


def main():
    """
    The main function of the script.
    """
    # A dictionary mapping property names to their corresponding CSS class names
    property_to_class_map = {
        "details": "ux-item-details",
        "name": "ux-item-name",
        "second_row_wrapper": "ux-item-second-row-wrapper",
        "publisher": "ux-item-publisher",
        "publisher_link": "ux-item-publisher-link",
        "rating": "ux-item-rating",
        "review_rating_wrapper": "ux-item-review-rating-wrapper",
        "review_rating": "ux-item-review-rating",
        "rating_control": "ux-item-rating-control",
        "rating_count": "ux-item-rating-count",
        "short_desc": "ux-item-shortdesc",
        "action": "ux-item-action"
    }

    # Parse command line arguments
    parser = argparse.ArgumentParser(
        description='Extract short description of VSCode extensions.')
    parser.add_argument('extension_ids', metavar='EXTENSION_ID', type=str, nargs='+',
                        help='one or more VSCode extension IDs')
    args = parser.parse_args()

    extensions = []

    # Loop through each extension ID and extract its details
    for extension_id in args.extension_ids:
        url = f"https://marketplace.visualstudio.com/items?itemName={extension_id}"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        extension = Extension(extension_id)

        # Loop through each property and extract its value from the HTML
        for prop, class_name in property_to_class_map.items():
            value = soup.select_one(f".{class_name}").text.strip()
            setattr(extension, prop, value)

        extensions.append(extension)

        # Print the short description of the extension
        print(f"{extension_id}: {extension.short_desc}")


if __name__ == "__main__":
    main()
