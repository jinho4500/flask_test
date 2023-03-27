# 사용자가 정의한(커스텀)
from flask import Flask, render_template, jsonify, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return "home page 커스텀"

