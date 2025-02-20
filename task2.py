# pylint: disable = missing-module-docstring
# pylint: disable = no-name-in-module
# pylint: disable = missing-function-docstring

import json
import socket
import netifaces  # 修复：显式导入模块而非通配符
from netaddr import IPAddress

def get_ip_addresses():
    """
    Get a dictionary mapping network interface names to a list of their IPv4 addresses.
    """
    interface_to_ip = {}
    # 修复：使用 netifaces.interfaces()
    interface_list = netifaces.interfaces()
    # 修复：使用 netifaces.ifaddresses()
    address_entries = [netifaces.ifaddresses(iface) for iface in interface_list]

    # map the interface name to ip address
    for key, value in zip(interface_list, address_entries):
        interface_to_ip[key] = value

    # ipv4 address types
    ipv4_address_entries = {}
    for interface, address in interface_to_ip.items():
        # 修复：使用 socket.AF_INET
        if socket.AF_INET in address:  # Look for IPv4 entries
            ipv4_address_entries[interface] = interface_to_ip[interface][socket.AF_INET]
    return ipv4_address_entries

def get_netmask_readable(ip_info):
    """
    Convert the netmask to integer format.
    """
    netmask = ip_info['netmask']
    # 修复：移除危险的 eval，直接使用整数操作
    ip_info['netmask'] = IPAddress(netmask).netmask_bits()
    return ip_info

def check_localhost(ip_info):
    ip_addr = ip_info['addr']
    # 修复：使用 == 替代 is
    if ip_addr == "127.0.0.1":
        return True
    return False

if __name__ == "__main__":
    ip_addresses = get_ip_addresses()
    for intf, ip in ip_addresses.items():
        ip_addresses[intf] = get_netmask_readable(ip[0])
        ip_addresses[intf]['is_localhost'] = check_localhost(ip[0])

    # Print the result as JSON.
    print(json.dumps(ip_addresses, indent=4))
