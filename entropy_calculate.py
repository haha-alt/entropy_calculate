#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import os
import numpy as np
import re
exec_path = sys.path[0]
os.chdir(exec_path)
daily_path = input("corpus_filename:\n>>> ")
result_count_path = input("output_count_filename:\n>>> ")
result_freq_path = input("output_freq_filename:\n>>> ")

total_nb_word = 0
word_count_dict = {}

with open(daily_path,"r",True,encoding='utf-8') as fr:
    for line in fr:
        line = line.strip().replace(' ', '')
        line = line.replace('\u3000', '')
        line = re.sub("\W+", "", line)
        total_nb_word += len(line)
        for x in range(0,len(line)):
            if line[x] not in word_count_dict:
                word_count_dict[line[x]] = 0
            word_count_dict[line[x]] += 1

with open(result_count_path, 'w') as fw:
    fw.write('{}\n'.format(total_nb_word))
    for word, count in word_count_dict.items():
        fw.write('{} ||| {}\n'.format(word, count))

word_freq_dict = {}
H = 0
for word in word_count_dict:
    if word not in word_freq_dict.keys():
        word_freq_dict[word] = np.around((word_count_dict[word] / total_nb_word),decimals=5)
        H += -word_freq_dict[word] * np.log2(word_freq_dict[word])
    
    
with open(result_freq_path,'w') as fc:
    fc.write('{}\n'.format(total_nb_word))
    for word, freq in word_freq_dict.items():
        fc.write('{} ||| {}\n'.format(word,freq))
    total_nb_word,word_freq_dict
    fc.write('{}\n'.format(H))