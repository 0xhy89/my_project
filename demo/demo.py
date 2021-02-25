# -*- coding: utf-8 -*-
# @Time    : 2020-09-11 14:18
# @Author  : XU
# @File    : demo.py
# @Software: PyCharm
import os
import re
import poplib
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr

keyword = ['闪退', '崩溃', 'app', 'App', 'APP', '引诱']
dir_path = os.path.abspath(os.path.dirname(__name__))
filename = dir_path + '/demo.html'

html = """<html>
<head>
    <meta http-equiv="content-type" content="text/html;charset=utf-8"/>
</head>
<table border="1" cellspacing="0" style="text-align: left;" cellpadding="4">{}
</table>
</html>"""

item = """
    <tr>
        <td>{}</td>
        <td>{}</td>
        <td>{}</td>
        <td>{}</td>
        <td>{}</td>
        <td>{}</td>
        <td>{}</td>
        <td>{}</td>
        <td>{}</td>
    </tr>
"""


def decode_msg_header(header):
    """
    解码头文件
    :param header: 需解码的内容
    :return:
    """
    value, charset = decode_header(header)[0]
    if charset:
        value = value.decode(charset)
    return value


def decode_msg_body(body):
    """
    解码内容
    :param body: 邮件部分
    :return:
    """
    content_type = body.get_content_type()
    text_content = ""
    if content_type == "text/plain" or content_type == "text/html":
        content = body.get_payload(decode=True)
        charset = body.get_charset()
        if charset is None:
            content_type = body.get('Content-Type', '').lower()
            position = content_type.find('charset=')
            if position >= 0:
                charset = content_type[position + 8:].strip()
        if charset:
            text_content = content.decode(charset)
    return text_content


def msg_obj():
    """pop服务器信息"""
    pop_host = "pop.exmail.qq.com"
    user_account = "xusirui@tianyancha.com"
    user_password = "X4aU69qBtYYRw8uK"

    pop_server = poplib.POP3(host=pop_host)
    pop_server.user(user=user_account)
    pop_server.pass_(pswd=user_password)

    """获取邮件数量"""
    message_count, mailbox_size = pop_server.stat()

    """获取一封邮件信息"""
    for i in range(message_count):
        response, msgLines, octets = pop_server.retr(which=message_count - i)
        msg_to_str = b"\r\n".join(msgLines).decode(encoding="utf8", errors="ignore")
        msg_object = Parser().parsestr(msg_to_str)  # 获取邮件对象

        """获取发件人姓名、发件人地址"""
        # sender_content = msg_object["From"]
        # sender_name, sender_address = parseaddr(addr=sender_content)
        # sender_realname = decode_msg_header(header=sender_name)

        """获取邮件主题"""
        msg_header = msg_object["Subject"]
        msg_real_header = decode_msg_header(header=msg_header)
        if "针对企业申诉" in msg_real_header:
            break

    return msg_object


msg_object = msg_obj()

"""获取邮件正文"""
msg_body_contents = []
if msg_object.is_multipart():
    msg_parts = msg_object.get_payload()
    for msg_body in msg_parts:
        body_content = decode_msg_body(body=msg_body)
        if body_content:
            msg_body_contents.append(body_content)
else:
    body_content = decode_msg_body(body=msg_object)
    if body_content:
        msg_body_contents.append(body_content)

contents = msg_body_contents[0]
# td = r'<td>(.*?)</td>'
# contents_list = re.findall(td, contents)
# for content in contents_list:
#     if '</a>' in content:
#         contents_list.pop(contents_list.index(content))
# print(contents)

for word in keyword:
    contents = contents.replace(word, f'<span style="color: red; ">{word}</span>')

with open(filename, 'w', encoding='utf8') as file:
    file.write(contents)

pop_server.quit()
