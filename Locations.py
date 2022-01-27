import urllib.request, urllib.parse, urllib.error
import json
import ssl
import webbrowser

api_key = 42
serviceurl = 'http://py4e-data.dr-chuck.net/json?'

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('\n'+'Enter location: ')
    typeofbusiness = input('\n'+'Provide the type of business to search: ')
    if len(address) < 1: break
