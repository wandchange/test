import requests
url = "https://www.lagou.com/jobs/positionAjax.json?xl=%E5%A4%A7%E4%B8%" \
      "93&px=default&city=%E5%B9%BF%E5%B7%9E&needAddtionalResult=false"
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0',
    'Referer':'https://www.lagou.com/jobs/lis…%B8%93&city=%E5%B9%BF%E5%B7%9E',
    'Host':'www.lagou.com'
}
datas = {
    'first': 'false',
    'pn': '4',
    'kd': 'python'
}
cookies = {
    'Cookie':'JSESSIONID=ABAAABAAAGFABEF80BACEC13CBF9AF243988CA96FF66CE3; _ga=GA1.2.497730886.1533'
             '707848; _gid=GA1.2.84269221.1533707848; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=15337'
             '07849; user_trace_token=20180808135728-ee8f3e23-9acf-11e8-a343-5254005c3644; LGUID=201'
             '80808135728-ee8f418a-9acf-11e8-a343-5254005c3644; index_location_city=%E5%B9%BF%E5%B7%9E;'
             ' TG-TRACK-CODE=search_code; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1533712719; LGRID='
             '20180808151839-4591f271-9adb-11e8-a356-5254005c3644; SEARCH_ID=84ac6c7588234d29a995560b0e'
             'cd6d76'
}
r = requests.post(url,datas,headers=header)# cookies=cookies
r.encoding ="utf-8"
print(r.text)