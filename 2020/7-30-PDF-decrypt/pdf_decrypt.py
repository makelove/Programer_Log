# -*- encoding: utf-8 -*-
'''
@File    :   pdf_decrypt.py
@Time    :   2020/07/30 16:48:24
@Author  :   play4fun
@Desc    :   
'''

def t1():
    #读取PDF文档
    import PyPDF2
    PDFfile='/Users/play/Downloads/UM_HERO_CS_REVA_WEB.pdf'
    pdf_obj=open(PDFfile,'rb')
    pdf_reader=PyPDF2.PdfFileReader(pdf_obj)
    pdf_reader.isEncrypted#False 没有加密

def 加密():
    from PyPDF2 import PdfFileWriter, PdfFileReader

    output = PdfFileWriter()
    p1=pdf_reader.getPage(2)#添加页面
    output.addPage(p1)
    p1=pdf_reader.getPage(4)
    output.addPage(p1)
    p1=pdf_reader.getPage(6)
    output.addPage(p1)

    password = "secret"
    output.encrypt(password)#加密

    outputStream = open("PyPDF2-output.pdf", "wb")
    output.write(outputStream)#写入新文档
    outputStream.close()
    pass
def 解密():
    from PyPDF2 import PdfFileReader
    am = open("PyPDF2-output.pdf", "rb")
    rd1 = PdfFileReader(am, strict=False)
    rd1.isEncrypted #True
    ter = PdfFileWriter() #新建

    rs=rd1.decrypt('secret')#解密
    rs# 1
    ter.appendPagesFromReader(rd1)
    ter.write(open('decrypted_filename.pdf', 'wb'))
    pass

if __name__ == "__main__":
    main()
