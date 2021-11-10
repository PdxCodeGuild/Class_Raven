'''Give hyperlink notifications with news'''



import requests
import webbrowser
from win10toast_click import ToastNotifier
import time

news_options = {
    '1': 'science',
    '2': 'business',
    '3': 'entertainment',
    '4': 'general',
    '5': 'health',
    '6': 'sports',
    '7': 'technology'
}

print('Get news notifications')

for label, option in news_options.items():
    print(f'\n{label}. {option}')

user_news = input('\nEnter the number of the topic you want\n\n>> ')

user_news = news_options.get(user_news)


response = requests.get(f'https://newsapi.org/v2/top-headlines?country=us&category={user_news}&apiKey=a93c9503b41e4190bcd984283be48d78')
data = response.json()['articles']



x = 1 
i = 0  
while x < 2:    
    name = (data[i]['source']['name'])
    author = (data[i]['author'])
    title = (data[i]['title'])
    url = (data[i]['url'])

    #print(url)





    def open_url():
        try:
            webbrowser.open_new(url)
            print('Opening URL...')
        except:
            print('Failed to open URL. Unsupported variable type.')

    toaster = ToastNotifier()

    toaster.show_toast(
        (data[i]['title']), #headline of the news article
        (data[i]['source']['name']), #name of the creator
        icon_path=None,
        duration=5,
        threaded=True,
        callback_on_click=open_url
    )
    time.sleep(5)
    i += 1
    x += 1


#add capability of user to enter the news they want to see.










