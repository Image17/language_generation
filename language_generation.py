# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 17:49:55 2018

@author: Image17
"""
#break out sentence starters and enders on gram[0] and gram[len(gram)-1]
#use those to start off and use matching grams
import csv
from nltk import ngrams
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from collections import Counter
import re
import random

def counts():
    s=''
    with open('hotel-reviews.csv', newline='', encoding='UTF-8-sig') as data:
        reader = csv.reader(data, delimiter=',')
        for row in reader:
            #sent tok then iter thru and add sentence start and end symbol
            sent = sent_tokenize(row[1])
            sent = [' <S>'+i+'</S> ' for i in sent]
            for i in sent:
                s+=i
    v = len(set(s))
    vocab = word_tokenize(s)
    print(len(s))
    print('vocabulary size ' ,len(vocab))
    print('set size ', len(set(vocab)))
    unigrams = ngrams(s.split(),1)
    bigrams = ngrams(s.split(),2)
    trigrams = ngrams(s.split(),3)
    unigram_freq = Counter(unigrams)
    bigram_freq = Counter(bigrams)
    trigram_freq = Counter(trigrams)
    unigram_prob={}
    bigram_prob={}
    trigram_prob={}
    start_words=[]
    stop_words={}
    mid_pos = []
    stop_pos = []
    rv=[]
    for gram in unigram_freq:
        unigram_prob[gram] = unigram_freq[gram] / v         
    for gram in bigram_freq:
        bigram_prob[gram] = bigram_freq[gram] / unigram_freq[gram[:-1]] 
    for gram in trigram_freq:
        trigram_prob[gram]  = trigram_freq[gram] / bigram_freq[gram[:-1]]

    for gram in unigram_freq:
        if re.match(r'<S>.*', gram[0]):
            start_words.append(gram)
    for gram in bigram_prob:
        if re.match(r'.+</S>', gram[1]):
            stop_words[gram] = bigram_prob[gram]    
    
    uni_ord = dict((v,k) for k,v in unigram_freq.items())
    uni_rv = sorted(uni_ord)[-15:]
    uni_rv.reverse()
    print('Top unigrams!')
    for i in uni_rv:
        print(uni_ord[i])
    print('Top bigrams!')
    bi_ord = dict((v,k) for k,v in bigram_freq.items())
    bi_rv = sorted(bi_ord)[-15:]
    bi_rv.reverse()
    for i in bi_rv:
        print(bi_ord[i])
    print('Top trigrams!')
    tri_ord = dict((v,k) for k,v in trigram_freq.items())
    tri_rv = sorted(tri_ord)[-15:]
    tri_rv.reverse()
    for i in tri_rv:
        print(tri_ord[i])

def run_bigrams():
    s=''
    with open('hotel-reviews.csv', newline='', encoding='UTF-8-sig') as data:

        
        reader = csv.reader(data, delimiter=',')
        for row in reader:
            #sent tok then iter thru and add sentence start and end symbol
            sent = sent_tokenize(row[1])
            sent = [' <S>'+i+'</S> ' for i in sent]
            for i in sent:
                s+=i
    v = len(set(s))
    print(len(s))
    print(v)
    unigrams = ngrams(s.split(),1)
    bigrams = ngrams(s.split(),2)
    trigrams = ngrams(s.split(),3)
    unigram_freq = Counter(unigrams)
    bigram_freq = Counter(bigrams)
    trigram_freq = Counter(trigrams)
    unigram_prob={}
    bigram_prob={}
    trigram_prob={}
    start_words=[]
    stop_words={}
    mid_pos = []
    stop_pos = []
    rv=[]
    for gram in unigram_freq:
        unigram_prob[gram] = unigram_freq[gram] / v         
    for gram in bigram_freq:
        bigram_prob[gram] = bigram_freq[gram] / unigram_freq[gram[:-1]] 

    for gram in unigram_freq:
        if re.match(r'<S>.*', gram[0]):
            start_words.append(gram)
    for gram in bigram_prob:
        if re.match(r'.+</S>', gram[1]):
            stop_words[gram] = bigram_prob[gram]
    #Find best word to follow hard coded start word
    max=0
    best_gram=()
    for gram in bigram_prob:
        if start_words[56][0] == gram[0] and bigram_prob[gram] > max:
            max = bigram_prob[gram] 
            best_gram = gram

    rv = list(best_gram)
    
    #Find an additional 6 words
    for i in range (0, 7):
        max=0
        best_gram=()
        for gram in bigram_prob:
            if rv[-2:] == list(gram[:-1]) and bigram_prob[gram] > max:
                if random.randint(0,1) % 2 is 0:
                    best_gram = gram
                    max = bigram_prob[gram] 
                mid_pos.append(gram)
        if best_gram is ():
            if not mid_pos:
                best_gram = random.choice(list(bigram_prob))#move to trigrams
            else:
                best_gram = random.choice(list(mid_pos))
        rv.append(best_gram[-1])
    
    #Find an appropriate ending word
    max=0
    best_gram=()
    for gram in stop_words:
            if rv[-2:] == list(gram[:-1]) and stop_words[gram] > max:
                if random.randint(0,1) % 2 is 0:
                    max = bigram_prob[gram] 
                    best_gram = gram
                stop_pos.append(gram)
    if best_gram is ():
        if not stop_pos:
            best_gram = random.choice(list(stop_words))
        else:
            best_gram = random.choice(list(stop_pos))
    rv.append(best_gram[-1])
    
    print(len(bigram_prob))
    print(' '.join(rv))


def run_trigrams():
    s=''
    with open('hotel-reviews.csv', newline='', encoding='UTF-8-sig') as data:

        
        reader = csv.reader(data, delimiter=',')
        for row in reader:
            #sent tok then iter thru and add sentence start and end symbol
            sent = sent_tokenize(row[1])
            sent = [' <S>'+i+'</S> ' for i in sent]
            for i in sent:
                s+=i
    v = len(set(s))
    print(len(s))
    print(v)
    unigrams = ngrams(s.split(),1)
    bigrams = ngrams(s.split(),2)
    trigrams = ngrams(s.split(),3)
    unigram_freq = Counter(unigrams)
    bigram_freq = Counter(bigrams)
    trigram_freq = Counter(trigrams)
    unigram_prob={}
    bigram_prob={}
    trigram_prob={}
    start_words=[]
    stop_words={}
    mid_pos = []
    stop_pos = []
    rv=[]
    for gram in unigram_freq:
        unigram_prob[gram] = unigram_freq[gram] / v         
    for gram in bigram_freq:
        bigram_prob[gram] = bigram_freq[gram] / unigram_freq[gram[:-1]] 
    for gram in trigram_freq:
        trigram_prob[gram]  = trigram_freq[gram] / bigram_freq[gram[:-1]]

    for gram in unigram_freq:
        if re.match(r'<S>.*', gram[0]):
            start_words.append(gram)
    for gram in trigram_prob:
        if re.match(r'.+</S>', gram[-1]):
            stop_words[gram] = trigram_prob[gram]
    #Find best word to follow hard coded start word
    max=0
    best_gram=()
    for gram in trigram_prob:
        if start_words[13][0] == gram[0] and trigram_prob[gram] > max:
            max = trigram_prob[gram] 
            best_gram = gram

    rv = list(best_gram)
    #Find an additional 6 words
    for i in range (0, 6):
        max=0
        best_gram=()
        for gram in trigram_prob:
            if rv[-2:] == list(gram[:-1]) and trigram_prob[gram] > max:
                if random.randint(0,1) % 2 is 0:
                    max = trigram_prob[gram] 
                    best_gram = gram
                mid_pos.append(gram)
        if best_gram is ():
            if not mid_pos:
                best_gram = random.choice(list(trigram_prob))
            else:
                best_gram = random.choice(list(mid_pos))    
            
        rv.append(best_gram[-1])
    #Find an appropriate ending word
    max=0
    best_gram=()
    for gram in stop_words:
            if rv[-2:] == list(gram[:-1]) and stop_words[gram] > max:
                if random.randint(0,1) % 2 is 0:
                    max = trigram_prob[gram] 
                    best_gram = gram
                stop_pos.append(gram)
    if best_gram is ():
        print('no suitable ending, lets pick a random one')
        best_gram = random.choice(list(stop_words))
    rv.append(best_gram[-1])
    
    print(len(trigram_prob))
    print(' '.join(rv))     
    
def run_unigrams():
    s=''
    with open('hotel-reviews.csv', newline='', encoding='UTF-8-sig') as data:

        
        reader = csv.reader(data, delimiter=',')
        for row in reader:
            #sent tok then iter thru and add sentence start and end symbol
            sent = sent_tokenize(row[1])
            sent = [' <S>'+i+'</S> ' for i in sent]
            for i in sent:
                s+=i
    v = len(set(s))
    print(len(s))
    print(v)
    unigrams = ngrams(s.split(),1)
    unigram_freq = Counter(unigrams)
    unigram_prob={}
    start_words=[]
    stop_words={}
    stop_pos = []
    rv=[]
    for gram in unigram_freq:
        unigram_prob[gram] = unigram_freq[gram] / v         

    for gram in unigram_freq:
        if re.match(r'<S>.*', gram[0]):
            start_words.append(gram)
    for gram in unigram_prob:
        if re.match(r'.+</S>', gram[-1]):
            stop_words[gram] = unigram_prob[gram]
    #Find best word to follow hard coded start word
    
    rv = list(random.choice(list(start_words)))
    for i in range(0,6):
        rv.append(random.choice(list(unigram_prob)))
    rv.append(random.choice(list(stop_words)))
    print(rv)