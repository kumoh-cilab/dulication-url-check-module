from diskcache import Cache

cache = Cache()

cache['test'] = "hi"


print(cache.get("test"))