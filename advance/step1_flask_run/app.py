from flask import Flask, render_template, jsonify, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return "home page app"

