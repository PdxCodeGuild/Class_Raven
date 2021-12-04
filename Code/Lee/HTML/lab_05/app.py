from flask import Flask, render_template, request, redirect, url_for
import json

from flask.json import load
app = Flask(__name__)