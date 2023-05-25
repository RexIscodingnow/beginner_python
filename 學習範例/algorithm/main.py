'''
演算法學習
            -- by 測試執行區

1. Divide and Conquer
'''

import numpy as np

from divide_and_conquer import Divide_and_Conquer


class HashTable:
    def __init__(self, size):
        self.size = size

    def _hash(self, value: str):
        hash_value = 0
        CONST_NUM = 3.1415926

        for char in value:
            hash_value += hash_value * CONST_NUM + ord(char)

        while len(str(int(hash_value))) != 10:
            if len(str(int(hash_value))) < 10:
                hash_value *= CONST_NUM
            else:
                hash_value *= 0.1

        hash_value = str(int(hash_value))
        return hash_value


    def insert(self, value: str):
        return self._hash(value)


if __name__ == "__main__":
    divide_and_conquer = Divide_and_Conquer()
    
    data = np.arange(1, 101, dtype=int)

    res = divide_and_conquer.binary_search(data, 1, 0, data.shape[0])
    print(res)

    data = np.random.randint(0, 100, size=10, dtype=int)
    data = divide_and_conquer.merge_sort(data)

    print(data)

    pass
