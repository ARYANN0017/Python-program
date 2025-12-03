# import pyshorteners
#
# url = input("Enter the URL you wish to shorten: ")
# def shorten(url):
#     s = pyshorteners.Shortener()
#     print(s.tinyurl.short(url))
#
#
# shorten(url)


import pyshorteners

long_url = input("enter long url :-")

s = pyshorteners.Shortener()  #pyshortrner ek library chE jema function and tools use thi url short kare! & shortener ek service che

# Shorten the URL
short_url = s.tinyurl.short(long_url)  #tiny ekk service che use karin long k short kare short variable maH!

print(f"Original URL: {long_url}")
print(f"Shortened URL: {short_url}")
