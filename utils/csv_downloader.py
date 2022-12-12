# Import HTTPX
import httpx
import json
import openpyxl
import pandas as pd
import os, sys
from dotenv import load_dotenv



# Get API keys from .env file  in the current directory
env_path = os.path.join(os.path.dirname(__file__), '../.env')
load_dotenv(env_path)
base_url = os.environ.get('base_url')
print(base_url)
headers = json.loads(os.environ.get('headers'))
print(headers)

def download_csv_report(scan_id):
    '''
    Function to download csv report from nessus
    '''
    # Get file IDS
    file_ids = httpx.post(f'{base_url}{scan_id}/export',
                        headers=headers, verify=False, json={"format": "csv"})
    print(json.dumps(file_ids.json(), indent=4, sort_keys=True))
    file_id = file_ids.json()['file']
    print(file_id)

    # wait for file to be generated loop
    while True:
        status = httpx.get(f'{base_url}{scan_id}/export/{file_id}/status',
                        headers=headers, verify=False)
        print(json.dumps(status.json(), indent=4, sort_keys=True))
        if status.json()['status'] != 'ready':
            continue
        # download file
        report = httpx.get(
            f'{base_url}{scan_id}/export/{file_id}/download', headers=headers, verify=False)
        # Report Headers
        report_headers = report.headers
        # gET Filename
        filename = report_headers['Content-Disposition'].split('filename=')[1]
        # remove spaces and replace with underscore
        filename = filename.replace(' ', '_').replace('"', '')
        print(dir(report))
        with open(str(f'repos/csvs/{filename}'), 'wb') as f:
            f.write(report.content)
        # convert to excel
        df = pd.read_csv(f'repos/csvs/{filename}')
        df.to_excel(f'repos/excels/{str(filename)}.xlsx', index=False)
        break
        # return filename
    return filename

# function to download html report
def download_html_report(scan_id):
    # get the file ids
    file_ids = httpx.post(f'{base_url}{scan_id}/export',
                            headers=headers, verify=False, json={"format": "html", "template_id": "919"})
    print(json.dumps(file_ids.json(), indent=4, sort_keys=True))
    file_id = file_ids.json()['file']
    print(file_id)

    # wait for file to be generated loop
    while True:
        status = httpx.get(f'{base_url}{scan_id}/export/{file_id}/status',
                        headers=headers, verify=False)
        print(json.dumps(status.json(), indent=4, sort_keys=True))
        if status.json()['status'] == 'running':
            continue
        if status.json()['status'] == 'error':
            print('Error generating report')
            break
        if status.json()['status'] == 'ready':
            # download file
            report = httpx.get(
                f'{base_url}{scan_id}/export/{file_id}/download', headers=headers, verify=False)
            # Report Headers
            report_headers = report.headers
            # gET Filename
            filename = report_headers['Content-Disposition'].split('filename=')[1]
            # remove spaces and replace with underscore
            filename = filename.replace(' ', '_').replace('"', '')
            print(dir(report))
            with open(str(f'repos/htmls/{filename}'), 'wb') as f:
                f.write(report.content)
            break


print(download_csv_report(124))
