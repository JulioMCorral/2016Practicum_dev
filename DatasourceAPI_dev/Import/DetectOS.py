import platform
import sys
import os

print platform.platform()
# print platform.system()

myOS = platform.platform()

if myOS.startswith("Linux"):
	os.system('./kali_mongoImport.sh')
elif myOS.startswith("Windows"):
	os.system('windows_mongoImport.sh')