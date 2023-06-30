from urlcreator import UrlCreator

MEMORY_1GB = 1073741824
MEMORY_1MB =  1000000
url_list = ["https://www.google.com", "https://www.bing.com",
 "https://www.facebook.com", "https://www.instagram.com",
 "https://www.twitter.com", "https://www.youtube.com", "https://www.netflix.com",
            "https://www.bbc.com/news", "https://www.cnn.com", "https://www.nytimes.com"]

creator = UrlCreator(MEMORY_1MB * 50, url_list)


len, result = creator.createUrl(1000)

print("end")