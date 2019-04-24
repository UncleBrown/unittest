#/usr/bin/env python3

#Data:11:19
#Author:Jeremy
#File:.py

from email.mime.text import MIMEText
from email.utils import parseaddr,formataddr
from email.header import Header

#把一个标头的用户名编码成utf-8格式的，如果不编码原标头中文用户名，用户名将无法被邮件解码
def _format_addr(s):
    #返回2元祖
    name,addr = parseaddr(s)
    print("parseaddr(s):%s,%s" %(name,addr))
    return formataddr((Header(name,'utf-8').encode(),addr))


from_addr = '494191687@qq.com'
msg = MIMEText('正文','palin','utf-8')
msg['From'] = _format_addr("发件人名<%s>" %from_addr)

msg1 = Header("发件人名",'utf-8')
print("msg['From']:%s" %msg['From'])
print("msg1:%s" %msg1)

