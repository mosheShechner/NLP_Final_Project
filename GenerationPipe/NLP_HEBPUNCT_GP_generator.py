# ##########################################################################################
# module        NLP_HEBPUNCT_GP_generator
# ##########################################################################################
# path          ...\repository\GenerationPipe\NLP_HEBPUNCT_GP_generator.py
# Purpose       pre-process
# description
# ##########################################################################################
import NLP_HEBPUNCT_GP_pre_processing as preproc
chunkSize = 70
punctList = [r'.', r',', r'?',r'!',r'(',r')', r'—', r'–' ,r'\-', r'־' , r'"', r':', r';', '\'']

def generate(URLList):
    allParagraphList = []
    for URL in URLList:
        sourceCode = preproc.getSingleURLSourceCode(URL)
        ParagraphList = preproc.getCleanparagraph(sourceCode, punctList)
        for paragraph in ParagraphList:
            if len(" ".split(paragraph))>chunkSize:
                allParagraphList.append(paragraph)

URLList =  [("קפיטליזם","https://he.wikipedia.org/wiki/%D7%A7%D7%A4%D7%99%D7%98%D7%9C%D7%99%D7%96%D7%9D"),
            ("קרל מרקס","https://he.wikipedia.org/wiki/%D7%A7%D7%A8%D7%9C_%D7%9E%D7%A8%D7%A7%D7%A1"),
            ("אילן רמון","https://he.wikipedia.org/wiki/%D7%90%D7%99%D7%9C%D7%9F_%D7%A8%D7%9E%D7%95%D7%9F"),
            ("אלברט איינשטיין","https://he.wikipedia.org/wiki/%D7%90%D7%9C%D7%91%D7%A8%D7%98_%D7%90%D7%99%D7%99%D7%A0%D7%A9%D7%98%D7%99%D7%99%D7%9F")]
targetUrlList = ["https://he.wikipedia.org/wiki/%D7%A7%D7%A4%D7%99%D7%98%D7%9C%D7%99%D7%96%D7%9D",
                 "https://he.wikipedia.org/wiki/%D7%A7%D7%A8%D7%9C_%D7%9E%D7%A8%D7%A7%D7%A1",
                 "https://he.wikipedia.org/wiki/%D7%90%D7%99%D7%9C%D7%9F_%D7%A8%D7%9E%D7%95%D7%9F",
                 "https://he.wikipedia.org/wiki/%D7%90%D7%9C%D7%91%D7%A8%D7%98_%D7%90%D7%99%D7%99%D7%A0%D7%A9%D7%98%D7%99%D7%99%D7%9F"]

def getDataFromURLList(URLList):
    dataList = [preproc.getDataFromURL(URL) for URL in URLList]
    outData = r"<DATADEL>".join(dataList)
    return outData




