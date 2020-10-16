from string import punctuation
from collections import Counter

def wordMapper(textFile):
    """
    Function to make a count of all words only in the text. Ignores any punctutation marks. The case is ignored.
    input: File name as string (can be relative or absolute)
    output: dictionary (map) of word and count
    """
    textFile = str(textFile)
    try:
        txt = open(textFile).read()
    except:
        print("No such file found. Aborting...")
        exit()
    for punctuationMark in list(punctuation):
        txt=txt.replace(punctuationMark,"")
    mapping = txt.lower().split()
    word_counts = Counter(mapping)
    return word_counts


def lineNumbers(textFile, token):
    """
    Function to find the lines containing a particular token word. The function is not case sensitive.
    input:  File name as string
    output: a list of obj=>(line_number, line)
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
    print("Found",len(found),"matching lines")
    return found



print(lineNumbers("/home/ninja/data/IIT-MANDI/semester-5/LAP/assignment-3/sampleTextFile","gandhi"))