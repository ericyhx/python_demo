# auth:eric.yu
# date: 2023/9/7 10:48
import json
from lxml import etree
import pprint

import requests

# 请求偷
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'}


def request_pic():
    # 请求连接
    url = "https://wenku.baidu.com/gsearch/rec/pcviewdocrec2023"
    # 请求参数
    data = {
        "docId": "58036ddfa3116c175f0e7cd184254b35effd1a7d",
        "query": "2022年研究生考试英语(二)真题",
        "recPositions": ["catalog", "toplist"]
    }
    ret = requests.get(url=url, params=data, headers=headers)
    print(ret.json())


def parse_text_from_bdjson(file_path):
    # url = 'https://wkrtcs.bdimg.com/rtcs/getbdjson?bucketNum=69&pn=1&rn=5&range=38116-7902_7903-15580_15581-31759_31760-38115_38116-&rsign=p_5-r_0-s_6fb49&dataType=rtcs&md5sum=d3b502770dcfefa6e1960a21b24eb805&sign=8421a3cd2b&rtcs_flag=1&rtcs_ver=4&callback=sf_edu_wenku_rtcs_doc_jsonp_1_5&_=1694068790401'
    url = 'https://wkrtcs.bdimg.com/rtcs/getbdjson?bucketNum=69&pn=1&rn=2&range=10305-10304_10305-&rsign=p_2-r_0-s_19e5e&dataType=rtcs&md5sum=7e121e9da6831e7583cf412266e06b5c&sign=3f4bd0ae05&rtcs_flag=3&rtcs_ver=3&callback=sf_edu_wenku_rtcs_doc_jsonp_1_2&_=1694072196296'
    ret = requests.get(url=url, headers=headers)
    s = ret.text.find("(")
    e = ret.text.rfind(")")
    rs = ret.text[s + 1:e]
    r_json = json.loads(rs)['document.xml']
    with open(file_path, "w",encoding='utf-8') as f:
        iterator(r_json, f)


def iterator(ret, f):
    if isinstance(ret, list):
        for r in ret:
            r0 = r['c']
            iterator(r0, f)
    else:
        f.write(ret+"\n")


if __name__ == '__main__':
    file_path = "result.txt"
    parse_text_from_bdjson(file_path)
