# ##########################################################################################
# module        NLP_HEBPUNCT_GP_pre_processing
# ##########################################################################################
# path          .../repository\GenerationPipe\NLP_HEBPUNCT_GP_pre_processing.py
# Purpose       pre-process
# description
# ##########################################################################################
from urllib import request
import re

def getSingleURLSourceCode(URL):
    # get handle to URL
    response = request.urlopen(URL)
    # fetch source code
    sourceCode = response.read().decode('utf8')
    return sourceCode

def replaceInternalLinkWithText(inText):
    # function replaces link syntax in html with it's shown hebrew text
    pattern = re.compile(r'<a href="[^"]*" title="[^"]*">([^<]*)</a>')
    outText = pattern.sub(r'\1', inText)
    return outText

def replaceExternalLinkWithText(inText):
    # function replaces link syntax in html with it's shown hebrew text
    pattern = re.compile(r'<a rel="[^"]*" class="[^"]*" href="[^"]*">([^<]*)</a>')
    outText = pattern.sub(r'\1', inText)
    return outText

def replaceRedirectWithText(inText):
    # function replaces link syntax in html with it's shown hebrew text
    pattern = re.compile(r'<a href="[^"]*" class="[^"]*" title="[^"]*">([^<]*)</a>')
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

def getParagraph(inStr: str, punctList):
    regExp =  r'<p>[א-ת0-9a-zA-Z\s' + r''.join(punctList) + r']*</p>'
    print(regExp)
    strListWithDelimiters = re.findall(regExp, inStr, re.UNICODE)
    strListNoDelimiters = [re.sub(r'<p>', '', strWithDelimiter) for strWithDelimiter in strListWithDelimiters]
    strListNoDelimiters = [re.sub(r'</p>', '', strWithDelimiter) for strWithDelimiter in strListNoDelimiters]
    return strListNoDelimiters

def getCleanparagraph(inRawText, punctList):
    # function recives raw HTML hebrew wikipedia text and returns list of clean paragraphs
    # cleans: {reference link; internal link; external link; redirect link; bold mark}
    editedText = removeReferenceLink(inRawText)
    editedText = replaceInternalLinkWithText(editedText)
    editedText = replaceExternalLinkWithText(editedText)
    editedText = replaceRedirectWithText(editedText)
    editedText = removeBold(editedText)
    # print(editedText)
    return getParagraph(editedText, punctList)