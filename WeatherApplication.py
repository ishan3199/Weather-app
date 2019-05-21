import tkinter as tk
import requests
root=tk.Tk()

canvas=tk.Canvas(root,height=500,width=600)
canvas.pack()
# key is '9b673552c67aff115c33e8a1bcfded21' must be passed to the server for accesing data
# api.openweathermap.org/data/2.5/weather?q={city name},{country code} is the query



background_image=tk.PhotoImage(file='weather.png')
background_label=tk.Label(root,image=background_image)
background_label.place(relheight=1,relwidth=1)
frame=tk.Frame(root,bg='#33FFDC',bd=4)  #frame is a sub element inside our canvas,
                                        # here 33FFDC represents colour shade of blue in hexadecimals
frame.place(relx=0.5,rely=0.1,relwidth=0.8,relheight=0.1,anchor='n')  #relx and rely will help in shifting reference
entry=tk.Entry(frame,font=('Courier',14))
entry.place(relwidth=0.6,relheight=1)
button=tk.Button(frame,font=('Courier',14),text='Enter City',command=lambda:get_weather(entry.get()))
  #lamba will make our o/p inline with i/p & entry.get passes the i/p from entry to argument of
  #getweather Fn
button.place(relx=0.65,relheight=1,relwidth=0.33)

frame2=tk.Frame(root,bg='#33FFDC',bd='7')
frame2.place(relx=0.5,rely=0.3,relwidth=0.8,relheight=0.6,anchor='n')
label=tk.Label(frame2,font=('courier',14))
label.place(relwidth=1,relheight=1)


def get_weather(city):
    weather_code = '9b673552c67aff115c33e8a1bcfded21'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    pars = {'appid': weather_code, 'q': city, 'units': 'Metric'}  #metric is celcius
    weather = requests.get(url, params=pars)  # requests will link our data to server
    response = weather.json()  # o/p will be recieved in json(list form)

    label['text'] = response_label(response)  #It will put the o/p of response_label Fn,
                                            #in the form of text in given label of frame 2;
                                        # lable already created at beginning and Fn at below



def response_label(response):          #this is Fn for getting output in label of lower frame2
    try:                               #Try will find the data in the server and if it is valid then executes try block

        x=response['name']
        y=response['weather'][0]['description']
        a=response['main']['temp']
        z=response['main']['temp_min']
        b=response['main']['temp_max']

        if a>30:     #simply if temp is > than 30 than sunny day
            out='Your City:%s\nCurrent Conditions:%s\nCurrent Temperature(Cel):%s\nMinimum Temp(cel):%s' \
            '\nMaximum Temp(cel):%s\n\n FORECAST:SUNNY DAY\n\n\nEnjoy the Weather & Have an eventful day\n\n' \
            'Weather Genie TM (ESTD 2019)\nServer Data: owm © 2019 ' %(x,y,a,z,b)
        else:
            out='Your City:%s\nCurrent Conditions:%s\nCurrent Temperature(Cel):%s\nMinimum Temp(cel):%s' \
            '\nMaximum Temp(cel):%s\n\n\n\n  Enjoy the Weather & Have an eventful day\n\n' \
            'Weather Genie TM (ESTD 2019)\nFounder:Ishan Patel\nServer Data: owm © 2019 ' %(x,y,a,z,b)
    except:                      # if Try is unable to retrieve data then,
                                 #Except executes except block
        out="ERROR 121:Sorry data not retrieved"

    return out


root.mainloop()   #tkinter window is ended with this command only





