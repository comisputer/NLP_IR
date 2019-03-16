
"""
name        : Jung In-seok
student ID  : 20131699
major       : Intergrative Engineering_Digital Imaging
date        : March 16, 2019 
"""

"""
Text Indexing Homework

1) Choose 10 movie scripts from https://www.imsdb.com/
(I suggest to make them in TXT files.)

2) Write a code for indexing the texts,
and draw charts for showing the word distributions of them. 

* You can use one of programming language (Python, Java, and C).
"""

"""
Reference :
[1] 어절단위로 끊어서 출력하기:
http://word.snu.ac.kr/wiki/doku.php?id=python:tutorial:learn_by_example:word_list

[2] 파이썬을 이용해 파일에서 단어 빈도 계산하기:
https://code.tutsplus.com/ko/tutorials/counting-word-frequency-in-a-file-using-python--cms-25965

[3] 파이썬 딕셔너리 정렬하기:
https://m.blog.naver.com/PostView.nhn?blogId=moonsoo5522&logNo=220826171626&proxyReferer=https%3A%2F%2Fwww.google.com%2F

[4] matplotlib 이용하여 그래프 그리기:
https://ordo.tistory.com/68
"""

import matplotlib.pyplot as plt
import operator
import re

movie_idx = 9
movie_list = ["BEAUTY AND THE BEAST",   \
              "COCO",                   \
              "FROZEN",                 \
              "GET OUT",                \
              "LA LA LAND",             \
              "MULAN",                  \
              "SHREK",                  \
              "THE AVENGERS",           \
              "THOR RAGNAROK",          \
              "WALL-E"]

filename = "data/" + movie_list[movie_idx] + ".txt"
file = open(filename, 'r')
 
index_list = []

# [1]
for line in file:
    for word in line.split():
        index_list.append(word)

# [2]
frequency = {}
for word in index_list:
    count = frequency.get(word, 0)
    frequency[word] = count + 1

#frequency_list = frequency.keys()
#for words in frequency_list:
#    print(words, frequency[words])

# [3]
sortedArr = sorted(frequency.items(), key=operator.itemgetter(1), reverse=True)
print(sortedArr)

# [4]
x = []
y = []
for arr in sortedArr:
    x.append(arr[0])
    y.append(arr[1])

plt.plot(x, y)
plt.xlabel('ID of terms')
plt.ylabel('frequency')

plt.title(movie_list[movie_idx])
plt.show()