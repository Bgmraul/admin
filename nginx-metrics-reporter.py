from collections import Counter

access_ip = []
with open("/var/log/nginx/access.log") as file:
    data_access = [line.strip().split(' ') for line in file]
    for data in data_access:
        access_ip.append(data[0])

data_ip = Counter(access_ip).most_common()

with open('/opt/report.txt', 'w') as file:
    for ip in data_ip:
        file.write(str(ip).strip('()').replace(",", "   ")+'\n')
