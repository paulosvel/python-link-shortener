import pyshorteners
link = input("Enter the link you want to shorten: ")
shortener =  pyshorteners.Shortener()
shortlink = shortener.tinyurl.short(link)
print(shortlink)