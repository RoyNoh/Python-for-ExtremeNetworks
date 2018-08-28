import sys

def build_system_id(desc,loca,dev_num):
    system_id = "020"+desc+"."+"{:0>4}".format(loca)+"."+"{:0^4}".format(dev_num)
    return system_id
def build_nick_name(loca,dev_num):
    nick_name = loca[0]+"."+loca[1::]+'.'+dev_num
    return nick_name
def build_virtual_mac(self_sys_id,peer_sys_id):
    if self_sys_id < peer_sys_id:
        virtual_mac = self_sys_id[:-1]+'f'
        return virtual_mac
    elif self_sys_id > peer_sys_id:
        virtual_mac = peer_sys_id[:-1]+'f'
        return virtual_mac
    else:
        print "Both system ID have same value. Try again"
def main():
    print ("Select a description of the devices.\n"
    "b: Branch, c:Core, d:Distribution, e:Edge")
    desc = raw_input("Choose one from the above options\n").lower()

    print ("Insert a valid location number.\n"
    "Location number must be within 3 digits in hex value format")
    loca = raw_input().lower()
    loca = "{:0>3}".format(loca)

    print ("Insert a valid device number.\n"
    "Device number must be within 2 digits in hex value format")
    dev_num = raw_input().lower()
    dev_num= "{:0>2}".format(dev_num)

    print ("Insert the peer device device number.\n"
    "Device number must be within 2 digits in hex value format")
    pdev_num = raw_input().lower()
    pdev_num= "{:0>2}".format(pdev_num)

    self_sys_id = build_system_id(desc,loca,dev_num)
    self_nick_name = build_nick_name(loca,dev_num)
    peer_sys_id = build_system_id(desc,loca,pdev_num)
    peer_nick_name = build_nick_name(loca,pdev_num)
    virtual_mac = build_virtual_mac(self_sys_id,peer_sys_id)

    print ("System ID(self) : "+self_sys_id)
    print ("System ID(peer) : "+peer_sys_id)
    print ("Nick name(self) : "+self_nick_name)
    print ("Nicn name(peer) : "+peer_nick_name)
    print ("Virtula MAC : "+virtual_mac)

if __name__ == '__main__':
    main()
