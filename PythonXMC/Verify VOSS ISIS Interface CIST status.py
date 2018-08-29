# @METADATASTART
#@DetailDescriptionStart
################################################################
# System Script
#
# Script        : Return CIST status on ISIS enabled ports of selected VOSS device(s)
# Revision      : 1.0
# Last updated  : 29/8/2018
# Purpose       : Return CIST status on ISIS enabled ports of selected VOSS device(s)
#
# Summary:
#      1. List ISIS active interfaces
#      2. Verify and print CIST status of ISIS enabled ports
#
################################################################
#@DetailDescriptionEnd

# @ScriptDescription "CIST status on ISIS enabled ports of VOSS devices"
# @SectionStart ( description = "No Setup Required")
# @SectionEnd
# @MetaDataEnd

import re

#List up ISIS enabled and active ports. Return a list of dictionary containing keys, SLOT and PORT
def list_isis_enabled_ports():
    cli_results1 = emc_cli.send('show isis interface').getOutput()
    re_pattern_str = r"Port(?P<{}>\d+)/(?P<{}>\d+)".format("SLOT","PORT")
    re_pattern = re.compile(re_pattern_str)
    match_groups = re_pattern.finditer(cli_results1)
    nni_ports = []
    for group in match_groups:
        nni_ports.append(group.groupdict())
    return nni_ports

#Verify CIST status of a port. Return a value for a key, STATUS
def verify_NNI_MSTP_conf(slot,port):
    cli_results2 = emc_cli.send('show spanning-tree mstp port config '+slot+'/'+port).getOutput()
    re_pattern_str = r"Cist\sPort\sforce-port-state\s+:\s(?P<{}>\w+)".format("STATUS")
    re_pattern = re.compile(re_pattern_str)
    match_groups = re_pattern.finditer(cli_results2)
    return match_groups.next().group("STATUS")

#Call functions and print port status
def main():
    plist = list_isis_enabled_ports()
    for port in plist:
        port["STATUS"] = verify_NNI_MSTP_conf(port["SLOT"], port["PORT"])
    for port in plist:
        print ("Port {}/{} is an NNI port".format(port.get("SLOT"),port.get("PORT")))
        print ("Cist on port {}/{} is {}d\n".format(port.get("SLOT"),port.get("PORT"),port.get("STATUS")))

if __name__ == '__builtin__':
    main()
