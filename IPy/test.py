from IPy import IP

ip=IP('192.168.247.32/27')
ips = '192.168.247.33/27'
ips.split('/')[0].split('.')[-1].strip()
print('.'.join(ips.split('/')[0].split('.')[:-1]))
# 计算网段的IP个数