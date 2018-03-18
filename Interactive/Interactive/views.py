"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, request, Flask
from urllib.request import urlopen
from bs4 import BeautifulSoup
from Interactive import app
import urllib.parse

@app.route('/keyboard')
def keyboard():
    return '{ "type" : "text" }'


@app.route('/message', methods = ['POST'])
def message():
    dataReceive = request.get_json()

    usrRequest = str(dataReceive['content'])

    realRequest = ""
    for x in usrRequest.split(' '):
        realRequest += urllib.parse.quote_plus(x)
        realRequest += "%20"
    realRequest = realRequest[:-3]

    html = getHTML(realRequest)
    print(realRequest)
    message = parseWord(html)

    resultMessage = '{ "message" : { "text" : "%s" }}' % message
    return resultMessage

def parseWord(html):
    try:
        soup = BeautifulSoup(html, 'html.parser')

        kind = soup.find("span", {"class" : "fnt_k09"}).getText()
        mean = soup.find("span", {"class" : "fnt_k05"}).getText()

        result = kind + " : " + mean
    except:
        result = "죄송합니다. 결과를 찾지 못했습니다."
    

    return result

def getHTML(wtsearch):
    try:
        url = "http://endic.naver.com/search.nhn?sLn=kr&isOnlyViewEE=N&query=" + wtsearch
        html = urlopen(url)
    except:
        html = ""
    return html