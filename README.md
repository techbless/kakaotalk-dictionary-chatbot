# interactive_dictionary_onkakaotalk_pf

**Interactive dictionary on Kakaotalk plus friend**

[![Travis](https://img.shields.io/badge/<build>-<unkown>-<lightgrey>.svg)]()

This is a code for kakao plusfriend auto respond server.

[Author]

    Chris Yunbin Chang

    
[How to Use]

    1. copy this code to your web server directory.
    2. check your web server running well
    3. go to https://center-pf.kakao.com/ to depoly your server to kakao api management.
    4. enter your server url and click 'API TEST'.
    5. Well Done!
         
    
    
[How it works]

    When User request a korean for english word to server.
    1. search a word at naver dictionary and parse a result.
	2. revise a result for user to read more efficiently
	3. send a JSON data containing a result.


[Parsing]
	
	this source code parse some dictionary data from naver search result.
	This use PHP Simple HTML DOM Parser.
        
[If it doesn't work]

    Naver corp may change a html code that we are using for parsing.
	feel free to change a code and commit and request a pull.
	I will accept your pull request.