import csv
from utils.csv_downloader import download_csv_report
import os
import matplotlib.pyplot as plt
import numpy as np





def load_csv(csv_file):
    with open(csv_file, 'r') as f:
        reader = csv.DictReader(f)
        data = list(reader)
        data = [row for row in data if row['Port'] != '0']
        return data



# print(data)
# remove the file after we are done with it
def port_statistics(scan_id):
    '''
    Count the number of ports per host\n
    like {host: {ports: [port1, port2, port3], count: 3}}
    '''
    filename = download_csv_report(scan_id)
    data = load_csv(f'repos/csvs/{filename}')
    port_stats = {}
    for row in data:
        if row['Host'] in port_stats:
            port_stats[row['Host']]['ports'].append(row['Port'])
            port_stats[row['Host']]['count'] += 1
        else:
            port_stats[row['Host']] = {'ports': [row['Port']], 'count': 1}

    # os.remove(f'repos/csvs/{filename}')
    # sort
    port_stats = dict(
        sorted(
            port_stats.items(), key=lambda item: item[1]['count'], reverse=True
        )
    )
    return port_stats

def port_count(scan_id):
    '''
    Count the number of ports per host\n
    like {port: count}
    '''
    filename = download_csv_report(scan_id)
    data = load_csv(f'repos/csvs/{filename}')
    port_stats = {}
    for row in data:
        if row['Port'] in port_stats:
            port_stats[row['Port']] += 1
        else:
            port_stats[row['Port']] = 1
    os.remove(f'repos/csvs/{filename}')
    # sort
    port_stats = dict(
        sorted(port_stats.items(), key=lambda item: item[1], reverse=True)
    )
    return port_stats
