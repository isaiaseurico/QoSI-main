import requests
import json
import platform
import iperf3
from datetime import datetime
from icmplib import ping, exceptions

def get_targets():
    tkey = {"token_key":"Aeco9H382YPq"}
    try:
        x = requests.post('http://18.169.204.30:8888/targets', json = tkey)
        return json.loads(x.text)
    except Exception as ex:
        return False

def get_isp():
    try:
        req = requests.get('https://ipinfo.io')
        result = json.loads(req.text)
        return result['org']
    except Exception as err:
        print(err)
        
def get_date():
    return datetime.today().strftime("%d-%m-%Y")

def get_hour():
    return datetime.datetime.today().strftime("%H:%M")

def get_os():
    return platform.system()

def run_ping(target):
    results = {}
    try:
        test = ping(target, 5)
        results['latency'] = test.avg_rtt
        results['jitter'] = test.jitter
        results['packet_loss'] = test.packet_loss
    except exceptions.SocketPermissionError:
        print("Permissions error. You need to run as sudo")
        return
    return results

def run_iperf(target):
    results = {}
    try:
        client = iperf3.Client()
        client.server_hostname = target
        test = client.run()
        results['download'] = "{:.2f}".format(test.received_Mbps)
        results['upload'] = "{:.2f}".format(test.sent_Mbps)
    except Exception as err:
        print(err)
    return results

def send_results(data_dict):
    data_dict['token_key'] = 'Aeco9H382YPq'
    res = ''
    try:
        x = requests.post('http://18.169.204.30:8888/submit', json = data_dict)
        res = json.loads(x.text)
    except Exception as ex:
        return False
    if res:
        return True
    else:
        return False
