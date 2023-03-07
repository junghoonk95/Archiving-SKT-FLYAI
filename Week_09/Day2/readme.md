# Microsoft cognitive service

## Computer Vision

- `computer vision`, `NLP` 등 여러가지 deep learning 서비스를 이용 가능

네트워크 계층

- 물리 계층
    - 물리적 전기적 표현, 케이블 종류 등
- 데이터링크 계층
    - 두 개의 노드 사이에 데이터 전송
    - mac 주소
- 위와 같이 7계층 까지 존재 (HTTP)

`GET`, `POST` 방식

```python
import requests

requests.get('http://naver.com').text
# 네이버 html 결과 return

key = '자신의 키 값'
endpoint = '자신의 엔드포인'

# 비전 서비스 버전 관리 
endpoint = endpoint + 'vision/v2.0/'
analyzeEndpoint = endpoint + 'analyze'

requests.get(image_url)
response.text

# 이미지 주소 받아서 출력
from io import BytesIO
from PIL import Image
image = Image.open(BytesIO(requests.get(image_url).content))
image

# 파라미터 정의 및 요청
headers = {'Ocp-Apim-Subscription-Key': key}
params = {'VisualFeatures':'Categories,Description,Color'}
data = {'url':image_url}
response = requests.post(analyzeEndpoint, headers=headers,params=params,json=data)

result = response.json()
result
"""
{'categories': [{'name': 'animal_dog', 'score': 0.99609375}],
 'color': {'dominantColorForeground': 'White',
  'dominantColorBackground': 'White',
  'dominantColors': ['White'],
  'accentColor': '8E633D',
  'isBwImg': False,
  'isBWImg': False},
 'description': {'tags': ['sitting',
   'cat',
   'brown',
   'indoor',
   'dog',
   'looking',
   'animal',
   'staring',
   'camera',
   'standing',
   'tan',
   'front',
   'table',
   'laying',
   'close',
   'orange',
   'bed'],
  'captions': [{'text': 'a close up of a dog and a cat looking at the camera',
    'confidence': 0.8600457150249555}]},
 'requestId': 'c941a29b-d781-47cb-b60b-55311c6e5eee',
 'metadata': {'height': 552, 'width': 570, 'format': 'Jpeg'}}
"""
# json parsing 해보기
result['description']['captions'][0]['text']

# Object Detection
detectEndpoint = endpoint + 'detect'
response = requests.post(detectEndpoint, headers=headers, params={}, json=data)
result = response.json()
result

# bouding box 만들기
for obj in result['objects']:
  print(obj)
from PIL import Image, ImageDraw, ImageFont
draw = ImageDraw.Draw(image)
def DrawImage(result):
  objects = result['objects']

  for obj in objects:
    print(obj)

    rect = obj['rectangle']
    x = rect['x']
    y = rect['y']
    w = rect['w']
    h = rect['h']

    draw.rectangle(((x,y),(x+w,y+h)), outline='red')

    draw.text((x,y),obj['object'],fill='red')
image
```
- 실행결과

![Untitled](https://user-images.githubusercontent.com/39786044/218895098-aab69e41-b009-40f7-83b8-3c8c3e0bdb21.png)

```python
ocrEndpoint = endpoint + 'ocr'
image_url = 'http://www.unikorea.go.kr/unikorea/common/images/content/peace.png'

image = Image.open(BytesIO(requests.get(image_url).content))
image

header = {'Ocp-Apim-Subscription-Key': key}
params = {'language': 'ko', 'dectOrientation': 'true'}
data = {'url': image_url}

response = requests.post(ocrEndpoint, headers = headers, params = params, json = data)
result = response.json()
result

lineinfos = [region['lines'] for region in result['regions']]
for line in lineinfos:
  for word_metadata in line:
    for word_inf in word_metadata['words']:
      print(word_inf['text'])
```

- 실행결과

![Untitled (1)](https://user-images.githubusercontent.com/39786044/218895241-1dc2f343-80cd-4f42-a7e9-e396f928e48d.png)
<img width="191" alt="Untitled (2)" src="https://user-images.githubusercontent.com/39786044/218895248-c27c2d46-f606-4a6d-9b37-78b63bd98444.png">
