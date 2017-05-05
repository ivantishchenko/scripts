#!/usr/bin/python3
import urllib.request as urllib
import re
from io import BytesIO
from bs4 import BeautifulSoup
from PIL import Image
import requests  
"""
VPN gate for getting a URL, a cookie and a pass image
"""
class Gate:
    original_URL = "https://www.freeopenvpn.org/logpass/"
    URL = original_URL + "germany.php"
    pattern = "<img(.*)germany(.*)>"
    result_image = "germany.png"
    credentials = "login.conf"

    """
    Get a url from where to download a picture
    """
    def getUrl(self):
        print("VPN Helper")
        # fetch and scrapple tag
        html = urllib.urlopen(self.URL).read().decode('utf-8')
        res_tag = re.search(self.pattern, html)

        print("Fetched tag is: " + res_tag.group())
        #parse tag
        soup = BeautifulSoup(res_tag.group(), 'html.parser')
        res_url = soup.find('img')['src']

        print("Image URL is: " + res_url)
        print("Fetching from: " + self.original_URL + res_url)
        return self.original_URL + res_url

    """
    Get a cookie needed for a picture
    """
    def getCookie(self, res_url):
        #get cookie
        cookie = re.search("\?(.*)$", res_url).group().replace("?", "")
        print("Cookie: " + cookie)
        #cookie = res_url[13:]
        #print("Cookie: " + cookie)
        return cookie

    """
    save image on disk
    """
    def saveImage(self):
        url = self.getUrl()
        cookie = self.getCookie(url)
        #save image
        opener = urllib.build_opener()
        opener.addheaders.append(('Cookie', 'par=' + cookie))
        f = open(self.result_image,'wb')
        f.write(opener.open(url).read())
        f.close()
        return f
    """
    Display a saved image
    """
    def displayImage(self):
        self.saveImage()
        image = Image.open(self.result_image)
        image.show()

    """
    create login file for OpenVPN
    """
    def createLoginFile(self):
        f = open(self.credentials, 'w')
        f.write("freeopenvpn\n")
        password = input("Please enter the password from an iamge: ")
        f.write(password)


myGate = Gate()
myGate.displayImage()
myGate.createLoginFile()