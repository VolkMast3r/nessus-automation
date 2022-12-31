import os
import sys



def convert_docx_pdf(filename):
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


if __name__ == '__main__':
    # check if the filename is passed as an argument
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        convert_docx_pdf(filename)
    else:
        print('Please pass the filename as an argument as shown below:')
        print('python convert_docx_pdf.py filename.docx')



