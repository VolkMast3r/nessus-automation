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


data = load_csv('repos/csvs/Momentum_Credit_Internal_egy66a.csv')


# wrap with a class
class Analyze_synopsis:
    def __init__(self, data):
        self.data = data
        self.synopsis = {}
        self.synopsis_hosts = {}
        self.host_synopsis = {}
        self.host = {}
        self.host_synopsis = {}
        self.synopsis = self.synopsis_count()
        self.synopsis_hosts = self.synopsis_hosts_list()
        self.host_synopsis = self.host_synopsis_list()
        self.host = self.host_count()
        self.host_synopsis = self.host_synopsis_list()

    def synopsis_count(self):
        '''
        output is like this:
        {'The remote host is missing a security patch': 1}
        '''
        synopsis = {}
        for row in self.data:
            if row['Synopsis'] in synopsis:
                synopsis[row['Synopsis']] += 1
            else:
                synopsis[row['Synopsis']] = 1
        return dict(sorted(synopsis.items(), key=lambda item: item[1], reverse=True))

    def synopsis_hosts_list(self):
        '''
        output is like this:
        {'The remote host is missing a security patch': ['
        }
        '''
        synopsis_hosts = {}
        for row in self.data:
            if row['Synopsis'] in synopsis_hosts:
                synopsis_hosts[row['Synopsis']].append(row['Host'])
            else:
                synopsis_hosts[row['Synopsis']] = [row['Host']]
        for key in synopsis_hosts:
            synopsis_hosts[key] = list(set(synopsis_hosts[key]))
        return synopsis_hosts

    def host_count(self):
        '''
        output is like this
        {'
        '''

        host = {}
        for row in self.data:
            if row['Host'] in host:
                host[row['Host']] += 1
            else:
                host[row['Host']] = 1
        return host

    def host_synopsis_list(self):
        '''
        output is like this:
        {'
        '''

        host_synopsis = {}
        for row in self.data:
            if row['Host'] in host_synopsis:
                host_synopsis[row['Host']].append(row['Synopsis'])
            else:
                host_synopsis[row['Host']] = [row['Synopsis']]
        for key in host_synopsis:
            host_synopsis[key] = list(set(host_synopsis[key]))
        return host_synopsis


# Create an instance of the class
analyze = Analyze_synopsis(data)

# Class attributes to JSON
with open('synopsis.json', 'w') as f:
    json.dump(analyze.synopsis, f, indent=4)


class Analyze_solution:
    def __init__(self, data):
        self.data = data
        self.solution = {}
        self.solution_hosts = {}
        self.host_solution = {}
        self.host = {}
        self.host_solution = {}
        self.solution = self.solution_count()
        self.solution_hosts = self.solution_hosts_list()
        self.host_solution = self.host_solution_list()
        self.host = self.host_count()
        self.host_solution = self.host_solution_list()

    def solution_count(self):
        ''' Get the count of each solution 
        output is like this:
        {'The remote host is missing a security patch': 1}
        '''
        solution = {}
        for row in self.data:
            if row['Solution'] in solution:
                solution[row['Solution']] += 1
            else:
                solution[row['Solution']] = 1
        return dict(sorted(solution.items(), key=lambda item: item[1], reverse=True))

    def solution_hosts_list(self):
        ''' Get the list of hosts for each solution
        output is like this:
        {'The remote host is missing a security patch': ['192.168.1.1', '10.0.1.5']}
        '''
        solution_hosts = {}
        for row in self.data:
            if row['Solution'] in solution_hosts:
                solution_hosts[row['Solution']].append(row['Host'])
            else:
                solution_hosts[row['Solution']] = [row['Host']]
        for key in solution_hosts:
            solution_hosts[key] = list(set(solution_hosts[key]))
        return solution_hosts

    def host_count(self):
        ''' Get the count of each host \n
        output is like this: {'192.168.10.1': 1}
        '''
        host = {}
        for row in self.data:
            if row['Host'] in host:
                host[row['Host']] += 1
            else:
                host[row['Host']] = 1
        return host

    def host_solution_list(self):
        host_solution = {}
        for row in self.data:
            if row['Host'] in host_solution:
                host_solution[row['Host']].append(row['Solution'])
            else:
                host_solution[row['Host']] = [row['Solution']]
        for key in host_solution:
            host_solution[key] = list(set(host_solution[key]))
        return host_solution

# instance of the class
analyze_synopsis = Analyze_solution(data)

# print top solutions and hosts
# for key in analyze.solution:
#     print(key, analyze.solution[key], analyze.solution_hosts[key])

class Analyze_Risks:
    def __init__(self, data):
        self.data = data
        self.risk = {}
        self.risk_hosts = {}
        self.host_risk = {}
        self.host = {}
        self.host_risk = {}
        self.risk = self.risk_count()
        self.risk_hosts = self.risk_hosts_list()
        self.host_risk = self.host_risk_list()
        self.host = self.host_count()
        self.host_risk = self.host_risk_list()

    def risk_count(self):
        '''
        Count the number of risks \n
        output is like this: {'Medium': 1, 'Critical': 1}
        '''
        risk = {}
        for row in self.data:
            if row['Risk'] in risk:
                risk[row['Risk']] += 1
            else:
                risk[row['Risk']] = 1
        return dict(sorted(risk.items(), key=lambda item: item[1], reverse=True))

    def risk_hosts_list(self):
        '''
        Get the list of hosts for each risk \n
        output is like this: {'Medium': ['192.168.1.2'], 'Critical': ['172.16.200.4']}
        '''
        risk_hosts = {}
        for row in self.data:
            if row['Risk'] in risk_hosts:
                risk_hosts[row['Risk']].append(row['Host'])
            else:
                risk_hosts[row['Risk']] = [row['Host']]
        for key in risk_hosts:
            risk_hosts[key] = list(set(risk_hosts[key]))
        return risk_hosts

    def host_count(self):
        ''' 
        Count the number of hosts \n
        output is like this: {'192.168.0.1': 1}
        '''
        host = {}
        for row in self.data:
            if row['Host'] in host:
                host[row['Host']] += 1
            else:
                host[row['Host']] = 1
        return host

    def host_risk_list(self):
        host_risk = {}
        for row in self.data:
            if row['Host'] in host_risk:
                host_risk[row['Host']].append(row['Risk'])
            else:
                host_risk[row['Host']] = [row['Risk']]
        for key in host_risk:
            host_risk[key] = list(set(host_risk[key]))
        return host_risk

class Analyze_Hosts:
    def __init__(self, data):
        self.data = data
        self.host = {}
        self.host_risk = {}
        self.host_synopsis = {}
        self.host_solution = {}
        self.host = self.host_count()
        self.host_risk = self.host_risk_list()
        self.host_synopsis = self.host_synopsis_list()
        self.host_solution = self.host_solution_list()

    def host_count(self):
        '''
        output is like {'host1': 3, 'host2': 2} 
        '''
        host = {}
        for row in self.data:
            if row['Host'] in host:
                host[row['Host']] += 1
            else:
                host[row['Host']] = 1
        return host

    def host_risk_list(self):
        '''
        # output is like this: {'host 1': ['risk 1', 'risk 2'], 'host 2': ['risk 1', 'risk 2']}
        '''
        host_risk = {}
        for row in self.data:
            if row['Host'] in host_risk:
                host_risk[row['Host']].append(row['Risk'])
            else:
                host_risk[row['Host']] = [row['Risk']]
        for key in host_risk:
            host_risk[key] = list(set(host_risk[key]))
        return host_risk

    def host_synopsis_list(self):
        '''
        # output is like this: {'host 1': ['synopsis 1', 'synopsis 2'], 'host 2': ['synopsis 1', 'synopsis 2']}
        '''
        host_synopsis = {}
        for row in self.data:
            if row['Host'] in host_synopsis:
                host_synopsis[row['Host']].append(row['Synopsis'])
            else:
                host_synopsis[row['Host']] = [row['Synopsis']]
        for key in host_synopsis:
            host_synopsis[key] = list(set(host_synopsis[key]))
        return host_synopsis

    def host_solution_list(self):
        '''
        # output is like this: {'host 1': ['solution 1', 'solution 2'], 'host 2': ['solution 1', 'solution 2']}
        '''
        host_solution = {}
        for row in self.data:
            if row['Host'] in host_solution:
                host_solution[row['Host']].append(row['Solution'])
            else:
                host_solution[row['Host']] = [row['Solution']]
        for key in host_solution:
            host_solution[key] = list(set(host_solution[key]))
        return host_solution

# initialize the class
analyze_hosts = Analyze_Hosts(data)
