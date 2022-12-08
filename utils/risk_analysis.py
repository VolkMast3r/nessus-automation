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



# corelate Risk with Hosts
def risk_count():
    '''
    Count the number of risks\n
    :param data: list of dicts\n
    :return: dict of risks and their counts like\n
    {'High': 2, 'Medium': 1, 'Low': 1}
    '''
    data = load_csv('repos/csvs/Momentum_Credit_Internal_egy66a.csv')
    risk = {}
    for row in data:
        if row['Risk'] in risk:
            risk[row['Risk']] += 1
        else:
            risk[row['Risk']] = 1
    return risk


def risk_percent_count():
    '''
    Count the number of risks\n
    :param data: list of dicts\n
    :return: dict of risks and their percentages like\n
    {'High': 50.0, 'Medium': 25.0, 'Low': 25.0}
    '''
    data = load_csv('repos/csvs/Momentum_Credit_Internal_egy66a.csv')
    risk = {}
    for row in data:
        if row['Risk'] in risk:
            risk[row['Risk']] += 1
        else:
            risk[row['Risk']] = 1
    # calculate the percentage of each risk
    total = sum(risk.values())
    for key in risk:
        risk[key] = round((risk[key] / total) * 100, 2)
    return risk


# Host with breakdown of risks
def host_risk_count():
    '''
    Count the number of risks per host\n
    :param data: list of dicts\n
    :return: dict of hosts and their risks like\n
    {'192.168.1.2': {'High': 2, 'Medium': 1, 'Low': 1}}
    '''
    data = load_csv('repos/csvs/Momentum_Credit_Internal_egy66a.csv')
    host_risk = {}
    for row in data:
        if row['Host'] in host_risk:
            if row['Risk'] in host_risk[row['Host']]:
                host_risk[row['Host']][row['Risk']] += 1
            else:
                host_risk[row['Host']][row['Risk']] = 1
        else:
            host_risk[row['Host']] = {row['Risk']: 1}
    return host_risk

# print(json.dumps(host_risk_count(data), indent=4))

# Combined Risk count per host
def host_risk_count_combined():
    '''
    Count the number of risks per host\n
    :param data: list of dicts\n
    :return: dict of hosts and their risks like\n
    {'192.168.1.1': 4, '192.168.1.2': 4}
    '''
    data = load_csv('repos/csvs/Momentum_Credit_Internal_egy66a.csv')
    host_risk = {}
    for row in data:
        if row['Host'] in host_risk:
            host_risk[row['Host']] += 1
        else:
            host_risk[row['Host']] = 1
    # sort the dict by value
#     host_risk = dict(sorted(host_risk.items(), key=lambda item: item[1], reverse=True))
#     print(f'The host with the most risks is {list(host_risk.keys())[0]} with {list(host_risk.values())[0]} risks \
#         and accounts for {round((list(host_risk.values())[0] / sum(host_risk.values())) * 100, 2)}% of the total risks')
#     print(f'The Top 5 hosts with the most risks are: {list(host_risk.keys())[:5]} with {list(host_risk.values())[:5]} risks \
#         and accounts for {round((sum(list(host_risk.values())[:5]) / sum(host_risk.values())) * 100, 2)}% of the total risks')
    return host_risk
# print(json.dumps(host_risk_count_combined(data), indent=4))

