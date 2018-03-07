from tkinter import *
from tkinter import ttk
from PIL import Image
import requests
from bs4 import BeautifulSoup

#############################################################
#현재 날씨 출력
url='http://www.weather.go.kr/weather/forecast/timeseries.jsp'
response = requests.get(url)
soup = BeautifulSoup (response.text, 'html.parser')

mylist=soup.select('dd.now_weather1_right')
mylist=str(mylist)
mylist=mylist.split(',')
templist=[]

for i in range(len(mylist)):
    templist.append(mylist[i][mylist[i].index('right')+7:])
for i in range(len(templist)):
    templist[i]=templist[i].replace('</dd>','')
templist[0]=templist[0][templist[0].index('>')+1:]
templist[3]=templist[3][:-1]

Current_temperature=templist[0]
Current_wind=templist[1]
Current_humidity=templist[2]
Current_precipitation=templist[3]

Current_weather='●현재 날씨●'
Current_temperature='   온도:   '+Current_temperature
Current_wind='   바람:   '+Current_wind
Current_humidity='   습도:   '+Current_humidity
Current_precipitation='강수량:   '+Current_precipitation


url='http://www.weather.go.kr/weather/forecast/timeseries.jsp'
response = requests.get(url)
soup = BeautifulSoup (response.text, 'html.parser')

mylist=soup.select('dd.now_weather1_left.icon')
mylist=str(mylist)
mylist=mylist.split(',')
mylist=mylist[0]
Weather_Description=mylist[mylist.index('alt="')+5:mylist.index('src')-16]

##############################################################

a=Tk()


#제목
label=ttk.Label(a,text="현재 서울 날씨를 알려드리겠습니다")
label.pack()
label.config(foreground='black',background='white')
label.config(font=('현대하모니 L',11,'bold'))


#이미지를 x, y좌표에 보여주기
lbl2=ttk.Label(a,text='image place')
lbl2.pack()
lbl2.config(justify=LEFT)
img=PhotoImage(file = 'C:/Users/Thomas/Desktop/Python/날씨 파일/맑음.gif')
img=img.subsample(2,2)
lbl2.img=img
lbl2.config(image=lbl2.img)
lbl2.config(justify=LEFT)
lbl2.place(x=10, y=75)
lbl2.configure(background='black')

#날씨 정보
Weather=ttk.Label(a,text=Current_weather)
Temperature=ttk.Label(a,text=Current_temperature)
Wind=ttk.Label(a,text=Current_wind)
Humidity=ttk.Label(a,text=Current_humidity)
Precipitation=ttk.Label(a,text=Current_precipitation)
Description=ttk.Label(a,text=Weather_Description)

#날씨 정보 위치
Weather.place(x=150,y=70)
Temperature.place(x=150,y=90)
Wind.place(x=150,y=110)
Humidity.place(x=150,y=130)
Precipitation.place(x=150,y=150)
Description.place(x=10,y=50)

#날씨 정보 백그라운드 색갈
Weather.configure(background='white')
Temperature.configure(background='white')
Wind.configure(background='white')
Humidity.configure(background='white')
Precipitation.configure(background='white')
Description.configure(background='white')
Description.config(font=('현대하모니 L',11,'bold'))
#현재 시간
import time as t
mytime=t.gmtime()
mytime=str(mytime).split()
for i in range(3):
    del mytime[-1]
for i in range(len(mytime)):
    mytime[i]=mytime[i][mytime[i].find('=')+1:]
    mytime[i]=mytime[i][:mytime[i].index(',')]
Now=mytime[0]+'/'+mytime[1]+'/'+mytime[2]+' '+mytime[3]+'시 '+mytime[4]+'분 '+mytime[5]+'초'
Now=ttk.Label(a,text='※ '+Now+' 기준') #현재 시간 정보
Now.place(x=90,y=20) #위치
Now.configure(background='white') #백그라운드 색갈


#확인 버튼
def close_window(): 
    a.destroy()  #닫기

btn=Button(a,text="확인",command=close_window,width=12)
btn.place(x=160,y=180)


a.title('서울 날씨')
a.geometry('280x220+600+350')
a.configure(background='white')
a.mainloop()