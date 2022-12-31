import os
import sys
import PyPDF2


# Linux password protect pdf
def password_protect_pdf_linux(filename):
    # check if the filename is passed as an argument
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        # check if the file exists
        if os.path.exists(filename):
            # check if the file is a pdf
            if filename.endswith('.pdf'):
                # get the password from the user
                password = input('Enter the password to protect the pdf: ')
                with open(f'pdf_reports/{filename}', 'rb') as pdf_file:
                    # create a pdf reader object
                    pdf_reader = PyPDF2.PdfFileReader(pdf_file)
                    # create a pdf writer object
                    pdf_writer = PyPDF2.PdfFileWriter()
                    # loop through all the pages in the pdf
                    for page_num in range(pdf_reader.numPages):
                        # get the page
                        page = pdf_reader.getPage(page_num)
                        # add the page to the pdf writer
                        pdf_writer.addPage(page)
                    # encrypt the pdf with the password
                    pdf_writer.encrypt(password)
                    with open(f'pdf_reports/password_protected_{filename}', 'wb') as result_pdf:
                        # write the encrypted pdf to the new file
                        pdf_writer.write(result_pdf)
                print(
                    f'Password protected pdf saved as password_protected_{filename}')
            else:
                print('Please pass a pdf file as an argument')
        else:
            print('File does not exist')

    else:
        print('Please pass the filename as an argument as shown below:')
        print('python password_protect_pdf.py filename.pdf')

def password_protect_pdf_windows(filename):
    # check if the filename is passed as an argument
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        # check if the file exists
        if os.path.exists(filename):
            # check if the file is a pdf
            if filename.endswith('.pdf'):
                # get the password from the user
                password = input('Enter the password to protect the pdf: ')
                with open(f'pdf_reports\\{filename}', 'rb') as pdf_file:
                    # create a pdf reader object
                    pdf_reader = PyPDF2.PdfFileReader(pdf_file)
                    # create a pdf writer object
                    pdf_writer = PyPDF2.PdfFileWriter()
                    # loop through all the pages in the pdf
                    for page_num in range(pdf_reader.numPages):
                        # get the page
                        page = pdf_reader.getPage(page_num)
                        # add the page to the pdf writer
                        pdf_writer.addPage(page)
                    # encrypt the pdf with the password
                    pdf_writer.encrypt(password)
                    with open(f'pdf_reports\\password_protected_{filename}', 'wb') as result_pdf:
                        # write the encrypted pdf to the new file
                        pdf_writer.write(result_pdf)
                print(
                    f'Password protected pdf saved as password_protected_{filename}')
            else:
                print('Please pass a pdf file as an argument')
        else:
            print('File does not exist')

    else:
        print('Please pass the filename as an argument as shown below:')
        print('python password_protect_pdf.py filename.pdf')

# main function
if __name__ == '__main__':
    # check if the filename is passed as an argument
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        if os.name == 'nt':
            password_protect_pdf_windows(filename)
        else:
            password_protect_pdf_linux(filename)
    else:
        print('Please pass the filename as an argument as shown below:')
        print('python password_protect_pdf.py filename.pdf')

# Path: utils/convert_docx_pdf.py














































