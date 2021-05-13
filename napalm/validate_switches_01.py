from napalm import get_network_driver
import pprint as pp

driver = get_network_driver('eos')
device = driver('sw-1', 'admin', 'alta3')
device.open()
pp.pprint(device.compliance_report("/home/student/pyna/napalm/sw1_validate.yml"))
device.close()

