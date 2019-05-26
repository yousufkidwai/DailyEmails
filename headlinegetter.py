import requests, json


def get_choice():
    print("Please input the area of headlines you would like to receive")
    print("The choices are business, entertainment, health, science, sports, and technology")
    choice = input("> ")
    return choice


def get_headlines(choice):
    main_url = f"https://newsapi.org/v2/top-headlines?country=us&category={choice}&apiKey=4dbc17e007ab436fb66416009dfb59a8"
    open_bbc_page = requests.get(main_url).json()
    article = open_bbc_page["articles"]
    results = ['<b>']
    for ar in article:
        if len(results) > 18:
            break
        results.append('    ')
        results.append(ar["title"])
        results.append('<br>')
        results.append('<br>')
    results.append('</b>')
    results_str = ''.join(results)
    return results_str

