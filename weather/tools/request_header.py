


def get_cookie():

    raw_cookie = '''
    SINAGLOBAL=172.16.7.68_1512522631.934674; SCF=AimavQAn62pihBQdw9etdtjvHiMykPaq8jKUnlGnw_AKrKASbjv_2wRh-45oCVo3raPzedAf-I_fjBS8eQ8LRRQ.; UOR=www.baidu.com,blog.sina.com.cn,; U_TRS1=000000a8.33672fe9.5a45a2dc.60557b32; sso_info=v02m6alo5qztKWRk5yljoOgpZCjhKWRk5SljpOApY6DjKWRk5ilkJOkpY6TpKWRk5SlkJSQpY6TgKWRk5yljpSEpY6DkKWRk6SlkJSIpY6ToKWRk5SljoOUpY6DoKWRk5yljpOQpY6UmKadlqWkj5OUto2TlLCOg5S1jKOcwA==; SUB=_2AkMtCf7tf8NxqwJRmP4RxG_ja4R-ygnEieKbVQ82JRMyHRl-yD9jqmIftRB6BonQApTq266yL2e-Sp8CAijmBPZVz-Nr; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9WWI1LwPzEgr70nZROJnKyO0; NEVIS-WEATHER=c6bf40b75e3394cc69125b6a8186b749; vjuids=b4430eb2b.1614074514a.0.095faffef41e4; Apache=60.1.128.30_1517204820.540007; rotatecount=1; ULV=1517204841307:4:2:1:60.1.128.30_1517204820.540007:1514942867614; U_TRS2=0000001e.6dc770d1.5a6eb569.8f9a0450; lxlrttp=1517109061; vjlast=1517204820.1517204820.30
    '''
    cookie_list = raw_cookie.split(';')

    dict_cookies = {}

    for item in cookie_list:
        dict_cookies[item[0].replace(' ', '')] = item[1].replace(' ', '')
        pass
    return dict_cookies
