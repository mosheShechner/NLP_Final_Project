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


