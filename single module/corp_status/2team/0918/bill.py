# -*- coding: utf-8 -*-
from urllib.parse import DefragResult
from flask import Flask, render_template, request,redirect, url_for, flash,jsonify, send_file, session,escape
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import and_,text,update
import json
from datetime import datetime
from sqlalchemy import func
from sqlalchemy.sql.elements import Null
from werkzeug.utils import secure_filename
import os, sys, re
import random, string
import pymysql
import sqlalchemy 
from itertools import groupby


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
import time
import os
from urllib.request import urlretrieve

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

app = Flask(__name__)
app.secret_key = "Secret Keyf"
# 이곳에서 db 연결
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ErpTax.db'


@app.route("/")
def index():
    return render_template("bill.html")

if __name__=="__main__":
    app.run(host='Localhost', port=5000)