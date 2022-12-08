import csv
import json
import matplotlib.pyplot as plt
from docxtpl import DocxTemplate, InlineImage
from docx import Document
from docx.shared import Inches
from utils import risk_analysis, vuln_analysis

# initialize the document
document = DocxTemplate('word_reports/activity_log.docx')

risks = risk_analysis.risk_percent_count()

# define the colors High = red, Medium = yellow, Low = green, critical = purple
colors = ['red', 'Orange', 'green', 'purple']
# define the labels
labels = ['High', 'Medium', 'Low', 'Critical']
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
High Vulnerabilities account for {risks["High"]}% of the total vulnerabilities, \
Medium Vulnerabilities account for {risks["Medium"]}% of the total vulnerabilities, \
Low Vulnerabilities account for {risks["Low"]}% of the total vulnerabilities. \
\nHighest risk is {max(risks, key=risks.get)} '

risks_host = risk_analysis.host_risk_count_combined()

host_risk_summary = f'The host with the highest risk is {max(risks_host, key=risks_host.get)} with {risks_host[max(risks_host, key=risks_host.get)]} vulnerabilities,\
which accounts for {round((risks_host[max(risks_host, key=risks_host.get)] / sum(risks_host.values())) * 100, 2)}% of the total vulnerabilities.\
\nThe Top 5 hosts with the most vulnerabilities are: {list(risks_host.keys())[:5]} with {list(risks_host.values())[:5]} vulnerabilities \
which accounts for {round((sum(list(risks_host.values())[:5]) / sum(risks_host.values())) * 100, 2)}% of the total vulnerabilities respectively.\
'
name_synopsis = vuln_analysis.name_synopsis()

top_vuln_summary = f'The most common vulnerability is {list(name_synopsis.keys())[0]} with {list(name_synopsis.values())[0]["count"]} occurences \
and a risk of {list(name_synopsis.values())[0]["risk"]}. Its solution is to {list(name_synopsis.values())[0]["Solution"]}\
\nThe second most common vulnerability is {list(name_synopsis.keys())[1]} with {list(name_synopsis.values())[1]["count"]} occurences \
and a risk of {list(name_synopsis.values())[1]["risk"]}. Its solution is to {list(name_synopsis.values())[1]["Solution"]}\
\nThe third most common vulnerability is {list(name_synopsis.keys())[2]} with {list(name_synopsis.values())[2]["count"]} occurences'


risk_synopsis = vuln_analysis.risk_synopsis()

critical_synopsis = f'The vulnerability with Critical risk is {list(risk_synopsis.keys())[0]} with {list(risk_synopsis.values())[0]["count"]} occurences\
and a risk of {list(risk_synopsis.values())[0]["risk"]}. Its solution is to {list(risk_synopsis.values())[0]["Solution"]}\
    \nThe Second Highest Critical vulnerability is {list(risk_synopsis.keys())[1]} with {list(risk_synopsis.values())[1]["count"]} occurences\
    and a risk of {list(risk_synopsis.values())[1]["risk"]}. Its solution is to {list(risk_synopsis.values())[1]["Solution"]}\
    \nThe Third Highest Critical vulnerability is {list(risk_synopsis.keys())[2]} with {list(risk_synopsis.values())[2]["count"]} occurences \
    and a risk of {list(risk_synopsis.values())[2]["risk"]}. Its solution is to {list(risk_synopsis.values())[2]["Solution"]} '

context = {"risk_summary": risk_summary, "host_risk_summary": host_risk_summary,
           "risk_breakdown": imagen, "name_synopsis": top_vuln_summary, "critical_synopsis": critical_synopsis}
document.render(context)
document.save('word_reports/output.docx')


