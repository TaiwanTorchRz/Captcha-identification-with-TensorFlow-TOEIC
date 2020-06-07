import requests,bs4
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'}
for c in range(250):
    f=open('./pic/'+str(c)+'.jpg','wb')
    f.write(requests.get('https://www.examservice.com.tw/Account/GetValidateCode',headers=headers).content)
    f.close()
    print(c)
