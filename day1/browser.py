import webbrowser

webbrowser.open("http://www.naver.com")

team = {"레알마드리드","바르셀로나","유벤투스"}

# https://search.naver.com/search.naver?query=

for i in team:
    url = "https://search.naver.com/search.naver?where=nexearch&query=" + i
    webbrowser.open(url)


# DRY / 간결하게 표현.!

url = "https://search.naver.com/search.naver?query="
webbrowser.open(url + "아이유")
webbrowser.open(url + "수지")
webbrowser.open(url + "설현")

# 더욱 더 간결하게

keywords = ["아이유", "수지", "설현"]

url = "https://search.naver.com/search.naver?query="

for name in keywords:
    webbrowser.open(url + name)
    
