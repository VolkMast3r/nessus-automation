import csv
import json
import matplotlib.pyplot as plt
import os

# Read CSV file Authenticated_Scans_pxo3q6.csv to a dict

def load_csv(csv_file):
    with open(csv_file, 'r') as f:
        # Read the file
        reader = csv.DictReader(f)
        # Create a list of dicts
        data = list(reader)
        # drop Risk = None
        data = [row for row in data if row['Risk'] != 'None']
        return data

# corelate Name and Synopsis
def name_synopsis():
    data = load_csv('repos/csvs/Momentum_Credit_Internal_egy66a.csv')
    # print like this: {name:{ "synopsis": synopsis, "count": count, "risk": risk, "Solution": solution,}}
    name_synopsis = {}
    for row in data:
        if row['Name'] in name_synopsis:
            name_synopsis[row['Name']]['count'] += 1
        else:
            name_synopsis[row['Name']] = {
                "synopsis": row['Synopsis'],
                "count": 1,
                "risk": row['Risk'],
                "Solution": row['Solution'],
            }
    # sort by count in descending order
    name_synopsis = dict(sorted(name_synopsis.items(), key=lambda item: item[1]['count'], reverse=True))

    # Sort by Risk From Critical to Low
    risk_synopsis = dict(sorted(name_synopsis.items(), key=lambda item: item[1]['risk'], reverse=False))

#     print(f'The most common vulnerability is {list(name_synopsis.keys())[0]} with {list(name_synopsis.values())[0]["count"]} occurences\
# and a risk of {list(name_synopsis.values())[0]["risk"]}. Its solution is to {list(name_synopsis.values())[0]["Solution"]}')
#     # second most common
#     print(f'The second most common vulnerability is {list(name_synopsis.keys())[1]} with {list(name_synopsis.values())[1]["count"]} occurences\
# and a risk of {list(name_synopsis.values())[1]["risk"]}. Its solution is to {list(name_synopsis.values())[1]["Solution"]}')
#     # third most common
#     print(f'The third most common vulnerability is {list(name_synopsis.keys())[2]} with {list(name_synopsis.values())[2]["count"]} occurences\
# and a risk of {list(name_synopsis.values())[2]["risk"]}. Its solution is to {list(name_synopsis.values())[2]["Solution"]}')
#     print(f' The vulnerability with Critical risk is {list(risk_synopsis.keys())[0]} with {list(risk_synopsis.values())[0]["count"]} occurences\
#         and a risk of {list(risk_synopsis.values())[0]["risk"]}. Its solution is to {list(risk_synopsis.values())[0]["Solution"]}')
    return name_synopsis

# corelate Name and Synopsis


def risk_synopsis():
    data = load_csv('repos/csvs/Momentum_Credit_Internal_egy66a.csv')
    # print like this: {name:{ "synopsis": synopsis, "count": count, "risk": risk, "Solution": solution,}}
    name_synopsis = {}
    for row in data:
        if row['Name'] in name_synopsis:
            name_synopsis[row['Name']]['count'] += 1
        else:
            name_synopsis[row['Name']] = {
                "synopsis": row['Synopsis'],
                "count": 1,
                "risk": row['Risk'],
                "Solution": row['Solution'],
            }
    # sort by count in descending order
    name_synopsis = dict(sorted(name_synopsis.items(),
                         key=lambda item: item[1]['count'], reverse=True))

    # Sort by Risk From Critical to Low
    risk_synopsis = dict(sorted(name_synopsis.items(),
                         key=lambda item: item[1]['risk'], reverse=False))

#     print(f'The most common vulnerability is {list(name_synopsis.keys())[0]} with {list(name_synopsis.values())[0]["count"]} occurences\
# and a risk of {list(name_synopsis.values())[0]["risk"]}. Its solution is to {list(name_synopsis.values())[0]["Solution"]}')
#     # second most common
#     print(f'The second most common vulnerability is {list(name_synopsis.keys())[1]} with {list(name_synopsis.values())[1]["count"]} occurences\
# and a risk of {list(name_synopsis.values())[1]["risk"]}. Its solution is to {list(name_synopsis.values())[1]["Solution"]}')
#     # third most common
#     print(f'The third most common vulnerability is {list(name_synopsis.keys())[2]} with {list(name_synopsis.values())[2]["count"]} occurences\
# and a risk of {list(name_synopsis.values())[2]["risk"]}. Its solution is to {list(name_synopsis.values())[2]["Solution"]}')
#     print(f' The vulnerability with Critical risk is {list(risk_synopsis.keys())[0]} with {list(risk_synopsis.values())[0]["count"]} occurences\
#         and a risk of {list(risk_synopsis.values())[0]["risk"]}. Its solution is to {list(risk_synopsis.values())[0]["Solution"]}')
    return risk_synopsis

  