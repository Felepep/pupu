import requests
import re

cookies = dict(mybbuser='', sid='')
headers = {'POST':'/forum/xmlhttp.php HTTP/1.1', 'Host': '',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0',
            'Accept':'*/*', 'Accept-Encoding':'gzip, deflate',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8', 'X-Requested-With':'XMLHttpRequest',
            'Content-Length':'50', 'Origin':'', 'Connection':'close'}
url = ''

info_url = input('user: ')
acesso_url = requests.get(info_url, cookies=cookies)
html = acesso_url.text
num_pages = int(re.findall('<span class="pages">Pages(.+?):</span>', html)[0].replace('(', '').replace(')', ''))
id = re.findall('action=profile&amp;uid=(.+?)">', html)  # o primeiro id que aparece é o seu

for i in range(0, num_pages):
    pids = re.findall('#pid(.+?)"', html)
    for j in range(0, len(pids)):
        data = {'action': 'xem_fast_rep', 'uid': id[1], 'pid': pids[j], 'reputation':-1}
        hezbollah = requests.post(url, cookies=cookies, data=data, headers=headers)
    acesso_url = requests.get(info_url + '&page={}'.format(i + 2))
    html = acesso_url.text
