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


## Miniforge를 이용한 tensorflow 설치

Miniconda 는 아직 arm 아키텍처를 지원하지 않음.  
때문에, arm아키텍처를 유일하게 지원하는 Conda-Forge를 설치해 파이썬을 사용하는 게 유일한 해결책임.  

(1) 아래 링크에서 arm64 버전 forge를 다운로드 해준다.  
https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-MacOSX-arm64.sh

(2) 터미널을 켜고, 아래와 같이 miniforge를 설치해준다.  

```Terminal
(1) cd ~/Downloads/
(2) bash Miniforge3-MacOSX-arm64.sh
```

(3) 설치 중 약관 동의 및 기본 설치 경로 등은 y로 동의한다.

(4) conda 가상환경을 만들어준다.  

```Terminal
(1) conda create -n 가상환경명 python=3.8
(2) conda activate 가상환경명
```

(5) 필요한 프로그램 및 라이브러리를 설치한다.  
conda-activate 로 가상 환경을 실행 후 설치를 진행해야 하며,
conda-forge 의 라이브러리를 설치해야 한다. 아래 링크를 참고  
[https://anaconda.org/conda-forge/repo]('https://anaconda.org/conda-forge/repo')

```Terminal
(1) 주피터랩 : conda install -c conda-forge jupyterlab
(2) Pandas : conda install -c conda-forge pandas
(3) Numpy : conda install -c conda-forge numpy
(4) Tensorflow : conda install -c conda-forge tensorflow
(5) MatPlotlib : conda install -c conda-forge matplotlib-base
(5) tqdm 설치 : conda install tqdm
... 등등
```

(6) 텐서플로우 실행 확인  

* 텐서플로우를 이용한 코드를 실행해, 제대로 실행되는지 확인해주세요.

(7) 이후 사용 : 가상환경 이용  
이후 사용시에는 가상환경상에서 파이썬을 사용해주면 됨.

```Terminal
conda activate 가상환경명

이후

jupyter lab ... 등등 ...

```


### 레퍼런스
https://cpuu.postype.com/post/9077219






##    
##   
## 이하는 이전 시도했던 방식으로, 정상적으로 작동하지 않습니다. 참고용으로 남겨놓습니다.

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
```Terminal

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