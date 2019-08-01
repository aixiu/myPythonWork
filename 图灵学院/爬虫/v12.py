#!/usr/bin/env python
# -*- coding: utf-8 -*-

from urllib import request

if __name__ == '__main__':

    url = 'http://www.renren.com/882859385/profile'

    headers = {
        'Cookie':'anonymid=jyshd6q2-onsom5; depovince=GW; jebecookies=e841441e-0a05-45b5-848e-ce0371ba3547|||||; _r01_=1; JSESSIONID=abcY-Skk11vLd86nEHmXw; ick_login=7fce484a-4cdc-4272-820f-c4b728b4a785; _de=806D978CF17762997DE1374C26B60001; p=0f306fff094cf51dd8a41f93b64209f05; first_login_flag=1; ln_uact=4815563@qq.com; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; t=4ba79678afe3432f0dc93c69a1ea21ae5; societyguester=4ba79678afe3432f0dc93c69a1ea21ae5; id=882859385; xnsid=b37a03f4; ver=7.0; loginfrom=null; jebe_key=e68ae459-da2a-4cdf-bda6-d29b26af71c4%7Cc40d1edb1e0a1a8abcc7d3ac7afb27a5%7C1564651946175%7C1%7C1564651947701; jebe_key=e68ae459-da2a-4cdf-bda6-d29b26af71c4%7Cc40d1edb1e0a1a8abcc7d3ac7afb27a5%7C1564651946175%7C1%7C1564651947703; wp_fold=0'
    }

    rsp = request.Request(url, headers=headers)

    rsp = request.urlopen(rsp)

    html = rsp.read().decode()


    with open('rsp.html', 'w')  as f:
        f.write(html)