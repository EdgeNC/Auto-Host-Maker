import os

os.system("title ARIF TOOLS AUTO HOST MAKER")
host="host.txt"
d = open(host, 'w')
IPv4 = input("Input Your IP : ")
d.write(f"""{IPv4} growtopia1.com
{IPv4} growtopia2.com""")
d.close()
print("thanks for using this tools now your host has been createed")
