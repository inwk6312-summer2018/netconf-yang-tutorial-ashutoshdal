from ncclient import manager
import sys
import xml.dom.minidom

HOST = '10.1.101.5'
PORT = 830
USER = 'cisco'
PASS = 'cisco'

def main():
	with manager.connect(host=HOST,port=PORT,username=USER,password=PASS,hostkey_verify=False,device_params={'name':'default'},look_for_keys=False,allow_agent=False) as m:
		print('***Here are the Remote Device Capabilities***')
		for capability in m.server_capabilities:
			print(capability.split('?')[0])

	hostname_filter = '''
		<filter>
			<native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
				<hostname></hostname>
			</native>
		</filter>
			'''
	result = m.get_config('running',hostname_filter)
	xml_doc = xml.dom.minidom.parseString(result.xml)
	hostname = xml_doc.getElementsByTagName("hostname")
	print(hostname[0].firstChild.nodeValue)

#if__name__=='__main__':
#	sys.exit(main())
main()
