
from typing import List

def rolling_average(data, window_size):
    return [sum(data[i:i+window_size]) / window_size for i in range(len(data) - window_size + 1)]
data = [1,2,3,4,5,6]
window_size = 3
result = rolling_average(data,window_size)
print(result)