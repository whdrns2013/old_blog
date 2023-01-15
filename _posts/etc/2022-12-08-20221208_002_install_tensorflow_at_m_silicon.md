---
title:  맥 텐서플로우 설치하기 5단계 (M1 M2 M실리콘)                           # 게시물의 제목
subtitle: M실리콘 맥북에서 텐서플로우 설치하기   # 서브타이틀
date:   2022-12-10 20:21:00 +0900
lastmod:   2022-12-10 20:21:00 +0900
categories: etc                          # 게시물이 속하는 카테고리
author:                                   # 작성자
tags: 맥북 맥 M1 M2 파이썬 텐서플로우                               # 태그
sitemap :
  changefreq : daily
  priority : 1.0
# image:
#     path: /assets/images/20221210_002_002.png
---
<!--postNo: 20221210_002-->

![](/assets/images/20221210_002_002.png)

## Miniforge를 이용한 tensorflow 설치

>Miniconda 는 아직 arm 아키텍처를 지원하지 않음. (2022-12-10)  
때문에, arm아키텍처를 유일하게 지원하는 Conda-Forge를 설치해 파이썬을 사용하는 게 유일한 해결책임.  
{: .prompt-tip }

>tensorflow-macos + tensorflow-metal 과도 실행 속도를 비교해봤으나,  
forge를 통해 설치한 tensorflow의 처리속도가 훨씬 빨랐음.  
왜인지는 모르겠음.. 
(forge - cpu 480% 사용, metal - cpu 60%, gpu 90% 사용)
{: .prompt-tip }

## 설치 방법

1. 아래 링크에서 arm64 버전 forge를 다운로드 해준다.  
https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-MacOSX-arm64.sh

2. 터미널을 켜고, 아래와 같이 miniforge를 설치해준다.  
```terminal
(1) cd ~/Downloads/
(2) bash Miniforge3-MacOSX-arm64.sh
```

3. 설치 중 약관 동의 및 기본 설치 경로 등은 y로 동의한다.

4. conda 가상환경을 만들어준다.  
텐서플로와 호환되는 파이썬 버전이 현재 기준(2022.12.25) 3.10 이하이므로, 주의.  
```terminal
(1) conda create -n 가상환경명 python=3.8
(2) conda activate 가상환경명
```

5. 필요한 프로그램 및 라이브러리를 설치한다.  
conda-activate 로 가상 환경 하에서 설치를 진행해야한다.  
conda-forge 의 라이브러리를 설치해야 하므로 아래 링크를 참고  
[https://anaconda.org/conda-forge/repo]('https://anaconda.org/conda-forge/repo')
```terminal
(1) 주피터랩 : conda install -c conda-forge jupyterlab
(2) Pandas : conda install -c conda-forge pandas
(3) Numpy : conda install -c conda-forge numpy
(4) Tensorflow : conda install -c conda-forge tensorflow
(6) MatPlotlib : conda install -c conda-forge matplotlib-base
(7) 사이킷런 : conda install -c conda-forge scikit-learn
(8) tqdm 설치 : conda install -c conda-forge tqdm
(9) cv 설치 : conda install -c conda-forge opencv
(10) pydot 설치 : conda install -c conda-forge pydot
(11) grapgviz : conda install -c conda-forge graphviz
... 등등
```

6. 텐서플로우 실행 확인  
텐서플로우를 이용한 코드를 실행해, 제대로 실행되는지 확인한다.

7. 이후 사용 : 가상환경 이용  
이후 사용시에는 가상환경상에서 파이썬을 사용해주면 됨.  
```terminal
conda activate 가상환경명
이후
jupyter lab ... 등등 ...
```


### 레퍼런스
(1) https://cpuu.postype.com/post/9077219  
(2) https://discuss.tensorflow.org/t/tensorflow-mac-m1/8706  
(3) https://pasus.tistory.com/218  
(4) https://velog.io/@psjlmk/M1-맥북-tensorflow-설치  