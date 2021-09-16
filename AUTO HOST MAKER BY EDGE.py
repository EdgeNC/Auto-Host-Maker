import os

os.system("title Edge TOOLS AUTO HOST MAKER")
host="host.txt"
d = open(host, 'w')
IP = input("Input Your IP : ")
d.write(f"""{IP} growtopia1.com
{IP} growtopia2.com""")
d.close()
print("thanks for using this tools now your host has been createed")
