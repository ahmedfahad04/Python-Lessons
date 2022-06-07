# # importing required modules 
# import PyPDF2 
 
# # creating a pdf file object 
# pdfFileObj = open('sample.pdf', 'rb') 

# print(type(pdfFileObj))
 
# # # creating a pdf reader object 
# # pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# # # creating a page object 
# # pageObj = pdfReader.getPage(0) 
 
# # # extracting text from page 
# # print(pageObj.extractText()) 
 
# # closing the pdf file object 
# pdfFileObj.close()
file = open('sample.pdf', 'rb')

f = open('hello.bin', 'wb')
f.write(file)