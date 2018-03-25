"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, request, Flask
from urllib.request import urlopen
from bs4 import BeautifulSoup
from Interactive import app
import urllib.parse
import datetime

@app.route('/keyboard')
def keyboard():
    return '{ "type" : "text" }'


@app.route('/message', methods = ['POST'])
def message():
    dataReceive = request.get_json()

    usrRequest = str(dataReceive['content'])

    cmd = usrRequest.split(" ", maxsplit = 1)

    if cmd[0] == "!!오류":
        try:
            now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            logMessage = "[" + now + "] " + str(cmd[1]) + "\n"
            print(logMessage)
            with open("errlog.log", "w") as log:
                log.write(logMessage)
            message = "오류가 제보 되었습니다. 감사합니다."

        except:
            message = "오ㄹ..ㅠ 제ㅔ.! 보ㅇㅔ'! 싪패 했ㅅ습니다.." #not mistake, intended to be seen glitch.
        #print(message)
        resultMessage = '{ "message" : { "text" : "%s" }}' % message
    elif cmd[0] == "창윤빈":
        message = "[명사] 세상에서 제일 멋있는 남자" 
    elif cmd[0] == "권용수":
        message = "[명사] 세상에서 제일 섹시한 남자"
    else:
        usrRequest = urllib.parse.quote(usrRequest)

        html = getHTML(usrRequest)
        print(usrRequest)
        message = parseWord(html)

    resultMessage = '{ "message" : { "text" : "%s" }}' % message

    return resultMessage

def parseWord(html):
    try:
        soup = BeautifulSoup(html, 'html.parser')

        kind = soup.find("span", {"class" : "fnt_k09"}).getText()
        mean = soup.find("span", {"class" : "fnt_k05"}).getText()


        if kind == "" or mean == "":
            result = "죄송합니다. 결과를 찾지 못했습니다."
        else:
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
