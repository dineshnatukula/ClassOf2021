# 1. web server under construction
# 2. other than get is invalid request response with error code
# 3. /index.html, match contents.
# 4. list of directory with files and folders. (html template for printing)
# 5. Handling threads

# 1. /scripts/file.py, check for the output
# 2. /file.py, other than scripts folder
# 3. /scripts/file.py, checking with the parameters in the uri
# 4. /scripts/file.py, infinite loop checking
# 5. Handling threads

# -*- coding: utf-8 -*-
"""Test_webserver.ipynb

Automatically generated by Colaboratory.

Original file is located at
https://colab.research.google.com/drive/1--N3SeVNrh6fSAK77MMzrbz-m-MQu6V3
@author Praveen Garimella
@author Laxmi Narayana Murthy
@author Deepak Kumar Reddy
@author Vipul
@author Siva Sankar
"""

# import statements here.
import requests

# update the values according to your ip and port number.
host = "127.0.0.1"
port = "8888"
url = "http://" + host + ":" + port + "/"
file_name = "index.html"
print (url)

# driver to run all testcases

def Testcase(r, expstatuscode, expcontenttype, exptext, count):
    print("-----TestCase-" , count, "-----")
    if r.status_code != expstatuscode:
        print (r.status_code, " :: " , expstatuscode)
        print("Wrong status code")
        return False
    if r.headers['Content-Type'] != expcontenttype:
        print("Wrong content-type")
        return False
    # print(r.text)

    if exptext != "" and r.text != exptext:
        print (exptext, r.text)
        print("Wrong content")
        return False
    return True

# Test case
# give your local host and port number here.

# Testcase 1: Checking whether your server is handling requests or not.
# if it handle requests, the default response should be 
# <h1>Webserver Under construction</h1>
# This response should only be sent when the variable 
#enable_directory_browsing is set to False
r = requests.get(url)
print()
# print(r.headers)
# print(r.status_code)
# print(r.text)
if Testcase(r, 200, "text/html", "<h1>Tiny Webserver Under construction</h1>", 1):
    print("TestCase-1 passed")
else:
    print("TestCase-1 Failed")

r = requests.get(url + file_name)
http_response = """<!DOCTYPE html>
<html>
<head>
	<title>test web page</title>
</head>
<body>
<h1>Test web page for testing the tiny web server</h1>
<img src="one.png">
<img src="po.gif">
<a href="second.html">let's see if the second page also works?</a>
</body>
</html>"""
if Testcase(r, 200, "text/html", http_response, 2):
    print("TestCase-2 passed")
else:
    print("TestCase-2 Failed")

r = requests.get(url + file_name + "l")
if Testcase(r, 404, "text/html", "<h1>File Not Found</h1>", 3):
    print("TestCase-3 passed")
else:
    print("TestCase-3 Failed")

r = requests.get(url + "one.png")
if Testcase(r, 200, "image/png", "", 4):
    print("TestCase-4 passed")
else:
    print("TestCase-4 Failed")

r = requests.get(url + "second.html")
http_response = """<!DOCTYPE html>
<html>
<head>
	<title>this is the second page</title>
</head>
<body>
<h1>Sweet! The second page works too.</h1>
</body>
</html>"""
if Testcase(r, 200, "text/html", http_response, 5):
    print("TestCase-5 passed")
else:
    print("TestCase-5 Failed")

r = requests.get(url + "po.gif")
if Testcase(r, 200, "image/gif", "", 6):
    print("TestCase-6 passed")
else:
    print("TestCase-6 Failed")


