from napalm import get_network_driver # import code from NAPALM
driver = get_network_driver('eos') # get the driver for Arista devices
device = driver('sw-1', 'admin', 'alta3') # apply the switch credentials
device.open() # start the connection
#The next two lines of code are new
device.load_merge_candidate("/home/student/pyna/napalm/merge.me")
device.commit_config()

