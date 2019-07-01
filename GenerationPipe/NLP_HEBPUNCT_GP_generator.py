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

def addURLToData(URL, outFilePath_indx, outFilePath_data, outFilePath_stts):
    if (os.path.isfile(outFilePath_indx)):
        # index file exists (middle of process)

        outFile_indx = open(outFilePath_indx, "r+", encoding='utf-8')
        exitsURLList = outFile_indx.read().split("\n")
        # print(exitsURLList)

        # check if URL exists
        if URL not in exitsURLList:
            # add URL to index
            outFile_indx.write(URL+"\n")
            outFile_indx.close()

            (URLData, URLauxInfo) = preproc.getDataFromURL(URL, numConst, engConst, XY_DelConst, DATA_DelConst)
            if (preproc.checkVectorOK(URLData)):
                # add data
                outFile_data = open(outFilePath_data, "a", encoding='utf-8')
                data = DATA_DelConst + URLData
                outFile_data.write(data)
                outFile_data.close()

                # add statistics
                outFile_stts = open(outFilePath_stts, "r+", encoding='utf-8')
                prev_stts = eval(outFile_stts.read())
                outFile_stts.close()

                URLstts = preproc.calcDataStatistics(URLauxInfo)
                curr_stts = preproc.getUpdateStatistics(prev_stts, URLstts)

                outFile_stts = open(outFilePath_stts, "w", encoding='utf-8')
                prev_stts = outFile_stts.write(str(curr_stts))
                outFile_stts.close()
        else:
            outFile_indx.close()

    else:
        # index file is new

        # add URL to index
        outFile_indx = open(outFilePath_indx, "w", encoding='utf-8')
        outFile_indx.write(URL+"\n")
        outFile_indx.close()

        (data, auxInfo) = preproc.getDataFromURL(URL, numConst, engConst, XY_DelConst, DATA_DelConst)
        stts = preproc.calcDataStatistics(auxInfo)

        # add data
        outFile_data = open(outFilePath_data, "w", encoding='utf-8')
        outFile_data.write(data)
        outFile_data.close()

        # add statistics
        outFile_stts = open(outFilePath_stts, "w", encoding='utf-8')
        outFile_stts.write(str(stts))
        outFile_stts.close()

def generate(URLList, outFileName, verbose = True):
    # build data output file path
    scriptPath = os.path.dirname(os.path.realpath('__file__'))
    scriptPathPrev = os.path.split(scriptPath)[0]

    relFilePath_data = "\\data\\" + outFileName + ".txt"
    relFilePath_indx = "\\data\\" + outFileName + "_indx.txt"
    relFilePath_stts = "\\data\\" + outFileName + "_aux_stats.txt"
    outFilePath_data = scriptPathPrev + relFilePath_data
    outFilePath_indx = scriptPathPrev + relFilePath_indx
    outFilePath_stts = scriptPathPrev + relFilePath_stts

    #if (verbose): print("DEBUG adding to data set URLList: %s" % (URLList))
    for URL in URLList:
        if (verbose): print("DEBUG adding to data set URL: %s" %(URL))
        addURLToData(URL, outFilePath_indx, outFilePath_data, outFilePath_stts)

def getStringFromDataFile(filePrefix):
    scriptPath = os.path.dirname(os.path.realpath('__file__'))
    scriptPathPrev = os.path.split(scriptPath)[0]
    relFilePath_data = "\\data\\" + filePrefix + ".txt"

    dataFilePath    = scriptPathPrev + relFilePath_data
    dataFile        = open(dataFilePath, "r", encoding='utf-8')
    dataStr         = dataFile.read()
    # print(dataStr)
    return dataStr

targetUrlList = ["https://he.wikipedia.org/wiki/%D7%A7%D7%A4%D7%99%D7%98%D7%9C%D7%99%D7%96%D7%9D",
                 "https://he.wikipedia.org/wiki/%D7%A7%D7%A8%D7%9C_%D7%9E%D7%A8%D7%A7%D7%A1",
                 "https://he.wikipedia.org/wiki/%D7%90%D7%99%D7%9C%D7%9F_%D7%A8%D7%9E%D7%95%D7%9F",
                 "https://he.wikipedia.org/wiki/%D7%90%D7%9C%D7%91%D7%A8%D7%98_%D7%90%D7%99%D7%99%D7%A0%D7%A9%D7%98%D7%99%D7%99%D7%9F"]

readyUrlList1 = [
    "https://he.wikipedia.org/wiki/%D7%A7%D7%A4%D7%99%D7%98%D7%9C%D7%99%D7%96%D7%9D",
    "https://he.wikipedia.org/wiki/%D7%A7%D7%A8%D7%9C_%D7%9E%D7%A8%D7%A7%D7%A1",
    "https://he.wikipedia.org/wiki/%D7%90%D7%99%D7%9C%D7%9F_%D7%A8%D7%9E%D7%95%D7%9F",
    "https://he.wikipedia.org/wiki/%D7%90%D7%9C%D7%91%D7%A8%D7%98_%D7%90%D7%99%D7%99%D7%A0%D7%A9%D7%98%D7%99%D7%99%D7%9F",
    "https://he.wikipedia.org/wiki/%D7%A7%D7%A8%D7%99%D7%A4%D7%98%D7%95%D7%92%D7%A8%D7%A4%D7%99%D7%94",
    "https://he.wikipedia.org/wiki/%D7%9E%D7%92%D7%93%D7%9C%D7%99_%D7%94%D7%90%D7%A0%D7%95%D7%99",
    "https://he.wikipedia.org/wiki/%D7%90%D7%93%D7%95%D7%95%D7%99%D7%9F_%D7%94%D7%90%D7%91%D7%9C",
    "https://he.wikipedia.org/wiki/%D7%94%D7%A9%D7%93%D7%94_%D7%94%D7%9E%D7%92%D7%A0%D7%98%D7%99_%D7%A9%D7%9C_%D7%9B%D7%93%D7%95%D7%A8_%D7%94%D7%90%D7%A8%D7%A5",
    "https://he.wikipedia.org/wiki/%D7%97%D7%95%D7%A7%D7%99_%D7%A7%D7%A4%D7%9C%D7%A8",
    "https://he.wikipedia.org/wiki/%D7%A4%D7%95%D7%98%D7%95%D7%9F",
    "https://he.wikipedia.org/wiki/%D7%9E%D7%A8%D7%97%D7%91-%D7%96%D7%9E%D7%9F",
    "https://he.wikipedia.org/wiki/%D7%97%D7%95%D7%A8_%D7%A9%D7%97%D7%95%D7%A8",
    "https://he.wikipedia.org/wiki/%D7%9E%D7%A9%D7%A4%D7%98_%D7%A9%D7%9C%D7%9E%D7%94",
    "https://he.wikipedia.org/wiki/%D7%92%D7%A0%D7%99%D7%91%D7%AA_%D7%94%D7%91%D7%A8%D7%9B%D7%95%D7%AA",
    "https://he.wikipedia.org/wiki/%D7%99%D7%94%D7%93%D7%95%D7%AA_%D7%A7%D7%95%D7%A0%D7%A1%D7%A8%D7%91%D7%98%D7%99%D7%91%D7%99%D7%AA",
    "https://he.wikipedia.org/wiki/%D7%99%D7%94%D7%93%D7%95%D7%AA_%D7%A7%D7%A8%D7%90%D7%99%D7%AA",
    "https://he.wikipedia.org/wiki/%D7%AA%D7%A0%D7%95%D7%A2%D7%AA_%D7%94%D7%97%D7%A1%D7%99%D7%93%D7%95%D7%AA",
    "https://he.wikipedia.org/wiki/%D7%99%D7%A8%D7%95%D7%A9%D7%9C%D7%99%D7%9D_%D7%91%D7%AA%D7%A7%D7%95%D7%A4%D7%AA_%D7%91%D7%99%D7%AA_%D7%A9%D7%A0%D7%99",
    "https://he.wikipedia.org/wiki/%D7%90%D7%A8%D7%99%D7%AA%D7%9E%D7%98%D7%99%D7%A7%D7%94",
    "https://he.wikipedia.org/wiki/%D7%97%D7%96%D7%A7%D7%94_(%D7%9E%D7%AA%D7%9E%D7%98%D7%99%D7%A7%D7%94)",
    "https://he.wikipedia.org/wiki/%D7%97%D7%99%D7%93%D7%95%D7%AA_%D7%97%D7%99%D7%AA%D7%95%D7%9A_%D7%95%D7%94%D7%A8%D7%9B%D7%91%D7%94",
    "https://he.wikipedia.org/wiki/%D7%A4%D7%95%D7%A8%D7%98%D7%9C:%D7%A2%D7%A8%D7%9B%D7%99%D7%9D_%D7%9E%D7%95%D7%9E%D7%9C%D7%A6%D7%99%D7%9D/%D7%A2%D7%A8%D7%9B%D7%99%D7%9D/%D7%A7%D7%98%D7%9C%D7%9F",
    "https://he.wikipedia.org/wiki/%D7%A4%D7%95%D7%A8%D7%98%D7%9C:%D7%A2%D7%A8%D7%9B%D7%99%D7%9D_%D7%9E%D7%95%D7%9E%D7%9C%D7%A6%D7%99%D7%9D/%D7%A2%D7%A8%D7%9B%D7%99%D7%9D/%D7%A9%D7%9E%D7%95%D7%A8%D7%95%D7%AA_%D7%94%D7%A4%D7%A0%D7%93%D7%94_%D7%94%D7%A2%D7%A0%D7%A7_%D7%91%D7%A1%D7%A6%27%D7%95%D7%90%D7%9F",
    "https://he.wikipedia.org/wiki/%D7%A4%D7%95%D7%A8%D7%98%D7%9C:%D7%A2%D7%A8%D7%9B%D7%99%D7%9D_%D7%9E%D7%95%D7%9E%D7%9C%D7%A6%D7%99%D7%9D/%D7%A2%D7%A8%D7%9B%D7%99%D7%9D/%D7%A9%D7%97%D7%A4%D7%99%D7%AA_%D7%94%D7%A7%D7%95%D7%98%D7%91",
    "https://he.wikipedia.org/wiki/%D7%A4%D7%95%D7%A8%D7%98%D7%9C:%D7%A2%D7%A8%D7%9B%D7%99%D7%9D_%D7%9E%D7%95%D7%9E%D7%9C%D7%A6%D7%99%D7%9D/%D7%A2%D7%A8%D7%9B%D7%99%D7%9D/%D7%A9%D7%99%D7%9E%D7%A4%D7%A0%D7%96%D7%94_%D7%9E%D7%A6%D7%95%D7%99",
    "https://he.wikipedia.org/wiki/%D7%A4%D7%95%D7%A8%D7%98%D7%9C:%D7%A2%D7%A8%D7%9B%D7%99%D7%9D_%D7%9E%D7%95%D7%9E%D7%9C%D7%A6%D7%99%D7%9D/%D7%A2%D7%A8%D7%9B%D7%99%D7%9D/%D7%A9%D7%99%D7%A8%D7%AA_%D7%94%D7%9C%D7%95%D7%95%D7%99%D7%99%D7%AA%D7%9F",
    "https://he.wikipedia.org/wiki/%D7%A4%D7%95%D7%A8%D7%98%D7%9C:%D7%A2%D7%A8%D7%9B%D7%99%D7%9D_%D7%9E%D7%95%D7%9E%D7%9C%D7%A6%D7%99%D7%9D/%D7%A2%D7%A8%D7%9B%D7%99%D7%9D/%D7%AA%D7%A0%D7%99%D7%A0%D7%90%D7%99%D7%9D",
    "https://he.wikipedia.org/wiki/%D7%A4%D7%95%D7%A8%D7%98%D7%9C:%D7%A2%D7%A8%D7%9B%D7%99%D7%9D_%D7%9E%D7%95%D7%9E%D7%9C%D7%A6%D7%99%D7%9D/%D7%A2%D7%A8%D7%9B%D7%99%D7%9D/%D7%94%D7%90%D7%93%D7%9D_%D7%94%D7%A0%D7%99%D7%90%D7%A0%D7%93%D7%A8%D7%98%D7%9C%D7%99",
    "https://he.wikipedia.org/wiki/%D7%A4%D7%95%D7%A8%D7%98%D7%9C:%D7%A2%D7%A8%D7%9B%D7%99%D7%9D_%D7%9E%D7%95%D7%9E%D7%9C%D7%A6%D7%99%D7%9D/%D7%A2%D7%A8%D7%9B%D7%99%D7%9D/%D7%94%D7%95%D7%9E%D7%95_%D7%90%D7%A8%D7%A7%D7%98%D7%95%D7%A1",
    "https://he.wikipedia.org/wiki/%D7%A4%D7%95%D7%A8%D7%98%D7%9C:%D7%A2%D7%A8%D7%9B%D7%99%D7%9D_%D7%9E%D7%95%D7%9E%D7%9C%D7%A6%D7%99%D7%9D/%D7%A2%D7%A8%D7%9B%D7%99%D7%9D/%D7%94%D7%95%D7%9E%D7%95_%D7%A4%D7%9C%D7%95%D7%A8%D7%A1%D7%99%D7%99%D7%A0%D7%A1%D7%99%D7%A1",
    "https://he.wikipedia.org/wiki/%D7%A4%D7%95%D7%A8%D7%98%D7%9C:%D7%A2%D7%A8%D7%9B%D7%99%D7%9D_%D7%9E%D7%95%D7%9E%D7%9C%D7%A6%D7%99%D7%9D/%D7%A2%D7%A8%D7%9B%D7%99%D7%9D/%D7%94%D7%99%D7%A4%D7%95%D7%A4%D7%95%D7%98%D7%9D",
    "https://he.wikipedia.org/wiki/%D7%A4%D7%95%D7%A8%D7%98%D7%9C:%D7%A2%D7%A8%D7%9B%D7%99%D7%9D_%D7%9E%D7%95%D7%9E%D7%9C%D7%A6%D7%99%D7%9D/%D7%A2%D7%A8%D7%9B%D7%99%D7%9D/%D7%91%D7%99%D7%9C%D7%91%D7%99_%D7%A2%D7%A0%D7%A7",
    "https://he.wikipedia.org/wiki/%D7%A4%D7%95%D7%A8%D7%98%D7%9C:%D7%A2%D7%A8%D7%9B%D7%99%D7%9D_%D7%9E%D7%95%D7%9E%D7%9C%D7%A6%D7%99%D7%9D/%D7%A2%D7%A8%D7%9B%D7%99%D7%9D/%D7%A0%D7%93%D7%99%D7%93%D7%AA_%D7%A2%D7%95%D7%A4%D7%95%D7%AA",
    "https://he.wikipedia.org/wiki/%D7%A8%D7%99%D7%A6%27%D7%A8%D7%93_%D7%93%D7%95%D7%A7%D7%99%D7%A0%D7%A1",
    "https://he.wikipedia.org/wiki/%D7%A0%D7%99%D7%A1%D7%95%D7%99%D7%99%D7%9D_%D7%91%D7%9C%D7%A9%D7%A0%D7%99%D7%99%D7%9D_%D7%91%D7%A7%D7%95%D7%A4%D7%99_%D7%90%D7%93%D7%9D",
    "https://he.wikipedia.org/wiki/%D7%92%27%D7%99%D7%A0%D7%92%27%D7%99",
    "https://he.wikipedia.org/wiki/%D7%A1%D7%9E%D7%99%D7%9D_%D7%91%D7%A1%D7%A4%D7%95%D7%A8%D7%98",
    "https://he.wikipedia.org/wiki/%D7%90%D7%A8%D7%A1",
    "https://he.wikipedia.org/wiki/%D7%A7%D7%9C%D7%A8%D7%94_%D7%91%D7%A8%D7%98%D7%95%D7%9F",
    "https://he.wikipedia.org/wiki/%D7%91%D7%AA%D7%99%D7%A8%D7%AA_%D7%90%D7%91%D7%99_%D7%94%D7%A2%D7%95%D7%A8%D7%A7%D7%99%D7%9D",
    "https://he.wikipedia.org/wiki/%D7%A9%D7%93%D7%A8%D7%95%D7%AA_%D7%A8%D7%95%D7%98%D7%A9%D7%99%D7%9C%D7%93",
    "https://he.wikipedia.org/wiki/%D7%AA%D7%9C_%D7%90%D7%91%D7%99%D7%91_%D7%91%D7%9E%D7%9C%D7%97%D7%9E%D7%AA_%D7%94%D7%A2%D7%A6%D7%9E%D7%90%D7%95%D7%AA",
    "https://he.wikipedia.org/wiki/%D7%AA%D7%9C_%D7%90%D7%91%D7%99%D7%91-%D7%99%D7%A4%D7%95",
    "https://he.wikipedia.org/wiki/%D7%90%D7%A8%D7%92%D7%95%D7%9F_%D7%A6%D7%91%D7%90%D7%99_%D7%9C%D7%90%D7%95%D7%9E%D7%99",
    "https://he.wikipedia.org/wiki/%D7%94%D7%94%D7%92%D7%A0%D7%94",
    "https://he.wikipedia.org/wiki/%D7%94%D7%94%D7%A2%D7%A4%D7%9C%D7%94",
    "https://he.wikipedia.org/wiki/%D7%94%D7%99%D7%99%D7%A9%D7%95%D7%91_%D7%94%D7%99%D7%A9%D7%9F",
    "https://he.wikipedia.org/wiki/%D7%94%D7%A9%D7%95%D7%9E%D7%A8",
    "https://he.wikipedia.org/wiki/%D7%96%D7%90%D7%91_%D7%96%27%D7%91%D7%95%D7%98%D7%99%D7%A0%D7%A1%D7%A7%D7%99",
    "https://he.wikipedia.org/wiki/%D7%97%D7%99%D7%99%D7%9D_%D7%90%D7%A8%D7%9C%D7%95%D7%96%D7%95%D7%A8%D7%95%D7%91_(%D7%90%D7%95%D7%A0%D7%99%D7%99%D7%AA_%D7%9E%D7%A2%D7%A4%D7%99%D7%9C%D7%99%D7%9D)",
    "https://he.wikipedia.org/wiki/%D7%9E%D7%9C%D7%95%D7%9F_%D7%94%D7%9E%D7%9C%D7%9A_%D7%93%D7%95%D7%93",
    "https://he.wikipedia.org/wiki/%D7%9E%D7%97%D7%9C%D7%A7%D7%AA_%D7%94%D7%9C%22%D7%94",
    "https://he.wikipedia.org/wiki/%D7%AA%D7%97%D7%99%D7%99%D7%AA_%D7%94%D7%9C%D7%A9%D7%95%D7%9F_%D7%94%D7%A2%D7%91%D7%A8%D7%99%D7%AA",
    "https://he.wikipedia.org/wiki/%D7%94%D7%A7%D7%A8%D7%91_%D7%A2%D7%9C_%D7%99%D7%A8%D7%95%D7%A9%D7%9C%D7%99%D7%9D_%D7%91%D7%9E%D7%9C%D7%97%D7%9E%D7%AA_%D7%A9%D7%A9%D7%AA_%D7%94%D7%99%D7%9E%D7%99%D7%9D",
    "https://he.wikipedia.org/wiki/%D7%97%D7%95%D7%9E%D7%95%D7%AA_%D7%99%D7%A8%D7%95%D7%A9%D7%9C%D7%99%D7%9D",
    "https://he.wikipedia.org/wiki/%D7%9E%D7%A0%D7%94%D7%A8%D7%95%D7%AA_%D7%94%D7%9B%D7%95%D7%AA%D7%9C",
    "https://he.wikipedia.org/wiki/%D7%90%D7%A1%D7%A4%D7%A7%D7%AA_%D7%94%D7%9E%D7%99%D7%9D_%D7%9C%D7%99%D7%A8%D7%95%D7%A9%D7%9C%D7%99%D7%9D",
    "https://he.wikipedia.org/wiki/%D7%9B%D7%A0%D7%A1%D7%99%D7%99%D7%AA_%D7%94%D7%A7%D7%91%D7%A8",
    "https://he.wikipedia.org/wiki/%D7%99%D7%A8%D7%95%D7%A9%D7%9C%D7%99%D7%9D_%D7%91%D7%AA%D7%A7%D7%95%D7%A4%D7%94_%D7%94%D7%9E%D7%9E%D7%9C%D7%95%D7%9B%D7%99%D7%AA",
    "https://he.wikipedia.org/wiki/%D7%99%D7%A8%D7%95%D7%A9%D7%9C%D7%99%D7%9D_%D7%91%D7%AA%D7%A7%D7%95%D7%A4%D7%94_%D7%94%D7%A6%D7%9C%D7%91%D7%A0%D7%99%D7%AA",
    "https://he.wikipedia.org/wiki/%D7%99%D7%A8%D7%95%D7%A9%D7%9C%D7%99%D7%9D_%D7%91%D7%AA%D7%A7%D7%95%D7%A4%D7%94_%D7%94%D7%91%D7%99%D7%96%D7%A0%D7%98%D7%99%D7%AA",
    "https://he.wikipedia.org/wiki/%D7%99%D7%A9%D7%A8%D7%90%D7%9C_%D7%91%D7%9E%D7%9C%D7%97%D7%9E%D7%AA_%D7%99%D7%95%D7%9D_%D7%94%D7%9B%D7%99%D7%A4%D7%95%D7%A8%D7%99%D7%9D",
    "https://he.wikipedia.org/wiki/%D7%A9%D7%9E%D7%95%D7%90%D7%9C_%D7%99%D7%95%D7%A1%D7%A3_%D7%A2%D7%92%D7%A0%D7%95%D7%9F",
    "https://he.wikipedia.org/wiki/%D7%A2%D7%A6%D7%99%D7%9D_%D7%A2%D7%AA%D7%99%D7%A7%D7%99%D7%9D_%D7%91%D7%90%D7%A8%D7%A5_%D7%99%D7%A9%D7%A8%D7%90%D7%9C",
    "https://he.wikipedia.org/wiki/%D7%9E%D7%A6%D7%93%D7%94",
    "https://he.wikipedia.org/wiki/%D7%9E%D7%A0%D7%97%D7%9D_%D7%91%D7%92%D7%99%D7%9F",
    "https://he.wikipedia.org/wiki/%D7%99%D7%A6%D7%97%D7%A7_%D7%A9%D7%9E%D7%99%D7%A8",
    "https://he.wikipedia.org/wiki/%D7%A9%D7%9E%D7%A2%D7%95%D7%9F_%D7%A4%D7%A8%D7%A1",
    "https://he.wikipedia.org/wiki/%D7%99%D7%92%D7%90%D7%9C_%D7%90%D7%9C%D7%95%D7%9F",
    "https://he.wikipedia.org/wiki/%D7%99%D7%97%D7%A1%D7%99_%D7%99%D7%A9%D7%A8%D7%90%D7%9C-%D7%A1%D7%A8%D7%99_%D7%9C%D7%A0%D7%A7%D7%94",
    "https://he.wikipedia.org/wiki/%D7%94%D7%97%D7%A7%D7%99%D7%A7%D7%94_%D7%91%D7%99%D7%A9%D7%A8%D7%90%D7%9C",
    "https://he.wikipedia.org/wiki/%D7%94%D7%9E%D7%A9%D7%A4%D7%98_%D7%91%D7%99%D7%A9%D7%A8%D7%90%D7%9C",
    "https://he.wikipedia.org/wiki/%D7%9E%D7%A2%D7%A8%D7%9B%D7%95%D7%AA_%D7%94%D7%9E%D7%A1%D7%AA%D7%95%D7%A8_%D7%A9%D7%9C_%D7%91%D7%A8_%D7%9B%D7%95%D7%9B%D7%91%D7%90",
    "https://he.wikipedia.org/wiki/%D7%A7%D7%A8%D7%91_%D7%A1%D7%98%D7%9C%D7%99%D7%A0%D7%92%D7%A8%D7%93",
    "https://he.wikipedia.org/wiki/%D7%94%D7%A4%D7%9C%D7%99%D7%A9%D7%94_%D7%9C%D7%A0%D7%95%D7%A8%D7%9E%D7%A0%D7%93%D7%99",
    "https://he.wikipedia.org/wiki/%D7%94%D7%9E%D7%A2%D7%A8%D7%9B%D7%94_%D7%91%D7%90%D7%95%D7%A7%D7%99%D7%99%D7%A0%D7%95%D7%A1_%D7%94%D7%90%D7%98%D7%9C%D7%A0%D7%98%D7%99_(1939%E2%80%931945)",
    "https://he.wikipedia.org/wiki/%D7%90%D7%95%D7%A9%D7%95%D7%95%D7%99%D7%A5",
    "https://he.wikipedia.org/wiki/%D7%90%D7%A0%D7%94_%D7%A4%D7%A8%D7%A0%D7%A7",
    "https://he.wikipedia.org/wiki/%D7%94%D7%97%D7%95%D7%A7_%D7%9C%D7%94%D7%92%D7%A0%D7%AA_%D7%94%D7%90%D7%95%D7%9E%D7%94",
    "https://he.wikipedia.org/wiki/%D7%90%D7%9C%D7%9B%D7%A1%D7%A0%D7%93%D7%A8_%D7%94%D7%92%D7%93%D7%95%D7%9C",
    "https://he.wikipedia.org/wiki/%D7%99%D7%95%D7%95%D7%9F_%D7%94%D7%A7%D7%9C%D7%90%D7%A1%D7%99%D7%AA",
    "https://he.wikipedia.org/wiki/%D7%9B%D7%99%D7%91%D7%95%D7%A9_%D7%94%D7%90%D7%99%D7%9E%D7%A4%D7%A8%D7%99%D7%94_%D7%94%D7%A4%D7%A8%D7%A1%D7%99%D7%AA_%D7%A2%D7%9C_%D7%99%D7%93%D7%99_%D7%90%D7%9C%D7%9B%D7%A1%D7%A0%D7%93%D7%A8_%D7%94%D7%92%D7%93%D7%95%D7%9C",
    "https://he.wikipedia.org/wiki/%D7%A9%D7%A0%D7%90%D7%AA_%D7%99%D7%A9%D7%A8%D7%90%D7%9C_%D7%91%D7%A2%D7%95%D7%9C%D7%9D_%D7%94%D7%99%D7%95%D7%95%D7%A0%D7%99-%D7%A8%D7%95%D7%9E%D7%99",
    "https://he.wikipedia.org/wiki/%D7%9B%D7%99%D7%91%D7%95%D7%A9%D7%99_%D7%90%D7%9C%D7%9B%D7%A1%D7%A0%D7%93%D7%A8_%D7%94%D7%92%D7%93%D7%95%D7%9C_%D7%91%D7%90%D7%A1%D7%99%D7%94_%D7%94%D7%AA%D7%99%D7%9B%D7%95%D7%A0%D7%94",
    "https://he.wikipedia.org/wiki/%D7%99%D7%95%D7%95%D7%9F_%D7%94%D7%90%D7%A8%D7%9B%D7%90%D7%99%D7%AA",
    "https://he.wikipedia.org/wiki/%D7%94%D7%90%D7%9D_%D7%92%D7%95%D7%92%D7%9C_%D7%A2%D7%95%D7%A9%D7%94_%D7%90%D7%95%D7%AA%D7%A0%D7%95_%D7%98%D7%99%D7%A4%D7%A9%D7%99%D7%9D%3F",
    "https://he.wikipedia.org/wiki/%D7%9C%D7%A7%D7%95%D7%AA_%D7%9C%D7%9E%D7%99%D7%93%D7%94",
    "https://he.wikipedia.org/wiki/%D7%A4%D7%A1%D7%99%D7%9B%D7%95%D7%A4%D7%AA%D7%99%D7%94",
    "https://he.wikipedia.org/wiki/%D7%94%D7%A4%D7%A8%D7%A2%D7%AA_%D7%A7%D7%A9%D7%91_%D7%91%D7%9E%D7%91%D7%95%D7%92%D7%A8%D7%99%D7%9D",
    "https://he.wikipedia.org/wiki/%D7%9E%D7%99%D7%A9%D7%9C_%D7%A4%D7%95%D7%A7%D7%95",
    "https://he.wikipedia.org/wiki/%D7%9E%D7%A9%D7%91%D7%A8_%D7%A7%D7%A8%D7%A0%D7%95%D7%AA_%D7%94%D7%A4%D7%A0%D7%A1%D7%99%D7%94_%D7%94%D7%92%D7%A8%D7%A2%D7%95%D7%A0%D7%99%D7%95%D7%AA",
    "https://he.wikipedia.org/wiki/%D7%97%D7%95%D7%A7_%D7%94%D7%94%D7%A1%D7%93%D7%A8%D7%99%D7%9D",
    "https://he.wikipedia.org/wiki/%D7%94%D7%94%D7%A1%D7%AA%D7%93%D7%A8%D7%95%D7%AA_%D7%94%D7%9B%D7%9C%D7%9C%D7%99%D7%AA_%D7%A9%D7%9C_%D7%94%D7%A2%D7%95%D7%91%D7%93%D7%99%D7%9D_%D7%91%D7%90%D7%A8%D7%A5_%D7%99%D7%A9%D7%A8%D7%90%D7%9C",
    "https://he.wikipedia.org/wiki/%D7%90%D7%93%D7%A8%D7%99%D7%9B%D7%9C%D7%95%D7%AA_%D7%92%D7%95%D7%AA%D7%99%D7%AA",
    "https://he.wikipedia.org/wiki/%D7%9B%D7%A0%D7%A1%D7%99%D7%99%D7%AA_%D7%94%D7%91%D7%A9%D7%95%D7%A8%D7%94",
    "https://he.wikipedia.org/wiki/%D7%94%D7%9E%D7%97%D7%9C%D7%95%D7%A7%D7%AA_%D7%A2%D7%9C_%D7%94%D7%98%D7%A7%D7%A1%D7%99%D7%9D_%D7%94%D7%A1%D7%99%D7%A0%D7%99%D7%99%D7%9D",
    "https://he.wikipedia.org/wiki/%D7%94%D7%99%D7%A1%D7%98%D7%95%D7%A8%D7%99%D7%94_%D7%A9%D7%9C_%D7%94%D7%9E%D7%99%D7%A1%D7%99%D7%95%D7%9F_%D7%94%D7%A0%D7%95%D7%A6%D7%A8%D7%99",
    "https://he.wikipedia.org/wiki/%D7%AA%D7%90%D7%95%D7%A8%D7%99%D7%99%D7%AA_%D7%A9%D7%A0%D7%99_%D7%94%D7%9E%D7%A7%D7%95%D7%A8%D7%95%D7%AA",
    "https://he.wikipedia.org/wiki/%D7%A6%D7%9C%D7%99%D7%91%D7%AA_%D7%99%D7%A9%D7%95",
    "https://he.wikipedia.org/wiki/%D7%9E%D7%94%D7%93%D7%99",
    "https://he.wikipedia.org/wiki/%D7%A4%D7%95%D7%A8%D7%98%D7%9C:%D7%92%27%D7%90%D7%96/%D7%A2%D7%A8%D7%9B%D7%99%D7%9D_%D7%9E%D7%95%D7%9E%D7%9C%D7%A6%D7%99%D7%9D",
    "https://he.wikipedia.org/wiki/%D7%A4%D7%95%D7%A8%D7%98%D7%9C:%D7%9B%D7%93%D7%95%D7%A8%D7%A1%D7%9C/%D7%A2%D7%A8%D7%9B%D7%99%D7%9D_%D7%9E%D7%95%D7%9E%D7%9C%D7%A6%D7%99%D7%9D",
    "https://he.wikipedia.org/wiki/%D7%A4%D7%9C%D7%94",
    "https://he.wikipedia.org/wiki/%D7%92%D7%91%D7%99%D7%A2_%D7%94%D7%A2%D7%95%D7%9C%D7%9D_%D7%91%D7%9B%D7%93%D7%95%D7%A8%D7%92%D7%9C",
    "https://he.wikipedia.org/wiki/%D7%91%D7%A8%D7%A6%D7%9C%D7%95%D7%A0%D7%94_(%D7%9B%D7%93%D7%95%D7%A8%D7%92%D7%9C)"]

readyUrlList2 = [
    "https://he.wikipedia.org/wiki/%D7%A7%D7%A8%D7%91_%D7%90%D7%99%D7%A1%D7%90%D7%A0%D7%93%D7%9C%D7%95%D7%95%D7%90%D7%A0%D7%94",
    "https://he.wikipedia.org/wiki/%D7%94%D7%9C%D7%9F_%D7%A7%D7%9C%D7%A8",
    "https://he.wikipedia.org/wiki/%D7%A8%D7%95%D7%91%D7%A8%D7%98_%D7%90%D7%95%D7%A4%D7%A0%D7%94%D7%99%D7%99%D7%9E%D7%A8",
    "https://he.wikipedia.org/wiki/%D7%93%D7%95%D7%93_%D7%91%D7%9F-%D7%92%D7%95%D7%A8%D7%99%D7%95%D7%9F",
    "https://he.wikipedia.org/wiki/%D7%93%D7%99%D7%95%D7%A0%D7%95%D7%9F_%D7%A2%D7%A0%D7%A7",
    "https://he.wikipedia.org/wiki/%D7%99%D7%A9%D7%A8%D7%90%D7%9C",
    "https://he.wikipedia.org/wiki/%D7%93%D7%9E%D7%95%D7%A7%D7%A8%D7%98%D7%99%D7%94_%D7%A4%D7%A8%D7%9C%D7%9E%D7%A0%D7%98%D7%A8%D7%99%D7%AA",
    "https://he.wikipedia.org/wiki/%D7%9E%D7%93%D7%99%D7%A0%D7%94_%D7%99%D7%94%D7%95%D7%93%D7%99%D7%AA_%D7%95%D7%93%D7%9E%D7%95%D7%A7%D7%A8%D7%98%D7%99%D7%AA",
    "https://he.wikipedia.org/wiki/%D7%94%D7%99%D7%9D_%D7%94%D7%AA%D7%99%D7%9B%D7%95%D7%9F",
    "https://he.wikipedia.org/wiki/%D7%AA%D7%9C_%D7%90%D7%91%D7%99%D7%91-%D7%99%D7%A4%D7%95",
    "https://he.wikipedia.org/wiki/%D7%94%D7%A1%D7%9B%D7%A1%D7%95%D7%9A_%D7%94%D7%99%D7%A9%D7%A8%D7%90%D7%9C%D7%99-%D7%A2%D7%A8%D7%91%D7%99",
    "https://he.wikipedia.org/wiki/%D7%99%D7%A8%D7%95%D7%A9%D7%9C%D7%99%D7%9D",
    "https://he.wikipedia.org/wiki/%D7%94%D7%A9%D7%95%D7%90%D7%94",
    "https://he.wikipedia.org/wiki/%D7%99%D7%94%D7%95%D7%93%D7%99%D7%9D",
    "https://he.wikipedia.org/wiki/%D7%A0%D7%A6%D7%A8%D7%95%D7%AA",
    "https://he.wikipedia.org/wiki/%D7%9E%D7%95%D7%A1%D7%9C%D7%9E%D7%99%D7%9D",
    "https://he.wikipedia.org/wiki/%D7%93%D7%A8%D7%95%D7%96%D7%99%D7%9D",
    "https://he.wikipedia.org/wiki/%D7%A2%D7%A8%D7%91%D7%99%D7%99_%D7%99%D7%A9%D7%A8%D7%90%D7%9C",
    "https://he.wikipedia.org/wiki/%D7%91%D7%93%D7%95%D7%90%D7%99%D7%9D",
    "https://he.wikipedia.org/wiki/%D7%9E%D7%9C%D7%95%D7%9F_%D7%94%D7%9E%D7%9C%D7%9A_%D7%93%D7%95%D7%93",
    "https://he.wikipedia.org/wiki/%D7%91%D7%99%D7%AA_%D7%94%D7%A9%D7%92%D7%A8%D7%99%D7%A8%D7%95%D7%AA_%D7%94%D7%A8%D7%95%D7%A1%D7%99%D7%AA",
    "https://he.wikipedia.org/wiki/%D7%9E%D7%92%D7%93%D7%9C_%D7%93%D7%95%D7%93",
    "https://he.wikipedia.org/wiki/%D7%94%D7%9E%D7%A8%D7%9B%D7%96_%D7%94%D7%91%D7%94%D7%90%D7%99_%D7%94%D7%A2%D7%95%D7%9C%D7%9E%D7%99#%D7%94%D7%9E%D7%AA%D7%97%D7%9D_%D7%94%D7%91%D7%94%D7%90%D7%99_%D7%A2%D7%9C_%D7%94%D7%A8_%D7%94%D7%9B%D7%A8%D7%9E%D7%9C",
    "https://he.wikipedia.org/wiki/%D7%A1%D7%98%D7%9C%D7%94_%D7%9E%D7%90%D7%A8%D7%99%D7%A1",
    "https://he.wikipedia.org/wiki/%D7%90%D7%91%D7%90_%D7%90%D7%91%D7%9F",
    "https://he.wikipedia.org/wiki/%D7%A9%D7%99%D7%A8%D7%95%D7%AA_%D7%94%D7%91%D7%99%D7%98%D7%97%D7%95%D7%9F_%D7%94%D7%9B%D7%9C%D7%9C%D7%99",
    "https://he.wikipedia.org/wiki/%D7%94%D7%97%D7%91%D7%A8%D7%94_%D7%9C%D7%94%D7%92%D7%A0%D7%AA_%D7%94%D7%98%D7%91%D7%A2",
    "https://he.wikipedia.org/wiki/%D7%9E%D7%9E%D7%A9%D7%9C%D7%AA_%D7%99%D7%A9%D7%A8%D7%90%D7%9C",
    "https://he.wikipedia.org/wiki/%D7%99%D7%95%D7%A0%D7%94_%D7%91%D7%9F_%D7%90%D7%9E%D7%99%D7%AA%D7%99",
    "https://he.wikipedia.org/wiki/%D7%94%D7%94%D7%92%D7%A0%D7%94",
    "https://he.wikipedia.org/wiki/%D7%90%D7%A8%D7%92%D7%95%D7%9F_%D7%A6%D7%91%D7%90%D7%99_%D7%9C%D7%90%D7%95%D7%9E%D7%99",
    "https://he.wikipedia.org/wiki/%D7%96%D7%90%D7%91_%D7%96%27%D7%91%D7%95%D7%98%D7%99%D7%A0%D7%A1%D7%A7%D7%99",
    "https://he.wikipedia.org/wiki/%D7%9E%D7%90%D7%99%D7%A8_%D7%93%D7%99%D7%96%D7%A0%D7%92%D7%95%D7%A3",
    "https://he.wikipedia.org/wiki/%D7%94%D7%9B%D7%A8%D7%96%D7%AA_%D7%94%D7%A2%D7%A6%D7%9E%D7%90%D7%95%D7%AA",
    "https://he.wikipedia.org/wiki/%D7%91%D7%A2%D7%99%D7%A8_%D7%94%D7%94%D7%A8%D7%92%D7%94",
    "https://he.wikipedia.org/wiki/%D7%97%D7%99%D7%99%D7%9D_%D7%A0%D7%97%D7%9E%D7%9F_%D7%91%D7%99%D7%90%D7%9C%D7%99%D7%A7",
    "https://he.wikipedia.org/wiki/%D7%A6%D7%99%D7%95%D7%A0%D7%95%D7%AA_%D7%91%D7%A8%D7%95%D7%A1%D7%99%D7%94",
    "https://he.wikipedia.org/wiki/%D7%94%D7%92%D7%93%D7%95%D7%93%D7%99%D7%9D_%D7%94%D7%A2%D7%91%D7%A8%D7%99%D7%99%D7%9D",
    "https://he.wikipedia.org/wiki/%D7%A4%D7%A8%D7%A2%D7%95%D7%AA_%D7%A4%D7%98%D7%9C%D7%99%D7%95%D7%A8%D7%94",
    "https://he.wikipedia.org/wiki/%D7%94%D7%90%D7%99%D7%9E%D7%A4%D7%A8%D7%99%D7%94_%D7%94%D7%91%D7%A8%D7%99%D7%98%D7%99%D7%AA",
    "https://he.wikipedia.org/wiki/%D7%94%D7%90%D7%99%D7%9E%D7%A4%D7%A8%D7%99%D7%94_%D7%94%D7%A1%D7%A4%D7%A8%D7%93%D7%99%D7%AA",
    "https://he.wikipedia.org/wiki/%D7%94%D7%90%D7%99%D7%9E%D7%A4%D7%A8%D7%99%D7%94_%D7%94%D7%A4%D7%95%D7%A8%D7%98%D7%95%D7%92%D7%96%D7%99%D7%AA",
    "https://he.wikipedia.org/wiki/%D7%97%D7%91%D7%A8%D7%AA_%D7%94%D7%95%D7%93%D7%95_%D7%94%D7%9E%D7%96%D7%A8%D7%97%D7%99%D7%AA_%D7%94%D7%91%D7%A8%D7%99%D7%98%D7%99%D7%AA",
    "https://he.wikipedia.org/wiki/%D7%9E%D7%9C%D7%97%D7%9E%D7%AA_%D7%9E%D7%90%D7%94_%D7%94%D7%A9%D7%A0%D7%99%D7%9D_%D7%94%D7%A9%D7%A0%D7%99%D7%99%D7%94",
    "https://he.wikipedia.org/wiki/%D7%A2%D7%91%D7%93%D7%95%D7%AA",
    "https://he.wikipedia.org/wiki/%D7%94%D7%9E%D7%9C%D7%97%D7%9E%D7%95%D7%AA_%D7%94%D7%A0%D7%A4%D7%95%D7%9C%D7%99%D7%90%D7%95%D7%A0%D7%99%D7%95%D7%AA",
    "https://he.wikipedia.org/wiki/%D7%A0%D7%A4%D7%95%D7%9C%D7%99%D7%90%D7%95%D7%9F_%D7%91%D7%95%D7%A0%D7%A4%D7%A8%D7%98%D7%94",
    "https://he.wikipedia.org/wiki/%D7%9E%D7%9C%D7%97%D7%9E%D7%AA_%D7%94%D7%A2%D7%95%D7%9C%D7%9D_%D7%94%D7%A8%D7%90%D7%A9%D7%95%D7%A0%D7%94",
    "https://he.wikipedia.org/wiki/%D7%94%D7%90%D7%99%D7%9E%D7%A4%D7%A8%D7%99%D7%94_%D7%94%D7%A2%D7%95%D7%AA%27%D7%9E%D7%90%D7%A0%D7%99%D7%AA",
    "https://he.wikipedia.org/wiki/%D7%94%D7%90%D7%99%D7%9E%D7%A4%D7%A8%D7%99%D7%94_%D7%94%D7%A8%D7%95%D7%A1%D7%99%D7%AA",
    "https://he.wikipedia.org/wiki/%D7%94%D7%90%D7%99%D7%9E%D7%A4%D7%A8%D7%99%D7%94_%D7%94%D7%91%D7%99%D7%96%D7%A0%D7%98%D7%99%D7%AA",
    "https://he.wikipedia.org/wiki/%D7%91%D7%99%D7%AA_%D7%A2%D7%91%D7%90%D7%A1",
    "https://he.wikipedia.org/wiki/%D7%95%D7%99%D7%A7%D7%99%D7%A0%D7%92%D7%99%D7%9D",
    "https://he.wikipedia.org/wiki/%D7%A0%D7%A6%D7%A8%D7%95%D7%AA_%D7%A7%D7%AA%D7%95%D7%9C%D7%99%D7%AA",
    "https://he.wikipedia.org/wiki/%D7%95%D7%99%D7%A0%D7%A1%D7%98%D7%95%D7%9F_%D7%A6%27%D7%A8%D7%A6%27%D7%99%D7%9C",
    "https://he.wikipedia.org/wiki/%D7%A4%D7%A8%D7%A0%D7%A7%D7%9C%D7%99%D7%9F_%D7%93%D7%9C%D7%90%D7%A0%D7%95_%D7%A8%D7%95%D7%96%D7%95%D7%95%D7%9C%D7%98",
    "https://he.wikipedia.org/wiki/%D7%9E%D7%9C%D7%97%D7%9E%D7%AA_%D7%94%D7%A2%D7%95%D7%9C%D7%9D_%D7%94%D7%A9%D7%A0%D7%99%D7%99%D7%94",
    "https://he.wikipedia.org/wiki/%D7%94%D7%90%D7%99%D7%9E%D7%A4%D7%A8%D7%99%D7%94_%D7%94%D7%90%D7%95%D7%A1%D7%98%D7%A8%D7%95-%D7%94%D7%95%D7%A0%D7%92%D7%A8%D7%99%D7%AA",
    "https://he.wikipedia.org/wiki/%D7%90%D7%A8%D7%9E%D7%99%D7%99%D7%94_%D7%A7%D7%A8%D7%99%D7%95%D7%91%D7%94",
    "https://he.wikipedia.org/wiki/%D7%94%D7%A6%D7%91%D7%90_%D7%94%D7%90%D7%93%D7%95%D7%9D",
    "https://he.wikipedia.org/wiki/%D7%9E%D7%A8%D7%93_%D7%95%D7%A8%D7%A9%D7%94",
    "https://he.wikipedia.org/wiki/%D7%9E%D7%9E%D7%9C%D7%9B%D7%AA_%D7%99%D7%A9%D7%A8%D7%90%D7%9C_%D7%94%D7%9E%D7%90%D7%95%D7%97%D7%93%D7%AA",
    "https://he.wikipedia.org/wiki/%D7%91%D7%99%D7%AA_%D7%94%D7%9E%D7%A7%D7%93%D7%A9",
    "https://he.wikipedia.org/wiki/%D7%94%D7%9E%D7%A8%D7%93_%D7%94%D7%A2%D7%A8%D7%91%D7%99_%D7%94%D7%92%D7%93%D7%95%D7%9C",
    "https://he.wikipedia.org/wiki/%D7%92%D7%A8%D7%9E%D7%A0%D7%99%D7%94_%D7%94%D7%A0%D7%90%D7%A6%D7%99%D7%AA",
    "https://he.wikipedia.org/wiki/%D7%94%D7%9C%D7%99%D7%92%D7%94_%D7%94%D7%A2%D7%A8%D7%91%D7%99%D7%AA",
    "https://he.wikipedia.org/wiki/%D7%91%D7%A0%D7%99%D7%9E%D7%99%D7%9F_%D7%96%D7%90%D7%91_%D7%94%D7%A8%D7%A6%D7%9C",
    "https://he.wikipedia.org/wiki/%D7%9E%D7%A0%D7%97%D7%9D_%D7%91%D7%92%D7%99%D7%9F",
    "https://he.wikipedia.org/wiki/%D7%9E%D7%9C%D7%97%D7%9E%D7%AA_%D7%99%D7%95%D7%9D_%D7%94%D7%9B%D7%99%D7%A4%D7%95%D7%A8%D7%99%D7%9D",
    "https://he.wikipedia.org/wiki/%D7%92%D7%95%D7%9C%D7%93%D7%94_%D7%9E%D7%90%D7%99%D7%A8",
    "https://he.wikipedia.org/wiki/%D7%9E%D7%9C%D7%97%D7%9E%D7%AA_%D7%94%D7%94%D7%AA%D7%A9%D7%94",
    "https://he.wikipedia.org/wiki/%D7%94%D7%96%D7%99%D7%A8%D7%94_%D7%94%D7%90%D7%99%D7%A8%D7%95%D7%A4%D7%99%D7%AA:_1942%E2%80%931945",
    "https://he.wikipedia.org/wiki/%D7%9E%D7%9C%D7%97%D7%9E%D7%AA_%D7%94%D7%A2%D7%A6%D7%9E%D7%90%D7%95%D7%AA",
    "https://he.wikipedia.org/wiki/%D7%9E%D7%9C%D7%97%D7%9E%D7%AA_%D7%A9%D7%A9%D7%AA_%D7%94%D7%99%D7%9E%D7%99%D7%9D",
    "https://he.wikipedia.org/wiki/%D7%A2%D7%9C%D7%99%D7%99%D7%94_%D7%9C%D7%90%D7%A8%D7%A5_%D7%99%D7%A9%D7%A8%D7%90%D7%9C#%D7%94%D7%A2%D7%9C%D7%99%D7%95%D7%AA_%D7%94%D7%92%D7%93%D7%95%D7%9C%D7%95%D7%AA_%D7%A2%D7%93_%D7%9C%D7%94%D7%A7%D7%9E%D7%AA_%D7%94%D7%9E%D7%93%D7%99%D7%A0%D7%94",
    "https://he.wikipedia.org/wiki/%D7%A6%D7%91%D7%90_%D7%94%D7%92%D7%A0%D7%94_%D7%9C%D7%99%D7%A9%D7%A8%D7%90%D7%9C",
    "https://he.wikipedia.org/wiki/%D7%90%D7%91%D7%99%D7%91_%D7%9B%D7%95%D7%9B%D7%91%D7%99",
    "https://he.wikipedia.org/wiki/%D7%9E%D7%9C%D7%97%D7%9E%D7%AA_%D7%94%D7%9E%D7%A4%D7%A8%D7%A5",
    "https://he.wikipedia.org/wiki/%D7%91%D7%A0%D7%99%D7%9E%D7%99%D7%9F_%D7%A0%D7%AA%D7%A0%D7%99%D7%94%D7%95",
    "https://he.wikipedia.org/wiki/%D7%90%D7%A8%D7%99%D7%90%D7%9C_%D7%A9%D7%A8%D7%95%D7%9F",
    "https://he.wikipedia.org/wiki/%D7%A6%D7%99%D7%95%D7%A0%D7%95%D7%AA",
    "https://he.wikipedia.org/wiki/%D7%AA%D7%A0%D7%95%D7%A2%D7%AA_%D7%94%D7%94%D7%A9%D7%9B%D7%9C%D7%94_%D7%94%D7%99%D7%94%D7%95%D7%93%D7%99%D7%AA",
    "https://he.wikipedia.org/wiki/%D7%99%D7%94%D7%95%D7%93%D7%99%D7%9D",
    "https://he.wikipedia.org/wiki/%D7%94%D7%A2%D7%9C%D7%99%D7%99%D7%94_%D7%94%D7%A9%D7%A0%D7%99%D7%99%D7%94",
    "https://he.wikipedia.org/wiki/%D7%A6%D7%99%D7%95%D7%A0%D7%95%D7%AA_%D7%9E%D7%A2%D7%A9%D7%99%D7%AA",
    "https://he.wikipedia.org/wiki/%D7%94%D7%A2%D7%9C%D7%99%D7%99%D7%94_%D7%94%D7%A8%D7%90%D7%A9%D7%95%D7%A0%D7%94",
    "https://he.wikipedia.org/wiki/%D7%90%D7%93%D7%9E%D7%95%D7%A0%D7%93_%D7%92%27%D7%99%D7%99%D7%9E%D7%A1_%D7%93%D7%94_%D7%A8%D7%95%D7%98%D7%A9%D7%99%D7%9C%D7%93",
    "https://he.wikipedia.org/wiki/%D7%A6%D7%99%D7%95%D7%A0%D7%95%D7%AA_%D7%93%D7%AA%D7%99%D7%AA",
    "https://he.wikipedia.org/wiki/%D7%90%D7%91%D7%A8%D7%94%D7%9D_%D7%99%D7%A6%D7%97%D7%A7_%D7%94%D7%9B%D7%94%D7%9F_%D7%A7%D7%95%D7%A7",
    "https://he.wikipedia.org/wiki/%D7%AA%D7%A4%D7%99%D7%A1%D7%AA_%D7%94%D7%91%D7%99%D7%98%D7%97%D7%95%D7%9F_%D7%A9%D7%9C_%D7%99%D7%A9%D7%A8%D7%90%D7%9C",
    "https://he.wikipedia.org/wiki/%D7%99%D7%95%D7%9D_%D7%94%D7%A2%D7%A6%D7%9E%D7%90%D7%95%D7%AA",
    "https://he.wikipedia.org/wiki/%D7%90%D7%A0%D7%98%D7%99%D7%A9%D7%9E%D7%99%D7%95%D7%AA",
    "https://he.wikipedia.org/wiki/%D7%90%D7%99%D7%99%D7%96%D7%A7_%D7%A0%D7%99%D7%95%D7%98%D7%95%D7%9F",
    "https://he.wikipedia.org/wiki/%D7%90%D7%95%D7%92%D7%95%D7%A1%D7%98%D7%9F_%D7%9C%D7%95%D7%90%D7%99_%D7%A7%D7%95%D7%A9%D7%99",
    "https://he.wikipedia.org/wiki/%D7%96%27%D7%95%D7%96%D7%A3_%D7%9C%D7%95%D7%90%D7%99_%D7%9C%D7%92%D7%A8%D7%90%D7%A0%D7%96%27",
    "https://he.wikipedia.org/wiki/%D7%90%D7%A8%D7%9B%D7%99%D7%9E%D7%93%D7%A1",
    "https://he.wikipedia.org/wiki/%D7%90%D7%91%D7%95%D7%9C%D7%95%D7%A6%D7%99%D7%94_%D7%A9%D7%9C_%D7%94%D7%90%D7%93%D7%9D",
    "https://he.wikipedia.org/wiki/%D7%A6%D7%99%D7%99%D7%93%D7%99%D7%9D-%D7%9C%D7%A7%D7%98%D7%99%D7%9D",
    "https://he.wikipedia.org/wiki/%D7%91%D7%99%D7%A0%D7%94_%D7%9E%D7%9C%D7%90%D7%9B%D7%95%D7%AA%D7%99%D7%AA",
    "https://he.wikipedia.org/wiki/%D7%A7%D7%A4%D7%99%D7%98%D7%9C%D7%99%D7%96%D7%9D",
    "https://he.wikipedia.org/wiki/%D7%A1%D7%95%D7%A6%D7%99%D7%90%D7%9C%D7%99%D7%96%D7%9D",
    "https://he.wikipedia.org/wiki/%D7%90%D7%A1%D7%A4%D7%99%D7%A8%D7%99%D7%9F",
    "https://he.wikipedia.org/wiki/%D7%90%D7%91%D7%95%D7%9C%D7%95%D7%A6%D7%99%D7%94",
    "https://he.wikipedia.org/wiki/%D7%90%D7%A0%D7%94_%D7%A4%D7%A8%D7%A0%D7%A7",
    "https://he.wikipedia.org/wiki/%D7%A7%D7%A8%D7%9C_%D7%A4%D7%A8%D7%99%D7%93%D7%A8%D7%99%D7%9A_%D7%92%D7%90%D7%95%D7%A1",
    "https://he.wikipedia.org/wiki/%D7%90%D7%9C%D7%99%D7%96%D7%91%D7%AA_%D7%94%D7%A8%D7%90%D7%A9%D7%95%D7%A0%D7%94,_%D7%9E%D7%9C%D7%9B%D7%AA_%D7%90%D7%A0%D7%92%D7%9C%D7%99%D7%94",
    "https://he.wikipedia.org/wiki/%D7%94%D7%A0%D7%A8%D7%99_%D7%94%D7%A9%D7%9E%D7%99%D7%A0%D7%99,_%D7%9E%D7%9C%D7%9A_%D7%90%D7%A0%D7%92%D7%9C%D7%99%D7%94",
    "https://he.wikipedia.org/wiki/%D7%A1%D7%99%D7%9F_(%D7%90%D7%96%D7%95%D7%A8)",
    "https://he.wikipedia.org/wiki/%D7%94%D7%99%D7%A0%D7%93%D7%95%D7%90%D7%99%D7%96%D7%9D",
    "https://he.wikipedia.org/wiki/%D7%99%D7%A4%D7%9F",
    "https://he.wikipedia.org/wiki/%D7%A0%D7%A6%D7%A8%D7%95%D7%AA_%D7%90%D7%95%D7%A8%D7%AA%D7%95%D7%93%D7%95%D7%A7%D7%A1%D7%99%D7%AA",
    "https://he.wikipedia.org/wiki/%D7%94%D7%A4%D7%A8%D7%93%D7%AA_%D7%94%D7%93%D7%AA_%D7%9E%D7%94%D7%9E%D7%93%D7%99%D7%A0%D7%94",
    "https://he.wikipedia.org/wiki/%D7%93%D7%9E%D7%95%D7%A7%D7%A8%D7%98%D7%99%D7%94_%D7%9C%D7%99%D7%91%D7%A8%D7%9C%D7%99%D7%AA",
    "https://he.wikipedia.org/wiki/%D7%9E%D7%A8%D7%A7%D7%A1%D7%99%D7%96%D7%9D",
    "https://he.wikipedia.org/wiki/%D7%A4%D7%A1%D7%99%D7%9B%D7%95%D7%9C%D7%95%D7%92%D7%99%D7%94",
    "https://he.wikipedia.org/wiki/%D7%A1%D7%95%D7%A7%D7%A8%D7%98%D7%A1",
    "https://he.wikipedia.org/wiki/%D7%94%D7%9E%D7%94%D7%A4%D7%9B%D7%94_%D7%94%D7%A6%D7%A8%D7%A4%D7%AA%D7%99%D7%AA",
    "https://he.wikipedia.org/wiki/%D7%90%D7%A7%D7%95%D7%9C%D7%95%D7%92%D7%99%D7%94",
    "https://he.wikipedia.org/wiki/%D7%90%D7%9C%D7%9B%D7%A1%D7%A0%D7%93%D7%A8_%D7%92%D7%A8%D7%94%D7%9D_%D7%91%D7%9C",
    "https://he.wikipedia.org/wiki/%D7%90%D7%93%D7%9D",
    "https://he.wikipedia.org/wiki/%D7%A4%D7%9E%D7%99%D7%A0%D7%99%D7%96%D7%9D",
    "https://he.wikipedia.org/wiki/%D7%91%D7%A8%D7%99%D7%90%D7%AA_%D7%94%D7%A2%D7%95%D7%9C%D7%9D",
    "https://he.wikipedia.org/wiki/%D7%AA%D7%95%D7%A8%D7%A9%D7%94,_%D7%A1%D7%91%D7%99%D7%91%D7%94_%D7%95%D7%94%D7%AA%D7%A4%D7%AA%D7%97%D7%95%D7%AA_%D7%94%D7%90%D7%93%D7%9D",
    "https://he.wikipedia.org/wiki/%D7%91%D7%97%D7%99%D7%A8%D7%94_%D7%97%D7%95%D7%A4%D7%A9%D7%99%D7%AA"]



#generate(readyUrlList, "2019_02_20_train_data", True)

# print(getStringFromDataFile("train_data"))

UrlList = []
UrlList.extend(readyUrlList1)
UrlList.extend(readyUrlList2)
#generate(UrlList, "2019_06_27_all_data", True)



