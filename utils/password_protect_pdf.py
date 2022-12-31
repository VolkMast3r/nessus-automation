import os
import PyPDF2

# Linux password protect pdf
def password_protect_pdf_linux(filename):
    print(filename)
    if os.path.exists(f'pdf_reports/{filename}'):
        # check if the file is a pdf
        if filename.endswith('.pdf'):
            # get the password from the user
            password = "pl@tc0rp_ent"
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
                # create a folder for the encrypted pdf
                folder_name = filename.split('.')[0].replace('_', ' ')
                if not os.path.exists(f'pdf_reports/{folder_name}'):
                    os.mkdir(f'pdf_reports/{folder_name}')

                with open(f'pdf_reports/{folder_name}/Monthly_VA_Report_{filename}', 'wb') as result_pdf:
                    # write the encrypted pdf to the new file
                    pdf_writer.write(result_pdf)
            print(
                f'Password protected pdf saved as password_protected_{filename}')
                # remove the original file
            os.remove(f'pdf_reports/{filename}')
            # remove word doc
            # os.remove(f'word_reports/{filename}.docx')
        else:
            print('Please pass a pdf file as an argument')
    else:
        print('File does not exist')


def password_protect_pdf_windows(filename):
# check if the filename is passed as an argument
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



























