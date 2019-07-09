# -*- coding: utf-8 -*-

from flask import Flask, request, redirect, url_for
from os import path
import sqlite3
from sqlite3 import Error

database_file_path = 'data.db'

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


app = Flask(__name__)


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


@app.route('/')
def welcome():
    return app.send_static_file('welcome.html')


@app.route('/submit', methods=['GET', 'POST'])
def submisstion():
    if request.method == "GET":
        return app.send_static_file('submit_topic.html')
    else:
        if request.method == "POST":
            if insert_topic(request.form['Presenter'], request.form['Co-Presenter'], request.form['Language'], request.form['NITech'], request.form['Title'], request.form['Abstract']):
                return redirect(url_for('submit_done'))
            else:
                return redirect(url_for('submit_error'))


@app.route('/submit_done')
def submit_done():
    return app.send_static_file('submit_done.html')

@app.route('/submit_error')
def submit_error():
    return app.send_static_file('submit_error.html')


if __name__ == '__main__':
    if not path.isfile(database_file_path):
        print('create a empty database file\n')
        create_connection(database_file_path)
    app.run()
