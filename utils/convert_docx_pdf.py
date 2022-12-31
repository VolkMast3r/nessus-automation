import os
import sys



def convert_docx_to_pdf(filename):
    '''
    Function to convert docx to pdf
    Arguments:
        filename {str} -- filename of the docx file
    Returns:
        str -- filename of the pdf file
        
    '''
    if os.name == 'nt':
        import docx2pdf
        # Convert docx to pdf using docx2pdf library
        try:
            docx2pdf.convert(
                f'word_reports\\{filename}', f'pdf_reports\\{filename}.pdf')
        except Exception as e:
            print(e)
            return e
    else:
        # Convert docx to pdf using libreoffice command-line tool
        try:
            os.system(
                f'libreoffice --headless --convert-to pdf word_reports/{filename} --outdir pdf_reports/')
        except Exception as e:
            print(e)
            return e

    return filename





