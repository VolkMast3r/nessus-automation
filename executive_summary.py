import csv, os
import json
import matplotlib.pyplot as plt
from docxtpl import DocxTemplate, InlineImage
from docx import Document
from docx.shared import Inches
from utils import risk_analysis, vuln_analysis, open_ports, convert_docx_pdf, password_protect_pdf
import httpx
from dotenv import load_dotenv
# logging
import logging
# date
import datetime
import time

# Get API keys from .env file  in the current directory
env_path = os.path.join(os.path.dirname(__file__), '../.env')
load_dotenv(env_path)
base_url = os.environ.get('base_url')
# print(base_url)
headers = json.loads(os.environ.get('headers'))
logging.basicConfig(level=logging.DEBUG)
# print(headers)
# from config.config import get_platcorp_subs

scan_ids_dict = platcorp_subs = {
    "Eezy Track": "142",
    "Premier Credit Uganda": "127",
    "Platcorp Holdings": "148",
    "Momentum Credit":  "139",
    "Premier Credit Kenya": "136",
    "Platinum Credit Tanzania": "130",
    "Viva 365 Insurance Brokers": "145",
    "Platinum Credit Kenya": "121",
    "Fanikiwa Microfinance Limited": "133",
    "Platinum Credit Uganda": "124"
}

for sub_key, scan_id in scan_ids_dict.items():
    # log info with blue color to cmdline
    logging.info(f'Generating report for {sub_key}')
    # initialize the document
    document = DocxTemplate(
        'word_reports/activity_log.docx')

    risks = risk_analysis.risk_percent_count(scan_id)
    # print(risks)

    # define the colors High = red, Medium = yellow, Low = green, critical = purple
    colors = ['purple', 'red', 'Orange', 'green']
    # define the labels
    labels = ['Critical', 'High', 'Medium', 'Low']
    # find out mIssing keys
    for key in ['Critical', 'High', 'Medium', 'Low']:
        if key not in risks:
            risks[key] = 0
            # domt show missing keys
            labels[labels.index(key)] = ''
            print(f'{key} not in risks')

    # define the values
    values = [risks['Critical'], risks['High'], risks['Medium'], risks['Low']]
    # define the explode
    # explode = (0, 0, 0, 0)
 
    # plot the pie chart
    plt.pie(values, labels=None, colors=colors, explode=None, shadow=False, startangle=90)
    # Legend with the labels % values
    plt.legend(labels=[f'{l} - {v}%' for l, v in zip(labels, values)], loc="best")
    plt.axis('equal')
    plt.title('Risk Breakdown')
    plt.savefig(f'images/{sub_key}_risk_breakdown.png')

    imagen = InlineImage(
        document, f'images/{sub_key}_risk_breakdown.png', width=Inches(5))

    risk_summary =  f'The breakdown of the vulnerabilities is as follows:\n- Critical Vulnerabilities account for {risks["Critical"]}% of the total vulnerabilities, \n- High severity vulnerabilities account for {risks["High"]}% of the total vulnerabilities, \n- Medium severity vulnerabilities account for {risks["Medium"]}% of the total vulnerabilities, \n- Low severity vulnerabilities account for {risks["Low"]}% of the total vulnerabilities. \n\nHighest risk is {max(risks, key=risks.get)} '

    risks_host = risk_analysis.host_risk_count_combined(scan_id)

    host_risk_summary = f'The host with the highest risk is {max(risks_host, key=risks_host.get)} with {risks_host[max(risks_host, key=risks_host.get)]} vulnerabilities, which accounts for {round((risks_host[max(risks_host, key=risks_host.get)] / sum(risks_host.values())) * 100, 2)}% of the total vulnerabilities.\n\nThe Top 5 hosts with the most vulnerabilities are: {list(risks_host.keys())[:5]} with {list(risks_host.values())[:5]} vulnerabilities which accounts for {round((sum(list(risks_host.values())[:5]) / sum(risks_host.values())) * 100, 2)}% of the total vulnerabilities respectively.'
    name_synopsis = vuln_analysis.name_synopsis(scan_id)
    top_vuln_summary = f'The most common vulnerability is {list(name_synopsis.keys())[0]} with {list(name_synopsis.values())[0]["count"]} occurences and a risk of {list(name_synopsis.values())[0]["risk"]}. Its solution is to {list(name_synopsis.values())[0]["Solution"]}\n\nThe second most common vulnerability is {list(name_synopsis.keys())[1]} with {list(name_synopsis.values())[1]["count"]} occurences and a risk of {list(name_synopsis.values())[1]["risk"]}. Its solution is to {list(name_synopsis.values())[1]["Solution"]}\n\nThe third most common vulnerability is {list(name_synopsis.keys())[2]} with {list(name_synopsis.values())[2]["count"]} occurences'
    risk_synopsis = vuln_analysis.risk_synopsis(scan_id)
    critical_synopsis = f'The most common vulnerability is {list(risk_synopsis.keys())[0]} with {list(risk_synopsis.values())[0]["count"]} occurences and a risk of {list(risk_synopsis.values())[0]["risk"]}. Its solution is to {list(risk_synopsis.values())[0]["Solution"]} The Second most common vulnerability is {list(risk_synopsis.keys())[1]} with {list(risk_synopsis.values())[1]["count"]} occurences and a risk of {list(risk_synopsis.values())[1]["risk"]}. Its solution is to {list(risk_synopsis.values())[1]["Solution"]} The Third most common vulnerability is {list(risk_synopsis.keys())[2]} with {list(risk_synopsis.values())[2]["count"]} occurences and a risk of {list(risk_synopsis.values())[2]["risk"]}. Its solution is to {list(risk_synopsis.values())[2]["Solution"]}'
    conn = httpx.get(f'{base_url}{scan_id}', headers=headers, verify=False)
    # replace empty dictionary values with None
    conn.json().update((x, None) for x, y in conn.json().items() if y == {})

    # print(conn.json())
    # open_ports = open_ports.port_count(scan_id)
    # port_account = f'The most common open port is {list(open_ports.keys())[0]} with a unique count of {list(open_ports.values())[0]} \
    # and a total count of {sum(open_ports.values())}. The second most common open port is {list(open_ports.keys())[1]} with a unique count of {list(open_ports.values())[1]} \
    # and a total count of {sum(open_ports.values())}. The third most common open port is {list(open_ports.keys())[2]} with a unique count of {list(open_ports.values())[2]} \
    # and a total count of {sum(open_ports.values())}.'

    today = datetime.datetime.now().date()
    # Format the date as a string
    date_str = today.strftime("%d/%m/%Y")
    this_month = today.strftime("%B %Y")
    filename = conn.json()['info']['name'].replace(' ', '_')
    context = {"risk_summary": risk_summary, "host_risk_summary": host_risk_summary,
            "date": date_str,
            "month": this_month,
            "filename": f'{filename}.pdf',
            "risk_breakdown": imagen, "name_synopsis": top_vuln_summary, "critical_synopsis": critical_synopsis, "conn": conn.json()}
    document.render(context)

    # convert the docx to pdf using convert_docx_pdf
    filename = conn.json()['info']['name'].replace(' ', '_')
    document.save(f'word_reports/{filename}.docx')
    convert_docx_pdf.convert_docx_to_pdf(f'{filename}.docx')
    # password protect the pdf
    password_protect_pdf.password_protect_pdf_linux(f'{filename}.pdf')

    print(f'Word report for {filename} has been generated')
    


