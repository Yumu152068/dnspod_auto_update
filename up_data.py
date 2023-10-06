import socket
import requests
import datetime
import logging
logging.basicConfig(filename='YOUR_LOGPATH',
                 format = '%(asctime)s-%(levelname)s：%(message)s',
                 encoding= 'utf8',
                 level=logging.INFO)
logging.info(f'____________________________________________________{datetime.date.today()}___________________________________________________________________')

ipv6_temp_path = f'D:/ip-get/ipv6_temp'
def update_ipv6(ipv6):
    id = 'YOUR_ID'
    token = 'YOUR_TOKEN'
    domain_id = 'YOUR_DOMAIN_ID'
    sub_domain = 'YOUR_SUB'
    record_type = 'AAAA' #IPV6
    LOGIN_TOKEN = f'{id},{token}'

    url = 'https://dnsapi.cn/Record.Modify'
    data = {
        "login_token":LOGIN_TOKEN,
        "format":"json",
        "domain_id":domain_id,
        "sub_domain":sub_domain,
        "record_type":record_type,
        "record_id":"YOUR_RECORD_ID",
        "record_line":"默认",
        "value":ipv6
    }
    r = requests.post(url,data=data)
    r.encoding = 'unicode_escape'
    logging.info(r.text)
def getipv6():
    host_ipv6=''
    ips=socket.getaddrinfo(socket.gethostname(),80)
    for ip in ips:
        if ip[4][0].startswith('20'):
            host_ipv6=ip[4][0]
    return host_ipv6
ipv6 = getipv6()
try:
    ipv6_temp = open(ipv6_temp_path,encoding='utf8',mode='r+')
    o_ipv6 = ipv6_temp.read()

    if(o_ipv6 != ipv6):
        msg = '已修改'
        update_ipv6(ipv6)
        ipv6_temp.truncate(0)
        ipv6_temp.write(ipv6)

    else:msg = "未修改"
except:
    ipv6_temp = open(ipv6_temp_path,encoding='utf8',mode='w')
    ipv6 = getipv6()
    ipv6_temp.write(ipv6)
    update_ipv6(ipv6)
    msg = '已修改'
url = "YOUR_WEBHOOK_URL"
title = '106_ipv6地址'
content = f'{msg}，ipv6：{ipv6}'
if(msg == '已修改'):
    r = requests.post(
            url,
            json={
                "msgtype": "text",
                "text": {"content": title+'\n'+content}
            },
        )
logging.info(content)
ipv6_temp.close()

