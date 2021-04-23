from selenium import webdriver
import urllib.request
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from PIL import Image as imagesize
import os
from selenium.webdriver.chrome.options import Options
from PyPDF2 import PdfFileMerger, PdfFileReader

DRIVER_PATH = "C:\\Users\\aitha\\Downloads\\chromedriver_win32\\chromedriver.exe"
options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")
driver = webdriver.Chrome(options=options,executable_path=DRIVER_PATH)
driver.get("https://www.kmjmatrimony.com/index.php")

submit = driver.find_element_by_class_name("close").click()

login = driver.find_element_by_id("textemail").send_keys("madhura.rajaram@gmail.com")
pwd = driver.find_element_by_id(" textpasswd").send_keys("553215")
buts = driver.find_element_by_xpath("//button[@type='submit']").click()

driver.get("https://www.kmjmatrimony.com/searchid.php")
gid = driver.find_element_by_id("txtid").send_keys("610")
hvn = driver.find_element_by_xpath("//button[@type='submit']").click()

img1 = driver.find_element_by_xpath("//div[@class='row col-4 divpictureblock ml-1']/img")
src = img1.get_attribute('src')
urllib.request.urlretrieve(src, "girl1.png")

det1 = driver.find_elements_by_xpath("//div[@id='divscroll']/div/p")

Story=[]
filename='nameNotFound'
styles=getSampleStyleSheet()
for idx,i in enumerate(det1):
    if idx==1:
        filename = i.text.split(":")
    Story.append(Paragraph(i.text, styles["Normal"]))

bro = driver.find_element_by_xpath("//button[@class='btn btn-danger btnadditionalinfo form-contol']").click()
img2 = driver.find_element_by_xpath("//p[@class='anotherpic m-0 text-center']/img")
src = img2.get_attribute('src')
urllib.request.urlretrieve(src, "girl2.png")

det2 = driver.find_element_by_xpath("//div[@class='jconfirm-content']")
for i in det2.text.split("\n"):
    Story.append(Paragraph(i, styles["Normal"]))

logo = "girl1.png"
width, height = imagesize.open(logo).size
ratio = width/height
width = height = min(400,max(width,height))
if ratio<1:
    width = height * ratio
else:
    height = width * ratio

im = Image(logo, (width/96)*inch, (height/96)*inch)
Story.append(im)

logo = "girl2.png"
width, height = imagesize.open(logo).size
ratio = width/height
width = height = min(400,max(width,height))
if ratio<1:
    width = height * ratio
else:
    height = width * ratio
im = Image(logo, (width/96)*inch, (height/96)*inch)
Story.append(im)

src = driver.find_element_by_xpath("//p[@class='horoscope m-0']/a").get_attribute('href')
dum = src.split('.')
ext =dum[len(dum)-1]

urllib.request.urlretrieve(src, "hor."+ext)
if ext=='pdf':
    doc = SimpleDocTemplate(filename[1]+".pdf",pagesize=letter,
                        rightMargin=72,leftMargin=72,
                        topMargin=72,bottomMargin=18)
    doc.build(Story)
    mergedObject = PdfFileMerger()
    mergedObject.append(PdfFileReader(filename[1]+'.pdf', 'rb'))
    mergedObject.append(PdfFileReader('hor.pdf', 'rb'))
    mergedObject.write(filename[1]+".pdf")
else:
    logo = 'hor.'+ext
    width, height = imagesize.open(logo).size
    ratio = width/height
    width = height = min(400,max(width,height))
    if ratio<1:
        width = height * ratio
    else:
        height = width * ratio
    im = Image(logo, (width/96)*inch, (height/96)*inch)
    Story.append(im)
    doc = SimpleDocTemplate(filename[1]+".pdf",pagesize=letter,
                            rightMargin=72,leftMargin=72,
                            topMargin=72,bottomMargin=18)
    doc.build(Story)
    os.remove('hor.'+ext)
    os.remove('girl1.png')
    os.remove('girl2.png')