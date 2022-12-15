import csv
from utils.csv_downloader import download_csv_report

def load_csv(csv_file):
    with open(csv_file, 'r') as f:
        reader = csv.DictReader(f)
        data = list(reader)
        data = [row for row in data if row['Risk'] != 'None']
        return data

def risk_count(scan_id):
    '''
    Count the number of risks\n
    :param data: list of dicts\n
    :return: dict of risks and their counts like\n
    {'High': 2, 'Medium': 1, 'Low': 1}
    '''
    file_name = download_csv_report(f'{scan_id}')
    data = load_csv(f'repos/csvs/{file_name}')
    risk = {}
    for row in data:
        if row['Risk'] in risk:
            risk[row['Risk']] += 1
        else:
            risk[row['Risk']] = 1
    return risk


def risk_percent_count(scan_id):
    '''
    Count the number of risks\n
    :param data: list of dicts\n
    :return: dict of risks and their percentages like\n
    {'High': 50.0, 'Medium': 25.0, 'Low': 25.0}
    '''
    file_name = download_csv_report(f'{scan_id}')
    data = load_csv(f'repos/csvs/{file_name}')
    risk = {}
    for row in data:
        if row['Risk'] in risk:
            risk[row['Risk']] += 1
        else:
            risk[row['Risk']] = 1
    total = sum(risk.values())
    for key in risk:
        risk[key] = round((risk[key] / total) * 100, 2)
    return risk


def host_risk_count(scan_id):
    '''
    Count the number of risks per host\n
    :param data: list of dicts\n
    :return: dict of hosts and their risks like\n
    {'192.168.1.2': {'High': 2, 'Medium': 1, 'Low': 1}}
    '''
    file_name = download_csv_report(f'{scan_id}')
    data = load_csv(f'repos/csvs/{file_name}')
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


def host_risk_count_combined(scan_id):
    '''
    Count the number of risks per host\n
    :param data: list of dicts\n
    :return: dict of hosts and their risks like\n
    {'192.168.1.1': 4, '192.168.1.2': 4}
    '''
    file_name = download_csv_report(f'{scan_id}')
    data = load_csv(f'repos/csvs/{file_name}')
    host_risk = {}
    for row in data:
        if row['Host'] in host_risk:
            host_risk[row['Host']] += 1
        else:
            host_risk[row['Host']] = 1
    return host_risk


# print(host_risk_count_combined('139'))