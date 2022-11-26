---
layout: post                              # 레이아웃 : post(게시물)
title: '깃허브 블로그 (페이지) 만들기'                            # 게시물의 제목
subtitle: 나만의 깃허브 블로그를 만들어보자!  # 서브타이틀
date:   2022-11-26 22:46:06 +0900         # 게시물 작성 일자
categories: How_To_Use_Git                          # 게시물이 속하는 카테고리
author: Jongya                                  # 작성자
tags: [Git], [GitHub], [깃허브], [블로그], [만들기], [블로그 만들기]                              # 태그
meta: "Springfield"                       # 이건 뭐지?
sidebar: []                               # 이건 뭐지?
banner:
  image: https://bit.ly/3xTmdUP  # 배너 이미지
---
<!-- postNo: -->

# 인트로
프로그래밍을 배우면서, <u><b>블로그 운영의 필요성</b></u>을 느꼈습니다.  
어떤 블로그가 내게 맞을까.. 고민을 하다가!  
<u><b>html이나 마크다운에 대한 공부</b></u>도 할 겸 깃허브 블로그를 선택했습니다.  
  
이미 만들어진 서비스들보다는 만들기 어렵지만,  
만들고 보니 꽤나 뿌듯함이 있습니다.  
   
이 글을 보는 여러분께 자그마한 도움이 되었으면 하여  
제가 깃허브 블로그를 만들면서 적용했던 방법, 겪었던 어려움들을 공유합니다.  
  
*깃허브에서 진행하므로, 윈도우/맥 어디에서든 가능합니다.*   
</br>   

# 깃허브 가입과 저장소(Repository) 만들기

## 1) 깃허브 계정 만들기

깃허브 계정은 간단하게 만들 수 있습니다.  
아래 깃허브 사이트에서 `Sign up` 버튼을 클릭해 가입을 진행해주세요.  
(계정이 있으신 분은 Sign in 해주시면 됩니다.)  

> GitHub : https://github.com  

![회원가입](/assets/images/20221126_001_001.png)

</br>

## 2) 깃허브 저장소(Repository) 만들기

화면 오른쪽 상단에서 'Your respository' 를 클릭해주세요.

![저장소](/assets/images/20221126_001_002.png)

  </br>

`NEW` 버튼을 눌러 새로운 repository(저장소)를 만들어 봅시다.

![저장소 만들기](/assets/images/20221126_001_003.png)

</br>

Repository Name(저장소 이름)을 작성 후 `Create repository`를 클릭해주세요.

>💡 Repository Name 은 ` ID.github.io `  형식으로 만드시길 추천드립니다.

![저장소 만들기2](/assets/images/20221126_001_004.png)

</br>

repository가 만들어졌습니다. 한 번 들어가볼까요?

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/70059be5-9061-4b68-9f20-8981cea085d8/Untitled.png)

## 3) 깃허브 Page Setting

1. repository 화면에서 settings를 클릭해줍니다.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/cfb27758-d735-4a96-b50f-1c32796db792/Untitled.png)

1. page 메뉴에서 아래와 같이 설정한 후, save 해줍니다.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/b89aba2f-6c92-4f00-a51c-caae2903ae4a/Untitled.png)

1. 새로운 파일 만들기

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/68ee8e5f-3c9c-4c60-aeea-20b502b851fa/Untitled.png)

1. index.html 파일 만들기

<aside>
💡 index.html 파일은, 웹 브라우저가 특정 url에 처음 접근하였을때 읽어들이는 파일로, 어떤 화면을 첫 화면으로 보여줄지 결정해주는 역할을 합니다.

</aside>

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/0fe501b5-d176-45fc-b4dd-92df9292efef/Untitled.png)

1. 이제부터 본 repository는 아래 주소로 접속할 수 있습니다.

<aside>
💡 [https://](https://whdrns2013.github.io/)ID.github.io/

</aside>

# 깃허브 페이지 관리 툴 설치

## 1) Github Desktop 설치
1. 깃허브 데스크탑을 다운받습니다.

[GitHub Desktop](https://desktop.github.com/)

## 2) 코드 에디터 설치

1. 혹시 설치된 코드 에디터가 없다면, 코드 에디터를 설치합니다.

[Visual Studio Code - Code Editing. Redefined](https://code.visualstudio.com/)

### 깃허브 클론

1. 깃허브 데스크탑을 설치한 후, repository를 컴퓨터에 clone 해줍니다.

이 부분은 깃허브 설명 을 참고해주시기 바랍니다.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/a2250acb-8318-4a12-9595-460afc38ad82/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/33fedfcf-7fb2-4252-8064-d55f03f19261/Untitled.png)

1. 클론 후, repository → pull 을 클릭합니다.

pull 을 통해, 변경 사항을 동기화한 후에, history 탭을 확인해봅시다.

본 탭은, 해당 repository의 변경된 사항에 대한 history를 보여줍니다.

아까 만든 index.html 파일이 보이는군요! 

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/f9dbc1c2-c2d9-4677-980e-46b9451faed6/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/458c6e2d-0ab3-4e36-8a8b-e17ecf314181/Untitled.png)

### 에디터로 Repository 열기

1. Open the repository in your external editor

repository를 내가 사용하는 에디터로 여는 기능입니다.

저는 notepad++ 가 설치되어있어 기본으로 잡히는군요!

본인에게 익숙한 코드 에디터를 option에서 설정하여 사용하시기 바랍니다.

저는 VScode를 사용할 예정입니다.

에디터가 보이지 않을 때에는 다음 글을 참고해주세요 → 

[Github Desktop 에디터 추가](https://www.notion.so/Github-Desktop-7cb4cfdc2b41433fbe01aac4765098d6)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/41309104-0938-4279-a592-3afb218a3590/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/b5a75510-6b33-4ade-ae51-7b5f1ae139de/Untitled.png)

1. external editor로 열기를 선택하면, 해당 에디터가 열릴 것입니다.

그리고, github 사이트에서 만들었던 index.html 파일 또한 여기서 볼 수 있죠!

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/12e706c6-6ff9-4210-8081-5faef4a2b165/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/8dfb7f20-49d3-4a4e-b2dd-6cdb5e7a732d/Untitled.png)

1. 인덱스 파일이 보이는 김에, 간단한 문장을 작성해보자

텅 빈 인덱스 파일을 보니 너무 외롭습니다. 간단한 문장 하나를 적어보겠습니다.

삼촌께서 선물해주신 365일 문장달력 문구를 써봤습니다.

이후 꼭 저장!

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/5af516db-55f1-452e-9627-35a0d1c77243/Untitled.png)