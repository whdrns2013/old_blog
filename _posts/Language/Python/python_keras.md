---
layout: post                              # 레이아웃 : post(게시물)
title:  libraries of python      # 게시물의 제목
subtitle: 파이썬 라이브러리들   # 서브타이틀
date:   2022-11-26 16:46:06 +0900
lastmod:   2022-11-26 16:46:06 +0900
categories: [Language, Python]
author:                                   # 작성자
tags:                     # 태그
meta: "Springfield"                       # 이건 뭐지?
sitemap :
  changefreq : daily
  priority : 1.0
---
<!--postNo: python_libraries-->


> 들어가기 전에  
> Pandas, Numpy, Matplotlib 등 내용이 방대한 라이브러리는  
> 별도의 페이지에서 설명합니다.  

## Keras
[https://keras.io/ko/preprocessing/image/](https://keras.io/ko/preprocessing/image/)

|모듈명|라이브러리명|설명|파라미터|
|---|---|---|---|
|ImageDataGenerator|keras.uitls|기존 이미지를 가지고 새로운 이미지 생성||
|to_categorical|keras.utils|데이터를 원-핫 인코딩 해준다.||



### ImageDataGenerator

* 한정된 데이터량을 '데이터 증식'을 통해 늘려주는 데이터 증식의 일종  
* 회전, 뒤집기, 밀기, 밝기조절 등을 통해 기존 이미지를 복제, 다른형태로 변환한다.  
* 모델을 fit 할 때, train, val 데이터로 활용할 수 있다.

```python
from keras.utils import load_img, img_to_array
from keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt
import numpy as np

# 이미지 제너레이터 만들기

ImageDataGenerator(
    horizontal_flip = bool,
    vertical_flip = bool,
    shear_range = float,
    brightness_range = list[float, float],
    zoom_range = float,
    width_shift_range = float,
    height_shift_range = float,
    rotation_range = float,
    rescale = float,
    fill_mode = 'str'
)

# 적용
## 모델 학습 시에 적용
train_generator = ImageGenerator(Params).flow(x값, y라벨, batch_size)
model.fit(train_generator, epochs=30 ...)
```

|파라미터|데이터타입|설명|
|---|---|---|
|horizontal|bool|수평 방향 뒤집기 여부|
|vertical_flip|bool|수직 방향 뒤집기 여부|
|shear_range|float|전단 : 아래서부터 한쪽으로 민다. 기울기와 비슷|
|brightness_range|float|밝기. 최소% ~ 최대% 만큼 밝기를 조정한다.|
|zoom_range|float|확대|
|width_shift_range|float|너비 조정|
|height_shift_range|float|높이 조정|
|rotation_range|float|회전율|
|rescale|float|각 픽셀 값의 크기 조정. 주어진 값이 곱해진다.|
|fill_mode|str|이미지 조정으로 인해 빈 픽셀을 채우는 방식 지정|

> fill_mode  
> (1) 'constant': kkkkkkkk|abcd|kkkkkkkk (cval=k)  
> (2) 'nearest': aaaaaaaa|abcd|dddddddd  
> (3) 'reflect': abcddcba|abcd|dcbaabcd  
> (4) 'wrap': abcdabcd|abcd|abcdabcd  
  
|메서드|사용법|설명|파라미터|
|---|---|---|---|
|flow|ImageDataGenerator(Params).flow(x, y, batch_size=, ...)|데이터와 라벨 배열을 받아 증강된 데이터의 배치를 생성. x는 원본 이미지, y는 라벨 ...|
|get_random_transform|ImageDataGenerator(Params).get_random_transform(img_shape, seed)|변형에 대한 무직위 매개변수를 생성(딕셔너리 형태로 파람 반환)|
|random_transform|ImageDataGenerator(Params).random_transform(x, seed)|이미지에 무작위 변형을 적용. x와 같은 형태로 반환|
|transform_parameters|ImageDataGenerator(Params).transform_parameters(x, 파람들)| 주어진 이미지(x) 에 파람들에 해당하는 변형을 가한다.|
|fit|ImageDataGenerator(Paramas).fit(x, augment, rouds..)|샘플 데이터에 생성기를 학습시킨다. 특정 상황에서만 필요. x는 샘플 데이터|
|flow_from_directory|ImageDataGenerator(Params).flow_from_directory(...)|디렉토리 위치를 전달받아 증강/정규화된 데이터 배치 생성|
|flow_from_dataframe|ImageDataGenerator(Params).flow_from_dataframe(...)|dataframe과 디렉토리 위치를 전달받아 증강/정규화된 데이터 배치 생성|


### Application

* 전이 학습 transfer learning 에 사용되는 라이브러리.  
* 이미 만들어진 여러 모델들이 들어있다.

![](/assets/images/python_libraries_001.png){: witdh=600}






