import os
import sys
from pprint import pprint

from notion_client import Client


# Initialize the client
notion = Client(auth='secret_XsLZcIj2ZJqXyK0b35zhWyMzZn7OUgZOzWiULUBgSlu')



# Create a new page
your_name = input("\n\nEnter your name: ")
gh_uname = input("Enter your github username: ")
new_page = {
    "Name": {"title": [{"text": {"content": your_name}}]},
    "Tags": {"type": "multi_select", "multi_select": [{"name": "python"}]}
}
notion.pages.create(parent={"database_id": 'dc4633a949f546d1ab1e24d305343cbf'}, properties=new_page)
print("You were added to the People database!")

