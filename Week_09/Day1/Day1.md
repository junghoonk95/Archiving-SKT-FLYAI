# MLOps

## 1. MLOps란?

- Machine Learning Process에서 AI 모델 알고리즘을 설계하는 일은 전체 프로세스 중 극히 일부
- 데이터 준비하고 개발환경 세팅하는 게 훨씬 더 많은 부분을 차지
- 모델의 배포 및 운영 문제 고민 → 효과적으로 운영하기 위해 컨테이너 도입

![image](https://user-images.githubusercontent.com/79077316/218382681-00a815ab-6bce-4841-83b7-2a89e33b94a5.png)

- **MLOps** = 머신러닝 엔지니어링 + 데이터 엔지니어링 + 인프라 + Ops
    - MLOps는 머신러닝 모델 개발과 머신러닝 모델 운영에서 사용되는 문제, 반복을 최소화하고 비즈니스 가치를 창출하는 것이 목표
    - 모델링에 집중할 수 있도록 관련된 인프라를 만들고, 자동으로 운영되도록 함
    - 예) API 형태로 서버 만들기, 실험 파라미터와 결과 저장하기, 모델 결과 자동화하기, 데이터 Validation 등
- Research와 Production의 머신러닝

![image](https://user-images.githubusercontent.com/79077316/218382705-3acb6b97-626b-4444-9a3b-a8665f60173e.png)


## 2. MS Azure Machine Learning

- `Azure Machine Learning` 머신러닝 워크스페이스 만들기
![image](https://user-images.githubusercontent.com/79077316/218382996-1a59df2a-0005-4f62-ad00-9789a2c0ad48.png)

- `Azure Machine Learning Studio` 에서 compute instance 만들기
![image](https://user-images.githubusercontent.com/79077316/218383033-7b76d649-3ead-4426-9df2-97dc03804f21.png)

- `Automated ML` 에서 new job 만들기
    - Create data assset - **TitanicDataset** 만들기
    - Choose a source for your data asset - **From local file** 선택하고 `titanic_train.csv` 파일 업로그하기

![image](https://user-images.githubusercontent.com/79077316/218383074-ce6954b1-d323-4532-824c-3efae0ada6a8.png)
![image](https://user-images.githubusercontent.com/79077316/218383111-7577e553-5227-41c5-b2b8-8a3b6d13ceff.png)
![image](https://user-images.githubusercontent.com/79077316/218383123-45688324-2eed-48c8-91d2-a5080944383e.png)

## 3. Notebooks

- `Notebooks` 에서 주피터노트북 만들기
![image](https://user-images.githubusercontent.com/79077316/218383167-44744417-e668-4823-ab00-51e1dbd1fdc2.png)
- 자세한 노트북 Code는 본 폴더 'azure-mlops.ipynb' 확인
