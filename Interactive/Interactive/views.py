"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, request, Flask
from urllib.request import urlopen
from bs4 import BeautifulSoup
from Interactive import app

@app.route('/keyboard')
def keyboard():
    return '{ "type" : "text" }'


@app.route('/message', methods = ['POST'])
def message():
    dataReceive = request.get_json()

    usrRequest = str(dataReceive['content'])
    usrRequest = usrRequest.replace(" ", "%20")

    html = getHTML(usrRequest)

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
        url = u"http://endic.naver.com/search.nhn?sLn=kr&isOnlyViewEE=N&query=" + wtsearch
        html = urlopen(url)
    except:
        html = ""
    return html