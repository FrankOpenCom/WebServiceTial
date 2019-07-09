# -*- coding: utf-8 -*-

from flask import Flask, request, redirect, url_for, send_from_directory, render_template
from os import path
import sqlite3
from sqlite3 import Error

### global definition for database file path
database_file_path = 'data.db'


### funtions for support Database operation insert, update and delete etc.
def create_connection(db_file):
    """ create a database connection to a SQLite database """
    try:
        conn = sqlite3.connect(db_file)
        conn.execute(
            'CREATE TABLE topics (id integer PRIMARY KEY, presenter TEXT, co_persenter TEXT, language TEXT, nitech TEXT, title TEXT, abstract TEST)')
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        conn.close()
        

def insert_topic(presenter, co_persenter, language, nitech, title, abstract):
    try:
        with sqlite3.connect(database_file_path) as con:
            cur = con.cursor()
            cur.execute("INSERT INTO topics(presenter, co_persenter, language, nitech, title, abstract) VALUES(?, ?, ?, ?, ?, ?)",
                        (presenter, co_persenter, language, nitech, title, abstract))

            con.commit()
        return True
    except Error as e:
        print(e)
        con.rollback()
        return False
    finally:
        con.close()

### for Flask part
app = Flask(__name__)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(path.join(app.root_path, 'static/images'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

    
if __name__ == '__main__':
   app.run()