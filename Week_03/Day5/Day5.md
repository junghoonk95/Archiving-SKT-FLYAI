# RNN (Recurrent Neural Network, 순환 신경망)

  - 입력과 출력을 시퀸스 단위로 처리
    - 스퀸스란 문장 같은 단어가 나열된 것
    - 이러한 시퀸스들을 처리하기 위해 고안된 모델을 시퀸스 모델
    - 그중에서 RNN은 딥러닝의 가장 기본적인 시퀸스 모델
    
      ![image](https://user-images.githubusercontent.com/80855939/210904365-c9a3a3e5-d8a7-4d32-9c63-4da62cd613a4.png)

    
    
  - 은닉층에서 활성화 함수를 통해 결과를 내보내는 역할을 하는 노드를 셀
    - 이 셀은 이전의값을 기억, 일종의 메모리 역할을 수행(메모리 셀)
    - 은닉상태 : 은닉층의 메모리 셀에서 나온 값이 다음 은닉층의 메모리 셀에 입력
    
    메모리 셀이 출력층 방향 또는 다음 시점인 t+1의 자신에게 보내는 값을 은닉 상태(hidden state) 
    
     ![image](https://user-images.githubusercontent.com/80855939/210904646-66e4743c-ac7d-460d-afde-b7d6a0d911e4.png)


  - RNN 종류
    - **일 대 다(One-to-Many)** : 하나의 입력에 대해서 여러개의 출력 
      - 하나의 이미지 입력에 대해서 사진의 제목을 출력하는 이미지 캡셔닝(Image Captioning) 작업

    - **다 대 일(Many-to-One)** : 단어 시퀀스에 대해서 하나의 출력
      - 구조의 모델은 입력 문서가 긍정적인지 부정적인지를 판별하는 감성 분류(sentiment classification)
      - 메일이 정상 메일인지 스팸 메일인지 판별하는 스팸 메일 분류(spam detection)

    - **다 대 다(Many-to-Many)** : 단어 시퀸스에 대하여 여러개의 출력
      -  사용자가 문장을 입력하면 대답 문장을 출력하는 챗봇 혹은 번역기(입력 문장으로부터 번역된 문장을 출력)


![image](https://user-images.githubusercontent.com/80855939/210920795-8fc77ae7-7bae-4416-ac14-ecbc051581e2.png)



  - SimpleRNN
    - 케라스 모듈중 하나로 하나의 시퀸스가 아닌 케라스 층과 마찬가지로 시퀸스 배치를 처리 해주는 층 

  ## 스펨메일 분류
  
> 참고 사이트 https://wikidocs.net/22894

![image](https://user-images.githubusercontent.com/80855939/210905602-49370b9e-a812-4472-9839-51a520747072.png)

- 데이터셋 확인

  ![dataset](https://wikidocs.net/images/page/22894/%ED%9B%88%EB%A0%A8%EB%8D%B0%EC%9D%B4%ED%84%B0.PNG)

  - v1 : 스팸인지 아닌지를 나타내는 레이블
  - v2 : 메일의 본문

### RNN vs CNN vs MLP vs SVM
<img src="https://user-images.githubusercontent.com/80855939/210919740-4500641f-94ce-4112-b1a8-2eb6c2987688.png" width=70% height=70%>
