# Design Documentation

## Introduction
The project runs in Python3+ environment with Tkinter for GUI. It's best to use with Linux OS.

## Design
### Data Structures
#### 1) Hashmap/Dictionary
[Dictionary](https://docs.python.org/3/tutorial/datastructures.html#dictionaries) store count of words
- constant time O(1) access, given key
#### 2) Python list
[List](https://docs.python.org/3/tutorial/datastructures.html) store array results(like- words, lines)
- Easy to store/handle elements and perform linear search

<br/>

### Classes
#### 1) CustomText class  
- Highlight keywords in lines shown in GUI

<br/>

### Libraries/Modules
#### 1) string
- remove punctuations(like- ?, !)
#### 2) NLTK (Natural Language Toolkit)
- for string processing
#### 3) Tkinter
- to render GUI
#### 4) Matplotlib
- to show graph

<br/>

### Tradeoff/Limitations
- Most functions use linear search over space(words, lines) so increasing file size increases computation time
- File with many words may not fit in the limited space of graph reserved in GUI - user has to use toolkit provided with zooming options

<br/>

### Flow
#### Statistics functions
- mostoccuringWord - calculate hashMap/dictionary for words and maximumOccurence of any word, then does linear search over dictionary to find keys corresponding to value(=maximumOccurence)
- leastOccuringWord - call wordMapper(function), find minimum value in hashmap/dictionary and then find keys with this value by linear search over dictionary
- lineCounter - call removeEmptyLines(function) and then count lines
- wordCounter - call wordMapper(function) and find number of keys(=words) in hashMap/dictionary by it's size

<br/>

### Miscellaneous  
- Implementation is case insensitive
