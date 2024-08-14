import subprocess
import requests
import re

def parse_iwgetid_output(ssid:str) -> list:
    data = ssid.strip().split(maxsplit=1)
    data = [item.strip() for item in data]
    return data


def process_iwgetid_data():
    try:
        output = subprocess.run(['iwgetid'],capture_output=True)
    except FileNotFoundError:
        print("iwgetid not installed on system")
        return None
    
    if output.returncode != 0:
        print("Something went wrong")
        return None
    
    ssid_data = parse_iwgetid_output(output.stdout)
    ssid_id = ssid_data[0]
    ssid_name = ssid_data[1]

    ssid_id = ssid_id.decode('utf-8')
    ssid_name = ssid_name.decode('utf-8')
    ssid_name = ssid_name.split(':')[1].replace('"','').strip()

    return {
        "ssid_id":ssid_id,
        "ssid_name":ssid_name
    }

def is_ssid_connected(name:str) -> bool:
    data = process_iwgetid_data()
    if data is None:
        return False
    
    if name == data['ssid_name']:
        return True
    else:
        return False

def is_logged_in() -> bool:
    r = requests.get("http://neverssl.com")
    exp = "https:\/\/(.*)\/fgtauth\?"
    regexp = re.compile(exp)
    if regexp.search(r.text):
        return False
    else:
        return True


def get_captive_portal_address() -> str:
    r = requests.get("http://neverssl.com")
    exp = "https:\/\/(.*)\/fgtauth\?.*\""
    regexp = re.compile(exp)

    result = regexp.search(r.text)
    if result:
        return result.group(0).replace('"','')
