## 인트로
* matplotlib은 파이썬의 시각화 라이브러리이다.

## 설치
* pip install matplotlib 혹은
* conda install matplotlib

```python
pip install matplotlib # pip 이용
conda install matplotlib # anaconda 이용
```


## matplotlib.pyplot

> * import : import matplotlib.pyplot  
> * 이하에서는 `plt`로 줄여 설명한다.  
> * 다양한 시각화 도구가 있는 라이브러리  

[Matplotlib 설명]('https://wikidocs.net/92071')

### 주요 메서드

|메서드명|설명|파라미터|
|---|---|---|
|plt.plot(data, format)|시각화 데이터와 표현 형태를 정의하는 메서드|이하 참고|
|plt.show()|그래프를 보여주는 메서드|없음|
|plt.xlabel('str', ...)|그래프 x축의 레이블을 지정하는 메서드|이하 참고|
|plt.ylable('str', ...)|그래프 y축의 레이블을 지정하는 메서드|이하 참고|
|plt.legend()|그래프의 범례 표기에 대한 설정을 지정하는 메서드|이하 참고|



### plt.plot() 메서드  

> 시각화할 데이터와 표현 형태를 정의하는 메서드

|메서드/파라미터|설명|예시|
|---|---|---|
|plt.plot()|시각화할 데이터를 넣어주는 메서드. 리스트들, 데이터프레임, array, dict 등|
|데이터|리스트, 데이터프레임, array등이 들어갈 수 있다.|plt.plot([1, 2, 3], [2, 4, 8])|
|Format String|그래프에 값을 표시하는 선, 점의 색상과 형태를 지정|plt.plot(data, 'ro')|
| |선과 점의 선택 : 선('-'), 점선('--'), 점('o'), 세모('^'), 네모('s')|plt.plot(data, '^')|
| |색상의 선택 : 'r'(빨강), 'b'(파랑), 'g'(초록)... 등이 가능|plt.plot(data, 'ro')|


### 레이블 설정 메서드

> 레이블에 대한 설정값을 지정하는 메서드  

|메서드/파라미터|설명|예시|
|---|---|---|
|plt.xlabel()|x축의 설정값을 지정하는 메서드||
|plt.ylable()|y축의 설정값을 지정하는 메서드||
|'str'|축의 label 제목을 str으로 설정한다.|plt.xlabel('x축제목')|
|labelpad=int|레이블과 그래프 간 여백을 지정. 단위는 pt|plt.xlabel(labelpad = 15)|
|fontdict=dict|폰트 스타일을 설정. 'family', 'color', 'weight', 'size'를 설정할 수 있다.|plt.xlabel(fontdict={'family' : 'serif', 'color' : 'b', 'weight' : 'bold', 'size' : 14})|
|loc='left/right'| x 축 레이블 제목을 좌측 혹은 우측에 표기한다.|plt.xlabel(loc='right')|
|loc='top/bottom'| y 축 레이블 제목을 위 혹은 아래에 표기한다.|plt.ylabel(loc='top')|

### plt.legend() 범례 지정 메서드

|메서드/파라미터|설명|예시|
|---|---|---|
|plt.plot(label='str')|범례에 표현할 label을 지정하는 메서드|plt.plot(label='라벨1')|
|plt.legend()|범례가 그래프에 표기되게끔 한다. 위치는 자동 설정됨||



||||
||||
||||
||||
||||
||||
||||
||||
||||