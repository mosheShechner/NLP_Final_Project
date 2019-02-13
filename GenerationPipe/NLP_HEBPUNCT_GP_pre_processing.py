# ##########################################################################################
# module        NLP_HEBPUNCT_GP_pre_processing
# ##########################################################################################
# path          .../repository\GenerationPipe\NLP_HEBPUNCT_GP_pre_processing.py
# Purpose       pre-process
# description
# ##########################################################################################
from urllib import request
import re
import nltk
from nltk import word_tokenize, sent_tokenize

# default parameters
# ##########################################################################################
minNumOfWords = 50
punctList           = [r'.', r',', r'?',r'!',r'(',r')', r'—', r'–' ,r'\-', r'־' , r'"', r':', r';', '\'', r'\[', r'\]']
keepPuncList        = [r'.', r',', r'?',r'!']
removePunctList                           = [r'(',r')', r'—', r'–' ,r'\-', r'־' , r'"', r':', r';', '\'', r'\[', r'\]']
numConst            = r'0'
engConst            =  r'ENG'
XY_DelConst         = r'<XYDEL>'
DATA_DelConst       = r'<DATADEL>'

# 1.Fetch
# ##########################################################################################
def getSingleURLSourceCode(URL):
    # get handle to URL
    response = request.urlopen(URL)
    # fetch source code
    sourceCode = response.read().decode('utf8')
    return sourceCode

# 2.Clean - HTML code removal functions (getCleanParagraph)
# ##########################################################################################
def replaceInternalLinkWithText(inText):
    # function replaces link syntax in html code with it's shown text
    pattern = re.compile(r'<a href="[^"]*" title="[^"]*">([^<]*)</a>')
    outText = pattern.sub(r'\1', inText)
    return outText

def replaceExternalLinkWithText(inText):
    # function replaces link syntax in html code with it's shown text
    pattern = re.compile(r'<a rel="[^"]*" class="[^"]*" href="[^"]*">([^<]*)</a>')
    outText = pattern.sub(r'\1', inText)
    return outText

def replaceRedirectWithText(inText):
    # function replaces link syntax in html code with it's shown text
    pattern = re.compile(r'<a href="[^"]*" class="[^"]*" title="[^"]*">([^<]*)</a>')
    outText = pattern.sub(r'\1', inText)
    return outText

def replaceSmallReferenceLink(inText):
    # function replaces small reffences syntax in html code with it's shown text
    pattern = re.compile(r'<small class="[^"]*" dir="[^"]*">([^<]*)</small>')
    outText = pattern.sub(r'\1', inText)
    return outText

def replaceHebQuateCode(inText):
    # function replaces HTML heb quatation with shown text
    pattern = re.compile(r'<span class="[^"]*">([^<]*)</span>')
    outText = pattern.sub(r'\1', inText)
    return outText

def removeReferenceLink(inText):
    # function removes reffences from text
    pattern = re.compile(r'<sup id="[^"]*" class="[^"]*"><a href="[^"]*">[^<]*</a></sup>')
    outText = pattern.sub(r'', inText)
    return outText

def removeBold(inText):
    pattern = re.compile(r'<b>([^<]*)</b>')
    outText = pattern.sub(r'\1',inText)
    return outText

# 3.Truncate -  (getCleanParagraph)
# ##########################################################################################
def getParagraph(inStr: str, punctList):
    regExp =  r'<p>[א-ת0-9a-zA-Z\s' + r''.join(punctList) + r']*</p>'
    # print(regExp)
    strListWithDelimiters = re.findall(regExp, inStr, re.UNICODE)
    strListNoDelimiters = [re.sub(r'<p>', '', strWithDelimiter) for strWithDelimiter in strListWithDelimiters]
    strListNoDelimiters = [re.sub(r'</p>', '', strWithDelimiter) for strWithDelimiter in strListNoDelimiters]
    return strListNoDelimiters

def getCleanParagraph(inRawText, punctList):
    # function recives raw HTML hebrew wikipedia text and returns list of clean paragraphs
    # cleans: {reference link; internal link; external link; redirect link; bold mark}
    editedText = removeReferenceLink(inRawText)
    editedText = replaceInternalLinkWithText(editedText)
    editedText = replaceExternalLinkWithText(editedText)
    editedText = replaceRedirectWithText(editedText)
    editedText = replaceSmallReferenceLink(editedText)
    editedText = replaceHebQuateCode(editedText)
    editedText = removeBold(editedText)
    return getParagraph(editedText, punctList)

# 4.Format words - constant replacements for english and numerals (formatParagraph)
# ##########################################################################################
def replaceEnglish(inText, punctList, englishString = '<אנגלית>'):
    # function replaces
    punct = r''.join(punctList)
    pattern = re.compile(r'([a-zA-Z0-9]+[' + punct + r']*[a-zA-Z]+[a-zA-Z0-9]*|[a-zA-Z0-9]*[a-zA-Z]+[' + punct + r']*[a-zA-Z0-9]+|[a-zA-Z0-9]+[' + punct + r']*[a-zA-Z0-9]*[a-zA-Z]+|[a-zA-Z]+[a-zA-Z0-9]*[' + punct + r']*[a-zA-Z0-9]+)')
    #pattern = re.compile(r'([a-zA-Z0-9]+[' + punct + r']*[a-zA-Z]+[a-zA-Z0-9]*|[a-zA-Z0-9]*[a-zA-Z]+[' + punct + r']*[a-zA-Z0-9]+)')
    outText = pattern.sub(" " + englishString + " ", inText)
    pattern = re.compile(r'[a-zA-Z]')
    outText = pattern.sub(" " + englishString + " ", outText)
    return outText

def replaceNumber(inText, numberString = '<מספר>'):
    # function replaces
    pattern = re.compile(r'([0-9]+[,])*[0-9]+(\.[0-9]+)?')
    outText = pattern.sub(" " + numberString + " ", inText)
    return outText

def formatParagraph(inParagraph):
    # function recives paragraph, and return formatted text
    # outParagraph = replaceEnglish(inParagraph, punctList, '<אנגלית>')
    outParagraph = replaceEnglish(inParagraph, punctList, 'גבולאנגליתלובג')
    # outParagraph = replaceNumber(outParagraph, '<מספר>')
    outParagraph = replaceNumber(outParagraph, 'גבולמספרלובג')
    return outParagraph

# 5.Test for length - erase punctuation and keep (keepLongParagraphs)
# ##########################################################################################
def erasePunctuation(tokenList):
    newList = []
    for token in tokenList:
        if not(re.match("^\W+$", token)):
            newList.append(token)
    return newList

def keepLongParagraphs(paragraphList, minNumOfWords = 70):
    outParagraphList = []
    for paragraph in paragraphList:
        tokenList =  nltk.word_tokenize(paragraph)
        noPunctTokenList = erasePunctuation(tokenList)
        # paragraphLength = len(tokenList)
        numOfWords = len(noPunctTokenList)
        if (numOfWords >= minNumOfWords):
            # TBD here can insert more parameters of paragraph e.g. num of english words, num of digit words etc.
            outParagraphList.append((paragraph, numOfWords))
    return outParagraphList

# 6.Vectorize - generate tags and set vector format (getXY)
# ##########################################################################################
def removePunct(inText, removePunctList):
    punct = r''.join(removePunctList)
    pattern = re.compile(r'[' + punct + ']')
    outText = pattern.sub(r' ', inText)
    return outText

def relpaceConstStr(inStr, matchStr, replaceStr):
    pattern = re.compile(matchStr)
    outStr = pattern.sub(replaceStr, inStr)
    return outStr

def tag_paragraph(paragraph, punctList):
    tokens = nltk.tokenize.word_tokenize(paragraph)
    x = []
    y = []
    for w in tokens:
        if w in punctList:
            y.pop()
            y.append(w)
        else:
            y.append("none")
            x.append(w)
    # for word, tag in zip(x,y): print("%s %s" %(word, tag))
    return x, y

def getXY(paragraph, removePunctList, keepPuncList, inNumConst = numConst, inEngConst = engConst, inXY_DelConst = XY_DelConst):
    # remove unwanted punctuation
    noPunctParagraph = removePunct(paragraph, removePunctList)

    # tag paragraph with remain punctuation
    X_vec, Y_vec = tag_paragraph(noPunctParagraph, keepPuncList)

    # joinn to string
    X_str = " ".join(X_vec)
    X_str = relpaceConstStr(X_str, "גבולמספרלובג", inNumConst)
    X_str = relpaceConstStr(X_str, "גבולאנגליתלובג", inEngConst)
    Y_str = " ".join(Y_vec)
    #  here can add record info
    XY_str = X_str + inXY_DelConst + Y_str
    return XY_str

# 7.Aggregate -
# ##########################################################################################
def getDataFromURL(URL, inNumConst = numConst, inEngConst = engConst, inXY_DelConst = XY_DelConst, inDATA_DelConst = DATA_DelConst):
    # fetch
    sourceCode = getSingleURLSourceCode(URL)

    # clean and truncate
    paragraphList = getCleanParagraph(sourceCode, punctList)

    # format words
    formattedParagraphList = [formatParagraph(paragraph) for paragraph in paragraphList]

    # keep long paragraphs only
    longParagraphList = keepLongParagraphs(formattedParagraphList, minNumOfWords)

    # vectorize
    XY_List = [getXY(paragraph[0], removePunctList, keepPuncList, inNumConst, inEngConst, inXY_DelConst) for paragraph in longParagraphList]

    # aggregate
    DATA = inDATA_DelConst.join(XY_List)
    return DATA