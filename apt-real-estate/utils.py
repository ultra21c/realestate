import datetime
import calendar
import requests
import locale

from bs4 import BeautifulSoup

class Utils(object):
    lcode = {}
    pdates = []
    def codeLoad(self):
        with open('./res/lcode.dat') as f:
            for line in f.readlines():
                row = line.strip().split("   ")
                idx = row[0].strip()
                code = row[1].strip()
                name = row[2].strip()
                self.lcode[code] = name

    def period(self, p):
        today = datetime.date.today()
        month = today.month
        year = today.year
        emonth = month - p
        eyear = year
        while(p > 0):
            emonth = month - p +1
            p -=1
            eyear = year
            if emonth < 1:
                eyear -=1
                emonth = 12 + emonth
            self.pdates.append("%s%02d"%(eyear, emonth))
        return self.pdates    

class APIs(object):
    apiKey = "bl4TKVA4HC31zFStJKxeFu7WbqOJ9Uygqu3hWhDNEgS3CF9zgCSln9AXwsbxwNMqENQ5lfiRozVNc88EYwAwlQ%3D%3D"
    prefix = "http://openapi.molit.go.kr:8081/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc"
    apiRent = '''%(prefix)s/getRTMSDataSvcAptRent?LAWD_CD=%(lcode)s&DEAL_YMD=%(ymd)s&serviceKey=%(key)s'''
    apiTrade = '''%(prefix)s/getRTMSDataSvcAptTrade?LAWD_CD=%(lcode)s&DEAL_YMD=%(ymd)s&serviceKey=%(key)s'''
    params = {}
    params['key'] = apiKey
    params['prefix'] = prefix

    def rent(self, f, lname, lcode, ymd):
        self.params['lcode'] = lcode
        self.params['ymd'] = ymd
        body = requests.get(self.apiRent%self.params).text
        soup = BeautifulSoup(body, 'xml')
        for it in soup.findAll('item'):
            ans = {}
            ans['lname'] = lname
            ans['price'] = it.find('보증금액').string.strip()
            ans['mprice'] = it.find('월세금액').string.strip()
            ans['constyear'] = it.find('건축년도').string.strip()
            ans['year'] = it.find('년').string.strip()
            ans['month'] = it.find('월').string.strip()
            ans['yyyymm'] = ans['year'] + "%02d"%int(ans['month'])
            ans['day'] = it.find('일').string.strip()
            ans['size'] = it.find('전용면적').string.strip()
            ans['dong'] = it.find('법정동').string.strip()
            ans['jibun'] = it.find('지번').string.strip()
            ans['apt'] = it.find('아파트').string.strip()
            ans['floor'] = it.find('층').string.strip()
            ans['pyong'] = round(float(ans['size']) * 0.3025)
            ans['type'] = '전월세'
            rentPee = int(ans['mprice'].replace(',',''))*100
            ans['sprice'] = format(round((int(ans['price'].replace(',','')) + rentPee)  / ans['pyong']),',')
            ans['rsprice'] = format(round(int(ans['sprice'].replace(',','')) * 0.8), ',')
            ret = ('%(lname)s %(dong)s\t%(jibun)s\t%(apt)s\t%(floor)s\t%(size)s\t%(pyong)s\t%(price)s\t%(mprice)s\t%(sprice)s\t%(rsprice)s\t%(year)s\t%(month)s\t%(day)s\t%(yyyymm)s\t%(constyear)s\t%(type)s'%ans)
            f.write('%s\n'%ret)
            print (ret)

    def trade(self, f, lname, lcode, ymd):
        self.params['lcode'] = lcode
        self.params['ymd'] = ymd
        body = requests.get(self.apiTrade%self.params).text
        soup = BeautifulSoup(body, 'xml')
        for it in soup.findAll('item'):
            ans = {}
            ans['lname'] = lname
            ans['price'] = it.find('거래금액').string.strip()
            ans['mprice'] = '0'
            ans['constyear'] = it.find('건축년도').string.strip()
            ans['year'] = it.find('년').string.strip()
            ans['month'] = it.find('월').string.strip()
            ans['yyyymm'] = ans['year'] + "%02d"%int(ans['month'])
            ans['day'] = it.find('일').string.strip()
            ans['size'] = it.find('전용면적').string.strip()
            ans['dong'] = it.find('법정동').string.strip()
            ans['jibun'] = it.find('지번').string.strip()
            ans['apt'] = it.find('아파트').string.strip()
            ans['floor'] = it.find('층').string.strip()
            ans['type'] = '매매'
            ans['pyong'] = round(float(ans['size']) * 0.3025)
            ans['sprice'] = format(round(int(ans['price'].replace(',','')) / ans['pyong']),',')
            ans['rsprice'] = format(round(int(ans['sprice'].replace(',','')) * 0.8), ',')
            ret = ('%(lname)s %(dong)s\t%(jibun)s\t%(apt)s\t%(floor)s\t%(size)s\t%(pyong)s\t%(price)s\t%(mprice)s\t%(sprice)s\t%(rsprice)s\t%(year)s\t%(month)s\t%(day)s\t%(yyyymm)s\t%(constyear)s\t%(type)s'%ans)
            f.write('%s\n'%ret)
            print (ret)
            
        
if __name__ == '__main__':
    utils = Utils()
    utils.codeLoad()
    codes = utils.lcode
    for name in codes:
        print ("%s : %s" %(name, codes[name]))

    dates = utils.period(12)
    for date in dates:
        print (date)
    
    apis = APIs()
    with open('output/test.txt', 'w') as f:
        apis.rent(f, '만안구', '48840', '201309')
        apis.trade(f, '만안구', '48840', '201309')
