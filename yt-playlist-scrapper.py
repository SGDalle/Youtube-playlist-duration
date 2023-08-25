from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
import datetime

#opening browser
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
#paste your playlist url here
url = ''

driver.get(url)

#getting the whole page size

last_height = driver.execute_script("return document.documentElement.scrollHeight")

while True:
  driver.execute_script("window.scrollTo(0, arguments[0]);", last_height)
  time.sleep(3)
  
  new_height = driver.execute_script("return document.documentElement.scrollHeight")
  if new_height == last_height:
     break
  last_height = new_height

#Scrolling the whole page slowly

initial_scroll = 0
max_scroll = 1000 - 400
while max_scroll < last_height:
   driver.execute_script("window.scrollTo(arguments[0], arguments[1]);", initial_scroll, max_scroll)
   initial_scroll = max_scroll
   max_scroll += 1000
   time.sleep(1)
   


#scrapping video duration

video_duration = driver.execute_script("return document.querySelectorAll('ytd-thumbnail a div ytd-thumbnail-overlay-time-status-renderer span#text.style-scope.ytd-thumbnail-overlay-time-status-renderer')")


duration_list = []

for e in video_duration:
    duration_list.append(e.text)

print(duration_list)


#sum of all videos duration
sum = datetime.timedelta()
for i in duration_list:
   collon = 0
   for j in i:
      if j ==":":
         collon +=1
   if collon >= 2:
      (h,m,s) = i.split(':')
      d = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
      sum += d
   elif collon == 1:
      (m,s) = i.split(':')
      d = datetime.timedelta(minutes=int(m), seconds=int(s))
      sum += d

print(str(sum))

