## 챗봇

자연어처리를 통해 구현된다.

챗봇 : 대화형식

질문 > 답변이 반복되는 방식이다.

이러한 챗봇은 의도 파악 후 답변을 잘 하는지가 중요하다.

## Chat GPT

[OpenAI](https://openai.com/)

## KoGPT2 활용해서 간단한 챗봇 만들기

[KoGPT2_챗봇_ipynb의_사본](Week_07/Day1/KoGPT2_챗봇_ipynb의_사본.ipynb)

## 나만의 데이터셋으로 KoGPT2 활용해서 챗봇 만들기

## Docker에 구동하기 환경설정
### Windows 10 환경에서 Docker에 Ubuntu 설치

[[Docker] Windows10 환경에서 Docker에 Ubuntu 설치](https://hermeslog.tistory.com/498)

#### 1. 버전 확인
```bash
docker version
```
![image](https://user-images.githubusercontent.com/90374185/215736106-e9d5c4f5-e0be-4460-82b2-8d7af881134f.png)


#### 2. docker 우분투 찾기

![image](https://user-images.githubusercontent.com/90374185/215736837-76b7d35c-b823-429d-85e1-fe03e777db52.png)

#### 3. docker 우분투 내려받기
    
```bash
docker pull mysql 로 하지 말고
docker pull mysql:8.0.22로 버전을 지정해줘야 한다.
```

![image](https://user-images.githubusercontent.com/90374185/215736878-e5d43716-f106-4728-8bb9-589bef8fbd2d.png)

#### 4. docker 이미지를 Container 파일로 생성한다.
```bash
docker create -it --name ubuntu_server ubuntu:20.04
```
![image](https://user-images.githubusercontent.com/90374185/215736930-6bd18e9c-6779-47eb-81b5-49ad0fc96f39.png)

#### 5. docker에서 start 버튼으로 서버 실행
#### 6. docker 우분투 서버 접속
```bash
docker attach ubuntu_server
```

![image](https://user-images.githubusercontent.com/90374185/215736971-85b5de4b-8dd3-4b3d-8d32-4809ca3aa662.png)

cd / : 루트로 이동

ll : 파일 리스트

#### 7. docker 우분투 업그레이드
```bash
apt-get update
```

![image](https://user-images.githubusercontent.com/90374185/215737006-13f1fcb6-6f7d-4d61-8e71-43463821f537.png)

### 우분투 업그레이드시 에러 고치는법
```bash
Some index files failed to download. They have been ignored, or old ones used instead.
```
업그레이드 시 해당 에러가 발생한다면

먼저 apt-get install vim 또는 apt-get install nano를 통해 진행한다.

[[Linux] 리눅스 텍스트 에디터 vi와 vim, nano, gedit 차이 설명](https://blog.naver.com/PostView.naver?blogId=ycpiglet&logNo=222367301056)

[sudo apt-get upgrade 다운로드 서버 변경](https://wooriel.tistory.com/3)

vim을 통해서 외국 주소를 한국 주소로 바꿔주면 에러가 해결된다.

