# realestate
## KB부동산 데이터 정재
  * 두줄로 되어 있는 KB데이터를 한 라인으로 만들기
  * sample
  ```
    "골든/
    안양시 관양동"
    "골든/
    안양시 관양동"
    "골든/
    안양시 관양동"
  ```
   > python kb_aptname.py -f apt-manan-all.dat -j merge
   * file은 ./data/하위에 있어야 한다.

  * 슬래쉬로 구분되어 있는, 공급전용 면적을 나누기
  * sample
  ```
  99.43/84.89
  113.18/96.64
  142.54/127.45
  ```
  > python kb_aptname.py -f slash_manan-all.dat -j split
  * file은 ./data 하위에 있어야 한다.
    
## 실거래데이터를 이용한 갭
  * 매매 실거래 데이터 다운로드 : 다운로드 받은 파일을 c&p하여 tab 구분자로 data 디렉토리에 위치.
  * 전세 실거래 데이터 다운로드 : 상동
  * 실행
  * ./real_gap.sh
## KB부동산 아파트/주소가 2열로 되어 있는것 하나로
  * http://nland.kbstar.com/quics?page=B047172&cc=b028364:b057198&F%EB%8C%80%EC%A7%80%EC%97%AD%EB%AA%85=%EA%B2%BD%EA%B8%B0%EB%8F%84&F%EC%A4%91%EC%A7%80%EC%97%AD%EB%AA%85=%EC%95%88%EC%96%91%EC%8B%9C&F%EC%86%8C%EC%A7%80%EC%97%AD%EB%AA%85=%ED%8F%89%EC%B4%8C%EB%8F%99&%ED%8E%98%EC%9D%B4%EC%A7%80%EB%B2%88%ED%98%B8=4
  * 위에서 c&p한 데이터를 구글시트에 붙여넣고 단지명/소재지 열을 변경.
  * kb_aptname.kb_newline_merge
## "/" 로 구분 되어 있는 전용/공급면적
  * kb_aptname.split_slash 
  
## 아파트 실거래가 데이터 추출
 * 아파트 실거래가데이터를 추출한다
 * python 3.x기준이다.
 > python real-estate-price.py