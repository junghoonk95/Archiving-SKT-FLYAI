# 1. 딥러닝 종류

- 신경망 구성 방식에 따라 여러 종류로 구분됨

- **Computer Vision** : 
  - CNN(Convolution Neural Network) : 이미지 인식하는 딥러닝 모델, 컨볼루션 기법을 사용해 이미지 속 특징을 추출
  - GAN(Generative Adversarial Network) : 생성자와 식별자로 구성돼 이미지 생성과 판단을 반복하면서 고품질의 이미지를 생성하는 딥러닝 모델

- **Natural Language Processing** : 
  - Transformer: 자연어 처리하는 딥러닝 모델, 인코더(입력문장->벡터 변환)->디코더(벡터->새로운 문장) 구조를 통해 번역, 챗봇에 많이 활용됨
    - [Self-Attention ](https://aimb.tistory.com/182)기법을 통해 높은 성능을 보임
    - BERT : Transformer의 **인코더 부분**만 분리하여 활용한 모델, 문장 의미 분류에 활용
    - GPT : Transformer의 **디코더 부분**만 분리하여 활용한 모델, 문장 작성에 활용
  
- **Reinforcement Learning** : 
  - 학습 데이터가 필요없음
  - 가상 또는 실제 환경에서 행동을 수행하고 그에 대한 보상을 받으며 스스로 학습함
  - 체스, 바둑, 로봇과 같이 연속적인 행동의 순서를 결정하는데 많이 사용
