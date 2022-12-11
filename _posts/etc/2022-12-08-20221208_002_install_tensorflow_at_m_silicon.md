---
layout: post                              # 레이아웃 : post(게시물)
title:  맥 텐서플로우 설치하기 5단계 (M1 M2 M실리콘)                           # 게시물의 제목
subtitle: M실리콘 맥북에서 텐서플로우 설치하기   # 서브타이틀
date:   2022-12-10 20:21:00 +0900         # 게시물 작성 일자
categories: etc                          # 게시물이 속하는 카테고리
author:                                   # 작성자
tags: 맥북 맥 M1 M2 파이썬 텐서플로우                               # 태그
meta: "Springfield"                       # 이건 뭐지?
---
<!--postNo: 20221210_002-->

### M실리콘 tensorflow 설치하기

1. Conda 가상환경 만들기
```Terminal
conda create -n 가상환경명 anaconda
```

2. Conda 가상환경 실행
```Terminal 
conda activate 가상환경명
```

3. numpy, scipy 업그레이드
```Terminal
pip install numpy --upgrade
pip install scipy --upgrade
```
> Requirement already satisfied:  
> 이 문구는, 이미 최신버전이라는 뜻입니다. 다음 단계로 넘어가세요.

4. tensorflow 설치
```Terminal
conda install -c apple tensorflow-deps
pip install tensorflow-macos
pip install tensorflow-metal
```
> tensorflow-metal : GPU환경을 사용할 수 있게 해주는 툴

5. tensorflow 설치 확인 (버전 확인)
```python
# tensor 버전 확인
python # 파이썬 실행
import tensorflow # 텐서플로우 import
tensorflow.__version__ # 텐서 버전 확인
'버전명 출력됨 -> 내 경우 2.11.0'

# GPU 사용 여부 확인 (1이면 정상)
print(len(tensorflow.config.experimental.list_physical_devices('GPU')))
```

### 주피터에서 tensorflow를 쓰고 싶다면?
1. conda 가상환경을 실행
```Terminal 
conda activate 가상환경명
```

2. jupyter 설치
```Terminal 
pip install jupyter lab # 주피터랩 설치
pip install jupyter notebook # 주피터노트북 설치
```

3. jupyter 실행
```Terminal
conda activate 가상환경명 # 가상환경 실행 후 
jupyter lab
```

이후 tensorflow를 사용할 때에는, 가상환경 실행 후에야 가능합니다.. ㅠㅠ.. 얼른 업데이트가 되길..  
아니면.. 구글 코랩 사용을 권장합니다!  

### 레퍼런스
(1) https://discuss.tensorflow.org/t/tensorflow-mac-m1/8706
(2) https://pasus.tistory.com/218
(3) https://velog.io/@psjlmk/M1-맥북-tensorflow-설치