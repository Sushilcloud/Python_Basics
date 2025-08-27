# https://www.youtube.com/watch?v=wJXZq7ZO4sQ
import span
from selenium import webdriver

driver=webdriver.Chrome()

# url whatsapp
driver.get("https://web.whatsapp.com/")
driver.maximize_window()

name=input("Enter name or group name")
msg=input("Enter message")
count=int(input("Enter count"))

input("enter anything after scan qr code")

