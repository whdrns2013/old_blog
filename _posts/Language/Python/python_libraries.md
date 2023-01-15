---
layout: post                              # 레이아웃 : post(게시물)
title:  libraries of python      # 게시물의 제목
subtitle: 파이썬 라이브러리들   # 서브타이틀
date:   2022-11-26 16:46:06 +0900         # 게시물 작성 일자
lastmod:   2022-11-26 16:46:06 +0900         # 게시물 작성 일자
categories: [Language, Python]
author:                                   # 작성자
tags:                     # 태그
meta: "Springfield"                       # 이건 뭐지?
sitemap :
  changefreq : daily
  priority : 1.0
---
<!--postNo: python_libraries-->

## zipfile

Zip 파일을 다루는 라이브러리.

```python
import zipfile

path = '경로명'

# zip 파일 선택
zip_ref = zipfile.ZipFile(path,'r')

# zip 파일 압축 풀기
zip_ref.extractall('dataset/')

# zip 파일 닫기
zip_ref.close
```

## tqdm
진행률을 표시해주는 라이브러리
```python
from tqdm import tqdm

for i in tqdm(range(10)):
    time.sleep(0.5)
```