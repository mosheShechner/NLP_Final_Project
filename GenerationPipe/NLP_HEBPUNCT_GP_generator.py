# ##########################################################################################
# module        NLP_HEBPUNCT_GP_generator
# ##########################################################################################
# path          ...\repository\GenerationPipe\NLP_HEBPUNCT_GP_generator.py
# Purpose       generate training and test data
# description
# ##########################################################################################
import NLP_HEBPUNCT_GP_pre_processing as preproc
import os

# default parameters
# ##########################################################################################
minNumOfWords = 50
punctList           = [r'.', r',', r'?',r'!',r'(',r')', r'—', r'–' ,r'\-', r'־' , r'"', r':', r';', '\'', r'\[', r'\]']
keepPuncList        = [r'.', r',', r'?',r'!']
removePunctList                           = [r'(',r')', r'—', r'–' ,r'\-', r'־' , r'"', r':', r';', '\'', r'\[', r'\]']
numConst            = r'0'
engConst            = r'ENG'
XY_DelConst         = r'<XYDEL>'
DATA_DelConst       = r'<DATADEL>'

def addURLToData(URL, outFilePath_indx, outFilePath_data):
    if (os.path.isfile(outFilePath_indx)):
        outFile_indx = open(outFilePath_indx, "r+", encoding='utf-8')
        exitsURLList = outFile_indx.read().split("\n")
        print(exitsURLList)

        # check if URL exists
        if URL not in exitsURLList:
            # add URL to index
            outFile_indx.write(URL+"\n")
            outFile_indx.close()

            # add data
            outFile_data = open(outFilePath_data, "a", encoding='utf-8')
            data = DATA_DelConst + preproc.getDataFromURL(URL, numConst, engConst, XY_DelConst, DATA_DelConst)
            outFile_data.write(data)
            outFile_data.close()
        else:
            outFile_indx.close()
    else:
        # add URL to index
        outFile_indx = open(outFilePath_indx, "w", encoding='utf-8')
        outFile_indx.write(URL+"\n")
        outFile_indx.close()
        # add data
        outFile_data = open(outFilePath_data, "w", encoding='utf-8')
        data = preproc.getDataFromURL(URL, numConst, engConst, XY_DelConst, DATA_DelConst)
        outFile_data.write(data)
        outFile_data.close()

def generate(URLList, outFileName, verbose = True):
    # build data output file path
    scriptPath = os.path.dirname(os.path.realpath('__file__'))
    scriptPathPrev = os.path.split(scriptPath)[0]

    relFilePath_data = "\\data\\" + outFileName + ".txt"
    relFilePath_indx = "\\data\\" + outFileName + "_indx.txt"
    outFilePath_data = scriptPathPrev + relFilePath_data
    outFilePath_indx = scriptPathPrev + relFilePath_indx

    for URL in URLList:
        if (verbose): print("adding to data set URL: %s" %(URL))
        addURLToData(URL, outFilePath_indx, outFilePath_data)

targetUrlList = ["https://he.wikipedia.org/wiki/%D7%A7%D7%A4%D7%99%D7%98%D7%9C%D7%99%D7%96%D7%9D",
                 "https://he.wikipedia.org/wiki/%D7%A7%D7%A8%D7%9C_%D7%9E%D7%A8%D7%A7%D7%A1",
                 "https://he.wikipedia.org/wiki/%D7%90%D7%99%D7%9C%D7%9F_%D7%A8%D7%9E%D7%95%D7%9F",
                 "https://he.wikipedia.org/wiki/%D7%90%D7%9C%D7%91%D7%A8%D7%98_%D7%90%D7%99%D7%99%D7%A0%D7%A9%D7%98%D7%99%D7%99%D7%9F"]

generate(targetUrlList, "train_data", True)






