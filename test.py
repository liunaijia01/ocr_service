import requests

post_data = {"img_url": "https://image.baidu.com/search/detail?ct=503316480&z=undefined&tn=baiduimagedetail&ipn=d&word=%E5%B8%A6%E6%96%87%E5%AD%97%E7%9A%84%E5%9B%BE%E7%89%87&step_word=&ie=utf-8&in=&cl=2&lm=-1&st=undefined&hd=undefined&latest=undefined&copyright=undefined&cs=1009223177,3781080280&os=206590818,4045498103&simid=3038621,774010963&pn=11&rn=1&di=3410&ln=1548&fr=&fmq=1601023630916_R&fm=&ic=undefined&s=undefined&se=&sme=&tab=0&width=undefined&height=undefined&face=undefined&is=0,0&istype=0&ist=&jit=&bdtype=0&spn=0&pi=0&gsm=0&hs=2&objurl=http%3A%2F%2Fgss0.bdstatic.com%2F7LsWdDW5_xN3otebn9fN2DJv%2Fdoc%2Fpic%2Fitem%2Fe850352ac65c103871cdccc9ba119313b07e890d.jpg&rpstart=0&rpnum=0&adpicid=0&force=undefined"}
res = requests.post(url="http://0.0.0.0:8888/pic2text", data=post_data)
print(res.text)