# 규칙
# o   코드에 ‘/data’ 데이터 입/출력 경로 포함

# o   코드 파일 확장자: .R, .rmd, .py, .ipynb

# o   코드와 주석 인코딩: UTF-8

# o   모든 코드는 오류 없이 실행되어야 함(라이브러리 로딩 코드 포함)

# o   개발 환경(OS) 및 라이브러리 버전 기재

## %matplotlib inline 



#외부 라이브러리 임포트
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# ++ datetime 임포트
import datetime
from datetime import datetime
##warnings
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import os
#xgboost 임포트
import xgboost as xgb
from sklearn.metrics import mean_squared_error







for i in range(58):
    i = i+1
    i = str(i)
    # 한자리수 1을 01로 만들어줌 
    if len(i) == 1:
        i = "0" + i
    CsvName = 'Case_' + i
    
    # globals() 함수로 여러 csv 파싱, 선언
    Parse1 = globals()['train' + str(i)] =  pd.read_csv(r'open\\train_input\\{}.csv'.format(CsvName),encoding = 'UTF-8')
    
    # 이제 growth rate y값도 파싱해준다.
    Parse2 = globals()["train_result" + str(i)] = pd.read_csv(r'open\\train_target\\{}.csv'.format(CsvName),encoding = 'UTF-8')
    
    
    # # 파싱한 2 Csv를 합쳐줍니다 target 값은  28개로 row 개수가 적으니 일단 내비둠.
    # globals()['concated_csv' + i] = pd.concat([Parse1,Parse2], axis = 0)
    


    
    