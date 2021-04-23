from selenium import webdriver
from selenium.webdriver.chrome.options import Options

DRIVER_PATH = "C:\\Users\\aitha\\Downloads\\chromedriver_win32\\chromedriver.exe"
options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")

driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
driver.get("https://www.kmjmatrimony.com/index.php")
# print(driver.page_source)
file = open("sample.html", "w",encoding="utf-8")
file.write(driver.page_source)
driver.quit()