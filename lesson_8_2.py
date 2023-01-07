"""
 Написать регулярное выражение для парсинга файла логов web-сервера из ДЗ 6 урока nginx_logs.txt
(https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs) для получения
информации вида: (<remote_addr>, <request_datetime>, <request_type>, <requested_resource>, <response_code>,
<response_size>), например:
raw = '188.138.60.101 - - [17/May/2015:08:05:49 +0000] "GET /downloads/product_2 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.9.7.9)"'
parsed_raw = ('188.138.60.101', '17/May/2015:08:05:49 +0000', 'GET', '/downloads/product_2', '304', '0')
"""
import re

re_ip = re.compile(r'^\d+[.]\d+[.]\d+[.]\d')
re_datetime = re.compile(r'\[(.+)]')
re_type = re.compile(r'GET|POST')
re_resource = re.compile(r'[/]\w+[/]\w+\s')
re_code = re.compile(r'(?<="\s)\d{3}\s')
re_size = re.compile(r'(?<=\d{3}\s)\d+')
re_from_hell = re.compile(r"(^\d+[.]\d+[.]\d+[.]\d+) .+\[(.+)] \"(GET|POST) (.+)\" (\d{3}) (\d+)")


with open('ip.txt', 'r') as f:
    for line in f:
        print(re_from_hell.findall(line))
