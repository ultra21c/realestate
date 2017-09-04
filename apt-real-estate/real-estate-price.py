
import sys
from utils import Utils
from utils import APIs

def lcodeViewer(utils):
    utils.codeLoad()
    codes = utils.lcode
    msg = ''
    idx = 0
    for code in codes:
        idx +=1
        if msg == "":
            msg = "[%s](%s)"%(code, codes[code])
        else:
            msg += "\t\t" + "[%s] %s"%(code, codes[code])
        if (idx%5) == 0:
            print (msg)
            msg = ""
    
def callData(lname, lcode, period):
    apis = APIs()
    filename = './output/%s-%s.csv'%(lname.strip().replace(' ',''),lcode)
    with open(filename, 'w') as f:
        title = '시/군/구 동\t지번\t아파트명\t층\t전용면적\t평(전용면적)\t가격(보증금)\t월세\t평단가(전용)\t평단가(80%)\t년\t월\t일\t년월\t건축년도\t거래형태'
        print (title)
        f.write ('%s\n'%title)
        for p in period:
            apis.rent(f, lname, lcode, p)
            apis.trade(f, lname, lcode, p)


if __name__ == '__main__':
    utils = Utils()
    lcodeViewer(utils)
    lcode = input('\n* 지역명 옆의 지역코드를 입력하세요. ')
    period = input('* 추출기간. 오늘부터 몇개월 전까지를 조회할까요?(ex. 3, 12) : ')
    dates = utils.period(int(period))
    callData(utils.lcode[lcode], lcode, dates)
