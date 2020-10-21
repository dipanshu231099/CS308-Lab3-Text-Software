from string import punctuation

#defining set of words to skip will calculating various actions
articles = ['a','an','the',"i","is","and","are","in"]

def removePunctuations(string):
    """
    removing punctuation marks from a string
    """
    for punctuationMark in list(punctuation):
        string=string.replace(punctuationMark,"")
    return string

def removeEmptyLines(lines):
    """
    removing empty lines from a string
    """
    linesPtr=0
    while(linesPtr<len(lines)):
        if(lines[linesPtr]==''):
            lines.pop(linesPtr)
        else:
            linesPtr+=1

def wordMapper(textFile,debug=0):
    """
    Function to make a count of all words only in the text. Ignores any punctutation marks. The case is ignored.
    INPUT: File name as string (can be relative or absolute)
    OUTPUT: dictionary (map) of word and count
    Options: pass debug=1 as argument for console results
    """
    try:
        txt = open(textFile).read()
    except:
        print("No such file found. Aborting...")
        exit()

    #changing case of text file
    txt = txt.lower()

    # removing punctuation marks
    txt = removePunctuations(txt)
    
    # removing useless lines
    lines=txt.split('\n')
    removeEmptyLines(lines)

    # creating the hash map for words
    mapping={}
    for i in range(len(lines)):
        sentence = lines[i].lower().split()
        for word in sentence:
            # skipping the articles
            if(word in articles):
                continue
            try:
                mapping[word]+=1
            except:
                mapping[word]=1
    if debug:
        print("Mapping of words:",mapping)
    return mapping


def lineNumbers(textFile, token, debug=0):
    """
    Function to find the lines containing a particular token word. The function is not case sensitive.
    INPUT:  File name as string
    OUTPUT: list of obj=>(line_number, line)
    Options: pass debug=1 as argument for console results
    """
    try:
        txt = open(textFile).read()
    except:
        print("No such file found. Aborting...")
        exit()
    lines=txt.split('\n')
    found=[]
    for i in range(len(lines)):
        if(token in lines[i].lower()):
            found.append((i+1, lines[i]))
    if debug:
        print("Found",len(found),"matching lines")
    return found

def mostOccuringWords(textFile, debug=0):
    """
    INPUT:  string, input file, path can be relative or absolute
    OUTPUT: list of most occuring words
    Options: pass debug=1 as argument for console results
    """
    try:
        txt = open(textFile).read()
    except:
        print("No such file found. Aborting...")
        exit()
  
    # removing empty lines
    lines=txt.split('\n')
    removeEmptyLines(lines)

    # creating the required hashmap
    mapping={}
    maximumOccurence=0
    mostFrequent = []
    for i in range(len(lines)):
        sentence = lines[i].lower().split()
        for word in sentence:
            # skipping the articles
            if(word in articles):
                continue
            try:
                mapping[word]+=1
            except:
                mapping[word]=1
            if(mapping[word]>maximumOccurence):
                maximumOccurence=mapping[word]
    for word in mapping.keys():
        if(mapping[word]==maximumOccurence):
            mostFrequent.append((word,maximumOccurence))
    
    if debug:
        print("List of most occuring words:",mostFrequent)
    return mostFrequent

def leastOccuringWord(textFile, debug=0):
    """
    INPUT:  string, input file, path can be relative or absolute
    OUTPUT: list of most occuring words
    Options: pass debug=1 as argument for console results
    """
    try:
        txt = open(textFile).read()
    except:
        print("No such file found. Aborting...")
        exit()

    # making required hashmap
    mapping = wordMapper(textFile)
    minimumOccurence = min(mapping.values())

    # iterating within the map
    found=[]
    for word in mapping.keys():
        if(mapping[word]==minimumOccurence):
            found.append((word,mapping[word]))
    if debug:
        print("Found words with minimum occurence:",found)
    return found

def lineCounter(textFile, debug=0):
    """
    INPUT:  file path as string
    OUTPUT: number of non empty lines in the file
    Options:Debug mode, pass debug=1
    """
    try:
        txt = open(textFile).read()
    except:
        print("No such file found. Aborting...")
        exit()

    lines=txt.split('\n')

    # removing useless lines
    removeEmptyLines(lines)

    # making a count of lines
    if debug:
        print("Number of lines:",len(lines))
    return len(lines)

def WordCounter(textFile, debug=0):
    """
    INPUT:  file path as string
    OUTPUT: number of non-article words
    Options:debug mode pass, debug=1
    """
    try:
        txt = open(textFile).read()
    except:
        print("No such file found. Aborting...")
        exit()

    # skipping the articles and importing the mapping
    mapping = wordMapper(textFile)
    if debug:
        print(len(mapping.keys()))
    return len(mapping.keys())