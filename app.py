# Testing GitHub - rstanev@gmail.com
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import requests

from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def main():
  return redirect('/index')

@app.route('/index')
def index():
  return render_template('index.html')

if __name__ == '__main__':
  app.run(port=33507)
