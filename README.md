### 배추 가격 예측 인공지능 소프트웨어 (AI-powered Cabbage Price Forecasting Software)
배추 가격을 예측하는 인공지능 소프트웨어입니다. <br/>
It is an AI software that predicts the price of cabbages. <br/>

By 선도사업 Vegita 팀: 나동빈(교원대), 장승훈(교원대), 한지섭(충북대), 김연우(충북대), 명평윤(교통대)

### 시스템 구성도 (System Configuration Diagram)
![image](https://user-images.githubusercontent.com/16822641/44393019-8881e580-a56e-11e8-8c08-f72eb87f1016.png)

### Demo Web Site
![image](https://user-images.githubusercontent.com/16822641/44393034-933c7a80-a56e-11e8-9678-a3a088e7d23f.png)

### 참고 문헌 (References)
* [기상청 전국 기온 및 강수량](https://data.kma.go.kr/climate/StatisticsDivision/selectStatisticsDivision.do?pgmNo=158) : 기상청 정보를 토대로 채소 가격에 영향을 미치는 요인을 분석하기 위해 참고하였습니다.
* [National Temperature and Precipitation of the Korea Meteorological Administration](https://data.kma.go.kr/climate/StatisticsDivision/selectStatisticsDivision.do?pgmNo=158) : Based on the information of the Korea Meteorological Administration, it was used to analyze the factors affecting vegetable prices. <br/>
* [월별 배추 가격](https://www.kamis.or.kr/customer/price/retail/period.do?action=monthly&yyyy=2018&period=10&countycode=&itemcategorycode=200&itemcode=211&kindcode=&productrankcode=&convert_kg_yn=N) : 실질적인 국내 월별 배추 가격을 분석하기 위해 참고하였습니다.
* [Monthly Cabbage Price](https://www.kamis.or.kr/customer/price/retail/period.do?action=monthly&yyyy=2018&period=10&countycode=&itemcategorycode=200&itemcode=211&kindcode=&productrankcode=&convert_kg_yn=N) : This was used as a reference to analyze the actual monthly price of cabbage in Korea.
* [시계열수치입력 수치예측 모델 레시피](https://tykimos.github.io/2017/09/09/Time-series_Numerical_Input_Numerical_Prediction_Model_Recipe/) : 시계열(Time-Series Analysis) 예측 모델 학습자료로 참고하였습니다.
* [Time Series Input Numerical Prediction Model Recipe](https://tykimos.github.io/2017/09/09/Time-series_Numerical_Input_Numerical_Prediction_Model_Recipe/) : It was referenced as a learning material for the Time-Series Analysis prediction model.

### 서버 실행 명령어 (Server Run Commands)
```
# 깃 허브에서 소스코드를 다운로드 받습니다 (Download the source code from the git hub)
git clone https://github.com/ndb796/Vegita.git

# 받은 프로젝트 폴더로 이동합니다 (Navigate to the received project folder)
cd Vegita

# 플라스크 웹 서버 폴더로 이동합니다 (Navigate to the Flask web server folder)
cd "Flask Web Server"

# 웹 서버를 실행합니다 (Run the web server)
python server.py
```

### 파이썬 데이터 학습 모델 생성 명령어 (Create Python Data Learning Model Commands)
```
# 프로젝트 폴더에서 파이썬 폴더로 이동합니다 (In the Project folder, navigate to the Python folder)
cd "Python Software"

# 엑셀(Excel) 파일로 학습을 수행합니다 (Performs training with an Excel file)
python offline.py

# 옵션(Option) 학습된 데이터를 확인합니다 (View the trained data)
python "predict test.py"
>> 평균 온도 (Average temp)  : -2.7
>> 최저 온도 (Lowest temp)   : -6.6
>> 최고 온도 (highest temp)  : 2.0
>> 강수량    (precipitation) : 0.1
[2000.2086]

# 이후에 생성된 모델 파일을 웹 서버의 model 폴더에 붙여넣기 하면 적용됩니다.
# If you paste the generated model file to the model folder of the web server, it will be applied.
```
