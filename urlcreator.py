import sys
import random
from random_word import RandomWords
# url_creator 클래스는 max memory size를 지정해 그만큼의 URL을 생성할 수 있음.

r= RandomWords()
class UrlCreator:
    def __init__(self, maximum_memory_size, uri_list):
        self.__uri_list = uri_list
        self.__uri_idx_list = [0 for _ in range(len(self.__uri_list))]
        self.__maximum_memory_size = maximum_memory_size


    # 최대 메모리를 넘지 않는 선에서 url을 생성
    def createUrl(self, max_size):
        result_list = []
        result_list_len = 0

        str_memory_size = 0
        list_memory_size = 0
        uri_list_len = len(self.__uri_list)

        while(str_memory_size + list_memory_size < self.__maximum_memory_size and result_list_len < max_size):
            idx = random.randint(0, uri_list_len-1)
            new_url = self.__uri_list[idx] + "/" + r.get_random_word() + "/" + str(self.__uri_idx_list[idx])
            self.__uri_idx_list[idx] += 1

            result_list.append(new_url)
            result_list_len += 1

            list_memory_size = sys.getsizeof(list_memory_size)
            str_memory_size += sys.getsizeof(new_url)

        return result_list_len, result_list


