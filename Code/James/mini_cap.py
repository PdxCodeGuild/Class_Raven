'''Give notifications when new sciency (nvidia) stuff comes out'''

from notifypy import Notify

import requests

import webbrowser
from win10toast_click import ToastNotifier




response = requests.get('https://newsapi.org/v2/top-headlines?country=us&category=science&apiKey=a93c9503b41e4190bcd984283be48d78')
data = response.json()['articles']
#json.loads(data)
#print(data[0]['title'])
name = (data[0]['source']['name'])
author = (data[0]['author'])
title = (data[0]['title'])
description = (data[0]['description'])
#content = (data[0]['content'])
url = (data[0]['url'])
#print(url)

dictonary = {
    'name':name,
    'author':author,
    'title':title,
    'description':description,
    'url':url,
    #'content':2
}



def open_url():
    try:
        webbrowser.open_new(url)
        print('Opening URL...')
    except:
        print('Failed to open URL. Unsupported variable type.')

toaster = ToastNotifier()

toaster.show_toast(
    (data[0]['title']),
    (data[0]['source']['name']),
    icon_path=None,
    duration=5,
    threaded=True,
    callback_on_click=open_url
)




# notification = Notify()
# notification.title = title
# notification.message = url
# notification.send()





