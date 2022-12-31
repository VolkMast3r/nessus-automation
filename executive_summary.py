import csv, os
import json
import matplotlib.pyplot as plt
from docxtpl import DocxTemplate, InlineImage
from docx import Document
from docx.shared import Inches
from utils import risk_analysis, vuln_analysis, open_ports
import httpx 
from dotenv import load_dotenv
import docx2pdf


# Get API keys from .env file  in the current directory
env_path = os.path.join(os.path.dirname(__file__), '../.env')
load_dotenv(env_path)
base_url = os.environ.get('base_url')
print(base_url)
headers = json.loads(os.environ.get('headers'))
print(headers)
# from config.config import get_platcorp_subs

scan_id = '121'
# initialize the document
document = DocxTemplate(
    'word_reports/activity_log.docx')

risks = risk_analysis.risk_percent_count(scan_id)
print(risks)

# define the colors High = red, Medium = yellow, Low = green, critical = purple
colors = ['red', 'Orange', 'green', 'purple']
# define the labels
labels = ['High', 'Medium', 'Low', 'Critical']

# find out mIssing keys
for key in ['High', 'Medium', 'Low', 'Critical']:
    if key not in risks:
        risks[key] = 0
        print(f'{key} not in risks')

# define the values
values = [risks['High'], risks['Medium'], risks['Low'], risks['Critical']]
# define the explode
explode = (0, 0, 0, 0.1)

# plot the pie chart
plt.pie(values, labels=labels, colors=colors, explode=explode, autopct='%1.1f%%', shadow=True, startangle=90)
plt.axis('equal')
plt.title('Risk Breakdown')
plt.savefig('word_reports/risk_breakdown.png')

imagen = InlineImage(document, 'word_reports/risk_breakdown.png', width=Inches(5))

risk_summary = f'The breakdown of the vulnerabilities is as follows: Critical Vulnerabilities account for {risks["Critical"]}% of the total vulnerabilities, \
High severity vulnerabilities account for {risks["High"]}% of the total vulnerabilities, \
Medium severity vulnerabilities account for {risks["Medium"]}% of the total vulnerabilities, \
Low severity vulnerabilities account for {risks["Low"]}% of the total vulnerabilities. \
Highest risk is {max(risks, key=risks.get)} '

risks_host = risk_analysis.host_risk_count_combined(scan_id)

host_risk_summary = f'The host with the highest risk is {max(risks_host, key=risks_host.get)} with {risks_host[max(risks_host, key=risks_host.get)]} vulnerabilities,\
which accounts for {round((risks_host[max(risks_host, key=risks_host.get)] / sum(risks_host.values())) * 100, 2)}% of the total vulnerabilities.\
The Top 5 hosts with the most vulnerabilities are: {list(risks_host.keys())[:5]} with {list(risks_host.values())[:5]} vulnerabilities \
which accounts for {round((sum(list(risks_host.values())[:5]) / sum(risks_host.values())) * 100, 2)}% of the total vulnerabilities respectively.\
'
name_synopsis = vuln_analysis.name_synopsis(scan_id)

top_vuln_summary = f'The most common vulnerability is {list(name_synopsis.keys())[0]} with {list(name_synopsis.values())[0]["count"]} occurences \
and a risk of {list(name_synopsis.values())[0]["risk"]}. Its solution is to {list(name_synopsis.values())[0]["Solution"]}\
The second most common vulnerability is {list(name_synopsis.keys())[1]} with {list(name_synopsis.values())[1]["count"]} occurences \
and a risk of {list(name_synopsis.values())[1]["risk"]}. Its solution is to {list(name_synopsis.values())[1]["Solution"]}\
The third most common vulnerability is {list(name_synopsis.keys())[2]} with {list(name_synopsis.values())[2]["count"]} occurences'


risk_synopsis = vuln_analysis.risk_synopsis(scan_id)

critical_synopsis = f'The most common vulnerability is {list(risk_synopsis.keys())[0]} with {list(risk_synopsis.values())[0]["count"]} occurences\
and a risk of {list(risk_synopsis.values())[0]["risk"]}. Its solution is to {list(risk_synopsis.values())[0]["Solution"]}\
The Second most common vulnerability is {list(risk_synopsis.keys())[1]} with {list(risk_synopsis.values())[1]["count"]} occurences\
and a risk of {list(risk_synopsis.values())[1]["risk"]}. Its solution is to {list(risk_synopsis.values())[1]["Solution"]}\
The Third most common vulnerability is {list(risk_synopsis.keys())[2]} with {list(risk_synopsis.values())[2]["count"]} occurences \
and a risk of {list(risk_synopsis.values())[2]["risk"]}. Its solution is to {list(risk_synopsis.values())[2]["Solution"]} '

conn = httpx.get(f'{base_url}{scan_id}', headers=headers, verify=False)
# print(conn.json())
open_ports = open_ports.port_count(333)
port_account = f'The most common open port is {list(open_ports.keys())[0]} with a unique count of {list(open_ports.values())[0]} \
and a total count of {sum(open_ports.values())}. The second most common open port is {list(open_ports.keys())[1]} with a unique count of {list(open_ports.values())[1]} \
and a total count of {sum(open_ports.values())}. The third most common open port is {list(open_ports.keys())[2]} with a unique count of {list(open_ports.values())[2]} \
and a total count of {sum(open_ports.values())}.'

context = {"risk_summary": risk_summary, "host_risk_summary": host_risk_summary,
           "risk_breakdown": imagen, "name_synopsis": top_vuln_summary, "critical_synopsis": critical_synopsis, "conn": conn.json(), "port_account": port_account}
document.render(context)
document.save('word_reports/output.docx')

