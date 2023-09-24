# import PyPDF2

# #Extracting information from pdf file.

# pdf_read=open("ReleaseLetter_1.pdf","rb")
# pdf_reader = PyPDF2.PdfReader(pdf_read)
# pdf_pages=len(pdf_reader.pages)
# print(pdf_pages)
# page_select=pdf_reader.pages[0]
# pdf_txt=page_select.extract_text()
# print(pdf_txt)
# pdf_read.close()


# #Merging 2 pdf files.

# from PyPDF2 import PdfReader, PdfMerger

# file1_read=open("ReleaseLetter_1.pdf","rb")
# file2_read=open("ServiceCertificate_1.pdf","rb")
# merge_final=PdfMerger()
# merge_final.append(file1_read)
# merge_final.append(file2_read)
# with open("finalMergedFile.pdf","wb") as a:
#     merge_final.write(a)


#Saving a pdf file content into a text file.

import PyPDF2
pdf_read=open("ServiceCertificate_1.pdf","rb")
pdf_reader=PyPDF2.PdfReader(pdf_read)
page_select = pdf_reader.pages[0]
pdf_text = page_select.extract_text()

txt_file = open("pdfText.txt","w")
txt_file.write(pdf_text)
txt_file.close()