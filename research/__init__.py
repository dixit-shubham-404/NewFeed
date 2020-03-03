#curl 'https://ieeexplore.ieee.org/rest/search' -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0' -H 'Accept: application/json, text/plain, */*' -H 'Accept-Language: en-US,en;q=0.5' --compressed -H 'Referer: https://ieeexplore.ieee.org/search/searchresult.jsp?newsearch=true&queryText=cloud' -H 'Content-Type: application/json' -H 'Connection: keep-alive' -H 'Cookie: _gcl_au=1.1.388983739.1583225671; JSESSIONID=RDefm2WwdAlodqRc-q9A6R0MtwssbsWqzm-E-01JikcPIMYCaSnz!1128870156; ipCheck=103.79.235.159; WLSESSION=186802828.20480.0000; TS01dcb973=012f350623c6bba947f02682c0b0223479905cf75c240beee29cbeb6675c206954817ed6173f35702c30a5716968e77eda744f177ec86685b39a320115078aa4da0f869c319ddc3d98ff5ee11f12fa57a2c609babd; TS01109a32=012f350623a5ac22808cbf229b759e398329b681eb240beee29cbeb6675c206954817ed61740f0c1cd6eb00bcd0d753943da1e7b9ec223568273fcabd0f93d0751c259e290d9b5598098d90aa2602e09143e7c0b7e3562cdb82b764bb2d403cc2c27440c05ec8fb4e87ec6b44d0b8aaa66c753baf2; fp=65228f736ee8c0ddd84fde9cc8ef7fe3; utag_main=v_id:01709f9ac41d0002cedadcc5b41b00044002b0090086e$_sn:1$_ss:0$_st:1583227529561$ses_id:1583225685023%3Bexp-session$_pn:3%3Bexp-session$vapi_domain:ieee.org; AMCV_8E929CC25A1FB2B30A495C97%40AdobeOrg=1687686476%7CMCIDTS%7C18325%7CMCMID%7C51659105787088705983290730500960058943%7CMCAAMLH-1583830485%7C12%7CMCAAMB-1583830485%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1583232885s%7CNONE%7CvVersion%7C3.0.0; AMCVS_8E929CC25A1FB2B30A495C97%40AdobeOrg=1; __gads=ID=d82dad127624eeb5:T=1583225686:S=ALNI_Mb3-IiAO_Uf_-g89es_RdVOlLFkpw; s_cc=true' -H 'Cache-Control: max-age=0' --data '{"newsearch":true,"queryText":"cloud","highlight":true,"returnFacets":["ALL"],"returnType":"SEARCH"}'
import requests
import _json

def do_research():
    print('=============================================================================================')
    topic=input('Enter the topic you want to search?')
    print()
    print('=============================================================================================')
    cookies = {
        '_gcl_au': '1.1.388983739.1583225671',
        'JSESSIONID': 'RDefm2WwdAlodqRc-q9A6R0MtwssbsWqzm-E-01JikcPIMYCaSnz!1128870156',
        'ipCheck': '103.79.235.159',
        'WLSESSION': '186802828.20480.0000',
        'TS01dcb973': '012f350623c6bba947f02682c0b0223479905cf75c240beee29cbeb6675c206954817ed6173f35702c30a5716968e77eda744f177ec86685b39a320115078aa4da0f869c319ddc3d98ff5ee11f12fa57a2c609babd',
        'TS01109a32': '012f350623a5ac22808cbf229b759e398329b681eb240beee29cbeb6675c206954817ed61740f0c1cd6eb00bcd0d753943da1e7b9ec223568273fcabd0f93d0751c259e290d9b5598098d90aa2602e09143e7c0b7e3562cdb82b764bb2d403cc2c27440c05ec8fb4e87ec6b44d0b8aaa66c753baf2',
        'fp': '65228f736ee8c0ddd84fde9cc8ef7fe3',
        'utag_main': 'v_id:01709f9ac41d0002cedadcc5b41b00044002b0090086e$_sn:1$_ss:0$_st:1583227529561$ses_id:1583225685023%3Bexp-session$_pn:3%3Bexp-session$vapi_domain:ieee.org',
        'AMCV_8E929CC25A1FB2B30A495C97%40AdobeOrg': '1687686476%7CMCIDTS%7C18325%7CMCMID%7C51659105787088705983290730500960058943%7CMCAAMLH-1583830485%7C12%7CMCAAMB-1583830485%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1583232885s%7CNONE%7CvVersion%7C3.0.0',
        'AMCVS_8E929CC25A1FB2B30A495C97%40AdobeOrg': '1',
        '__gads': 'ID=d82dad127624eeb5:T=1583225686:S=ALNI_Mb3-IiAO_Uf_-g89es_RdVOlLFkpw',
        's_cc': 'true',
    }
    Refer = 'https://ieeexplore.ieee.org/search/searchresult.jsp?newsearch=true&queryText='+topic
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Referer': 'https://ieeexplore.ieee.org/search/searchresult.jsp?newsearch=true&queryText=security',
        'Content-Type': 'application/json',
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
    }
    data='{"newsearch":true,"queryText":"'+topic+'","highlight":true,"returnFacets":["ALL"],"returnType":"SEARCH"}'
    response = requests.post('https://ieeexplore.ieee.org/rest/search', headers=headers, cookies=cookies, data=data)
    response=response.json()
    i=0
    for article in response['records']:
        i=i+1
        if i==10:
            break;
        print('Article Name:'+article['articleTitle']+'\t|\t Pubclication Date: '+article['publicationDate']+'\n')
        print('Link: '+'https://ieeexplore.ieee.org'+article['documentLink']+'\n')
        print('=============================================================================================')

