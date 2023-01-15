## Pillow - Image

> * import : from PIL import Image  
> 파이썬에서 이미지를 다루는 라이브러리입니다.  
> 이하는 Pillow의 Image 모듈에 대해 다룹니다.

### 주요 메서드

|메서드명|설명|파라미터|
|---|---|---|
|변수 = Image.open(path, mode=)|이미지 불러오기|* path : 이미지파일 경로명 * mode =str (r:읽기)|
|변수.show()|불러온 이미지를 출력||
|Image.save(path, format)|이미지 저장하기|*path : srt / *format : jpg, bmp 등|


### 이미지 포맷
|이미지 포맷|읽기 지원|쓰기 지원|
|---|---|---|
|BMP|O|O|
|GIF|O|O|
|JPEG|O|O|
|PNG|O|O|
|TIFF|O|O|
|Webp|O|O|
|BLP|O|X|
|DCX|O|X|
|DDS|O|X|
|PSD|O|X|
|PDF|X|O|
|PALM|X|O|
|이외도 많음...|||





## 레퍼런스

https://appia.tistory.com/353