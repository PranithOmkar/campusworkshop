"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chaacl3hp8u791gtfo7g-a.oregon-postgres.render.com",
        database="todo_vl0g",
        user="root",
        password="kYJruZ67TMBtjf8RnG5wTHA6uxXK6UxZ")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
