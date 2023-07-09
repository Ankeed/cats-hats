import requests


api_key = 'BjaMFjK7uZhhRGstmJjnDlIklrklr3SH'
search_tag = input('Wat do you wanna get?\n> ')
gif_resp = requests.get(f'https://api.giphy.com/v1/gifs/search?api_key={api_key}&q={search_tag}&limit=10&offset=0&rating=g&lang=en&bundle=messaging_non_clips')
urls = gif_resp.json()

links=[]
for url in urls['data']:
    links.append(url['url'])

new_links = [item + '\n' for item in links]

path_str = "\\some_path\\"
with open(path_str + 'urls.txt', 'w') as file:
    file.writelines(new_links)