# API Documentation

A text analysis and plotting tool

## Credits

The API is maintained and developed by Dipanshu (B18054)

## Functions

The following are the defined functionalities enabled in the API:

1. removePunctuations(string)
    - INPUT:    String `string`
    - RETURNS:  String
    - USAGE:    removing punctuation marks from a string

2. removeEmptyLines(lines)
    - INPUT:    Array of Strings `lines`
    - RETURNS:  None
    - USAGE:    removing empty lines from a string

3. wordMapper(textFile,debug=0)
    - INPUT:    File Path (absolute preffered), (optional) debug mode
    - RETURNS:  Dictionary
    - USAGE:    Function to make a count of all words only in the text. Ignores any punctutation marks. The case is ignored.

4. lineNumbers(textFile, token, debug=0)
    - INPUT:    File Path, String `token`, (optional) debug mode
    - RETURNS:  Array of integers
    - USAGE:    Function to find the lines containing a particular token word. The function is not case sensitive.

5. mostOccuringWords(textFile, debug=0)
    - INPUT:    File Path (absolute preffered), (optional) debug mode
    - RETURNS:  Array of Strings
    - USAGE:    To produce a List of most occuring words

6. leastOccuringWord(textFile, debug=0)
    - INPUT:    File Path (absolute preffered), (optional) debug mode
    - RETURNS:  Array of Strings
    - USAGE:    To produce a List of least occuring words

7. lineCounter(textFile, debug=0)
    - INPUT:    File Path (absolute preffered), (optional) debug mode
    - RETURNS:  Integer
    - USAGE:    Count of number of lines in a file

8. WordCounter(textFile, debug=0)
    - INPUT:    File Path (absolute preffered), (optional) debug mode
    - RETURNS:  Integer
    - USAGE:    Count of number of words in a file (except Articles 'a' 'an' 'the')

