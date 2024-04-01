"""CAPTCHA ME IF YOU CAN
Honestly this one was annoying much. You need to make sure to send the PHPSESSID cookie with the request
Also My preprocessing is not perfect so It takes multiple attempts to get the correct captcha
"""
import base64
from io import BytesIO
import unicodedata
import requests
import pytesseract
from bs4 import BeautifulSoup
from PIL import Image, ImageEnhance

URL = "http://challenge01.root-me.org/programmation/ch8/"
HEADERS = {
    "Cookie": "PHPSESSID=YOUR_PHPSESSID;"
}
while "flag" not in requests.get(URL, timeout=5, headers=HEADERS).text:
    response = requests.get(URL, timeout=5, headers=HEADERS)
    b64_img = BeautifulSoup(response.text, "html.parser").find("img")[
        "src"].split(",")[1]
    image_data = base64.b64decode(b64_img)
    image = Image.open(BytesIO(image_data))
    # Denoise
    pixel = image.load()
    for x in range(250):
        for y in range(50):
            if pixel[x, y] == (0, 0, 0):
                pixel[x, y] = (255, 255, 255)
    # Enhance image
    image = ImageEnhance.Contrast(image).enhance(2)
    image = ImageEnhance.Brightness(image).enhance(1.5)
    image = ImageEnhance.Sharpness(image).enhance(2)
    # Save image for testing purposes only
    # image.save("./Root-me/captcha.png")
    captcha = pytesseract.image_to_string(
        image, lang="eng", config='--psm 10 --oem 3')
    captcha = unicodedata.normalize("NFKD", captcha).strip()
    print("Captcha=", captcha)
    response = requests.post(
        URL, data={"cametu": captcha}, timeout=5, headers=HEADERS)
    response = BeautifulSoup(response.text, "html.parser").find("p")
    print("Server response:", response.text)
    if "flag" in response.text:
        print("Done!")
        break
