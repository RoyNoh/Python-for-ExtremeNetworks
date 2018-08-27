import re
import sys

def validate_mc_ip(arg):
    com = re.compile("^(22[4-9]|23[0-9]?)\."
    "((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){2}"
    "(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$")
    match = com.match(arg)
    try:
        return match.group(0)
    except:
        print('Input error. Please retry')
        sys.exit()

def convert_mc_ip_to_int(arg):
    str_ip = arg.split('.')
    int_ip = []
    for each in str_ip:
        int_ip.append(int(each))
    return int_ip

def compose_mc_mac(arg):
    base_mac = [0x01,0x00,0x5e]
    mc_mac = base_mac
    arg.pop(0)
    arg[0] = arg[0]%128
    for each in arg:
        mc_mac.append(each)
    print mc_mac
    return mc_mac

def print_hex_mc_mac(arg):
    list_mac = []
    for each in arg:
        list_mac.append('{:0>2}'.format(str(hex(each))[2:]))
#    print(list_mac)
#    v1 = '{0}:{1}:{2}:{3}:{4}:{5}'.format(list_mac[0],list_mac[1],list_mac[2],list_mac[3],list_mac[4],list_mac[5])
    v2 = ':'.join(list_mac)
#    print(v1)
    print(v2)

def run():
    print("Input an IPv4 mcast address")
    mc_ip = raw_input()
    valid_mc_ip = validate_mc_ip(mc_ip)
    int_ip = convert_mc_ip_to_int(valid_mc_ip)
    mc_int_mac = compose_mc_mac(int_ip)
    print_hex_mc_mac(mc_int_mac)

if __name__ == '__main__':
    run()
