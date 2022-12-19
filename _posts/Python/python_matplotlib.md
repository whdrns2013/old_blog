## 인트로
* matplotlib은 파이썬의 시각화 라이브러리이다.

## 설치
* pip install matplotlib 혹은
* conda install matplotlib

```python
pip install matplotlib # pip 이용
conda install matplotlib # anaconda 이용
```


## matplotlib.pyplot (그래프 관련 기본)

> * import : import matplotlib.pyplot  
> * 이하에서는 `plt`로 줄여 설명한다.  
> * 다양한 시각화 도구가 있는 라이브러리  

[Matplotlib 설명]('https://wikidocs.net/92071')

> * matplotlib을 진행하는 순서
> * (1) 여러 개 그래프를 한 번에 그린다면 : subplot
> * (2) plt.plot() 혹은 plt.imshow()
> * (3) 레이블, ticks, fill, lim 내용

### 주요 메서드

|메서드명|설명|파라미터|
|---|---|---|
|plt.plot(data, format)|시각화 데이터와 표현 형태를 정의하는 메서드, 여러 개를 겹쳐 쓸 수 있다.|이하 참고|
|plt.show()|그래프를 보여주는 메서드|없음|
|plt.xlabel('str', ...)|그래프 x축의 레이블을 지정하는 메서드|이하 참고|
|plt.ylable('str', ...)|그래프 y축의 레이블을 지정하는 메서드|이하 참고|
|plt.legend()|그래프의 범례 표기에 대한 설정을 지정하는 메서드|이하 참고|
|plt.xlim([xmin, xmax])|x축에 표현되는 범위를 지정, 혹은 반환한다.|이하 참고|
|plt.ylim([ymin, ymax])|y축에 표현되는 범위를 지정, 혹은 반환한다.|이하 참고|
|plt.axis([xmin, xmax, ymin, ymax])|x, y축에 표현되는 범위를 지정, 혹은 반환한다.|이하 참고|
|plt.fill_between(x[범위], y[범위],, 색상..)|그래프와 x축 사이의 부분의 범위를 채워 표시한다.|이하 참고|
|plt.fill_betweenx(x[범위], y[범위], 색상..)|그래프와 y축 사이의 부분의 범위를 채워 표시한다.|이하 참고|
|plt.fill(x[범위], y1[범위], y2[범위]], 색상..)|특정 영역 범위를 채워 표시한다.|이하 참고|

```python
import matplotlib.pyplot as plt

import matplotlib.pyplot as plt

a = [2, 4, 5, 6]
b = [1, 3, 5, 7]
c = [9, 12, 15, 18]
## 표현할 값 리스트 지정


plt.plot([1,2,3],[2,4,8],'b--', label='1st')
plt.plot([1,5,9],[10,14,16], 'g^', label='2nd')
plt.plot(a, b, 'y-', label='3rd')
plt.plot(a, c, 'r:s', linewidth=5, label='4th')
## x축 내용, y축 내용을 지정하고 선과 점을 설정한다.

plt.xlabel('x axis')
plt.ylabel('y axis', loc = 'top')
## x, y축 레이블 지정

plt.legend(loc='lower right', ncol=2, fontsize=7)
## 범례 표시 지정

plt.fill_between(a[1:3], b[1:3], color='y', alpha=0.5)
plt.fill_between(a[2:4], b[2:4], c[2:4], color='k', alpha=0.3)
plt.fill([3,3,4.5,4.5],[3,5,9,7], color='lightgray', alpha=0.5)
## 영역 채우기

```



### plt.plot() 메서드  

> 시각화할 데이터와 표현 형태를 정의하는 메서드
> 순서대로 사용해야 한다.  

|메서드/파라미터|설명|예시|
|---|---|---|
|plt.plot()|시각화할 데이터를 넣어주는 메서드. 리스트들, 데이터프레임, array, dict 등|plt.plot([1,2,3],[2,4,8])|
|plt.imshow(행렬 등 데이터)|시각화할 이미지 데이터를 넣어주는 메서드. 행렬이 들어갈 수 있다.|
|데이터|리스트, 데이터프레임, array등이 들어갈 수 있다.|plt.plot([1, 2, 3], [2, 4, 8])|
|Format String|그래프에 값을 표시하는 선, 점의 색상과 형태를 지정|plt.plot(data, 'ro')|
|선 종류|선 종류 : 선('-'), 점선('--'), 작은점선(':'), 대쉬닷('-.')... 등|plt.plot(data, '--')|
|linewidth=int|선의 두께를 설정한다. 단위는 pt|plt.plot(data, '--', linewidth=5)| 
|마커 종류|점('o'), 세모('^'), 네모('s')|plt.plot(data, '^')|
|color=c|색상의 선택 : 'r'(빨강), 'b'(파랑), 'g'(초록), 'y'(노랑)... 등이 가능|plt.plot(data, '--', color='b')|
|선, 마커 색상|선, 마커, 색상은 동시에 지정이 가능하다.|plt.plot()
|plt.plot(label='str')|범례에 표현할 label을 지정하는 메서드|plt.plot(label='라벨1')|
|plt.xticks([])|x축의 눈금을 설정한다.|이하 참고|
|plt.yticks([])|y축의 눈금을 설정한다.|이하 참고|
|변수=plt.subplot(nrows, ncols, index)|여러개의 그래프를 한 영역 안에 그린다. plot()아래에 입력하며, 행수, 열수, 몇번째에 표시할지를 지정해준다.|ax1=plt.subplot(2,2,1)|


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
|loc=(float, float)|범례의 여백(혹은 위치) 지정|plt.legend(loc=(1.0, 1.0)|
|loc='위치'|범례의 여백(혹은 위치) 지정. [lower, center, upper], [left, right] 가능|plt.legend(loc='higher left')|
|ncol=int|범례의 열 수 지정. 몇 개의 열로 표기할 것인지|plt.legend(ncol=2) 두 개의 열로 범례 표현|
|fontsize=int|범례 폰트사이즈 지정. 단위는 pt|plt.legend(fontsize=15)|

### 축의 범위를 지정 혹은 반환

![](https://wikidocs.net/images/page/92082/axis_range_07.png)

|메서드/파라미터|설명|예시|
|---|---|---|
|plt.xlim([xmin, xmax])|x축에 표현되는 범위를 지정, 혹은 반환한다.||
|plt.ylim([ymin, ymax])|y축에 표현되는 범위를 지정, 혹은 반환한다.||
|plt.axis([xmin, xmax, ymin, ymax])|x, y축에 표현되는 범위를 지정, 혹은 반환한다.||
|[xmin, xmax, ymin, ymax]|x축의 시작과 끝, y축의 시작과 끝 수|[0, 10, 0, 15]|
|범위 반환| 변수 = plt.xlim(), 변수 = plt.axis()로 범위를 반환받을 수 있다.||
| |지정하지 않으면, 표현되는 값에 맞춰 자동으로 조정된다.| |

### 범위 채우기

|메서드/파라미터|설명|예시|
|---|---|---|
|plt.fill_between(x[범위], y[범위],, 색상..)|그래프와 x축 사이의 부분의 범위를 채워 표시한다.|이하 참고|
|plt.fill_betweenx(x[범위], y[범위], 색상..)|그래프와 y축 사이의 부분의 범위를 채워 표시한다.|이하 참고|
|plt.fill(x[범위], y1[범위], y2[범위]], 색상..)|특정 영역 범위를 채워 표시한다.|이하 참고|
|범위 x[], y[]|채울 범위의 x축, y축 리스트의 index를 입력한다. 리스트 형태로 입력.|plt.fill_between(x[1:10], y[2:6])
|범위 x[], y1[], y2[]|채울 범위의 x축, y축 리스트의 index를 입력한다. 리스트 형태로 입력.|plt.fill(x[1:10], y1[2:6], y2[4:8])|
|color='str'|범위를 채우는 색상을 입력한다. 'b', 'r' 등의 색상 이용 가능|plt.fill_between(x[1:10], y[2:6], color='b')|
|alpha=float|범위를 채우는 색상의 투명도를 설정한다.|plt.fill_between(x[1:10], y[2:6], color='b', alpha=0.5)|

### 눈금 지정 xticks, yticks

|메서드/파라미터|설명|예시|
|---|---|---|
|plt.xticks([])|x축의 눈금을 설정한다. 리스트 안에 표시할 눈금을 입력하며, int 또는 str을 입력할 수 있다. 리스트가 비어있으면 표시하지 않는다.|이하 참고|
|plt.yticks([])|y축의 눈금을 입력하며, int 또는 str을 입력할 수 있다. 리스트가 비어있으면 표시하지 않는다.|이하 참고|


## matplotlib.pyplot (이미지 관련)

> * import : import matplotlib.pyplot  
> * 이하에서는 `plt`로 줄여 설명한다.  
> * 다양한 시각화 도구가 있는 라이브러리  

