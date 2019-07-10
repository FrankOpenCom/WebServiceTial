# -*- coding: utf-8 -*-

from flask import Flask, request, redirect, url_for, send_from_directory, render_template, jsonify
from os import path
import sqlite3
from sqlite3 import Error
from waitress import serve
import sys
import traceback

### global definition for database file path
database_file_path = 'data.db'


class InvalidUsage(Exception):
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv


### funtions for support Database operation insert, update and delete etc.
def create_connection(db_file):
    """ create a database connection to a SQLite database """
    try:
        conn = sqlite3.connect(db_file)
        conn.execute(
            'CREATE TABLE topics (id integer PRIMARY KEY, presenter TEXT, co_persenter TEXT, language TEXT, nitech TEXT, title TEXT, abstract TEST)')
    finally:
        conn.close()
        

def insert_topic(presenter, co_persenter, language, nitech, title, abstract):
    try:
        with sqlite3.connect(database_file_path) as con:
            cur = con.cursor()
            cur.execute("INSERT INTO topics(presenter, co_persenter, language, nitech, title, abstract) VALUES(?, ?, ?, ?, ?, ?)",
                        (presenter, co_persenter, language, nitech, title, abstract))

            con.commit()
    except Error as e:
        con.rollback()
    finally:
        con.close()


def get_topics():
    try:
        with sqlite3.connect(database_file_path) as con:
            con.row_factory = sqlite3.Row
            cur = con.cursor()
            cur.execute("select * from topics")
            rows = cur.fetchall()
            return rows
    finally:
        con.close()

### for Flask part
app = Flask(__name__)


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(path.join(app.root_path, 'static/images'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


@app.route('/topic/<int:id>')
def topic(id):
    return


@app.route('/')
def root():
    try:
        rows = get_topics()
        return render_template("topics_view.html",rows = rows)    
    except:
        raise InvalidUsage(traceback.format_exc(), status_code=410)



if __name__ == '__main__':
   app.run()
   ### serve(app, host='0.0.0.0', port=8000)