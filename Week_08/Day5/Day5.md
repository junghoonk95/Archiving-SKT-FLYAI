## ****1. Github Actions 기반 CI/CD - Build와 Push****

### 실습
[Github_Actions_기반_CICD_-_Build_와_Push.pdf](https://github.com/SKT-FlyAi/SKT-FLYAI-Archiving/files/10719559/Github_Actions_._CICD_-_Build_._Push.pdf)


## ****2. Prometheus_Grafana****
### 1). Prometheus   
https://github.com/prometheus

Prometheus는 이벤트 모니터링 및 알림에 사용되는 자유 소프트웨어 응용 프로그램이다.
- 2012 년 SoundCloud 에서 만든 모니터링 & 알람 프로그램
- 2016 년 CNCF 에 Joined, 2018 년 Graduated 하여 완전 독립형 오픈소스 프로젝트로 발전
- 쿠버네티스에 종속적이지 않고, binary 혹은 docker container 형태로도 사용하고 배포 가능
- 쿠버네티스 생태계의 오픈소스 중에서는 사실상의 표준
- 구조가 쿠버네티스와 궁합이 맞고, 다양한 플러그인이 오픈소스로 제공
#### 특징
- 수집하는 Metric 데이터를 다차원의 시계열 데이터 형태로 저장
- 데이터 분석을 위한 자체 언어 PromQL 지원
- 시계열 데이터 저장에 적합한 TimeSeries DB 지원
- 데이터 수집하는 방식이 Pull 방식
  - 모니터링 대상의 Agent 가 Server 로 Metric을 보내는 Push 방식이 아닌, Server 가 직접 정보를 가져가는 Pull 방식
  - Push 방식을 위한 Push Gateway 도 지원
- 다양한 시각화 툴과의 연동 지원
- 다양한 방식의 Alarming 지원
#### 구조
![화면 캡처 2023-02-13 162134](https://user-images.githubusercontent.com/90374185/218395327-8fbc4c1f-03a8-4416-92d9-71a6b9837bf7.png)
![화면 캡처 2023-02-13 162434](https://user-images.githubusercontent.com/90374185/218395863-e3d82285-a576-44bc-8ccc-29446a83070d.png)
https://prometheus.io/docs/prometheus/latest/querying/basics/

#### 단점
- Scalability, High Availability
  - Prometheus Sever 가 Single node 로 운영되어야 하기 때문에 발생하는 문제
- ⇒ Thanos 라는 오픈소스를 활용해 multi prometheus server 를 운영  
https://thanos.io/

### 2). Grafana  
https://prometheus.io/docs/prometheus/latest/querying/basics/  
Grafana는 개방적이고 구성 가능한 관찰 및 데이터 시각화 플랫폼입니다.
- 2014 년 릴리즈된 프로젝트로 처음에는 InfluxDB, Prometheus 와 같은 TimeSeriesDB 전용 시각화 툴로 개발되었으나 이후 MySQL, PostgreSQL 과 같은 RDB 도 지원
- 현재는 Grafana Labs 회사에서 관리하고 있으며, 실습을 진행할 Open Source Project 인 Grafana 외에도 상용 서비스인 Grafana Cloud, Grafana Enterprise 제품 존재
  - 상용 서비스는 추가 기능을 제공하는 것뿐만 아니라 설치 및 운영 등의 기술 지원까지 포함
- playground 페이지도 제공하여 쉽고 간편하게 Grafana Dashboard 를 사용해볼 수 있음  
https://play.grafana.org/
- 마찬가지로 쿠버네티스에 종속적이지는 않고 docker 로 쉽게 설치할 수는 있지만, 여러 Datasource 와의 연동성이 뛰어나고 특히 Prometheus 와의 연동이 뛰어나 함께 발전

### 실습
[Prometheus__Grafana_실습.pdf](https://github.com/SKT-FlyAi/SKT-FLYAI-Archiving/files/10719580/Prometheus__Grafana_.pdf)

## ****3. DVC( Data version control )****

DVC는 Data Version Control 의 약자로, 머신러닝 프로젝트에서 모델과 데이터의 버전 관리를 위한 오픈 소스이다.  
머신러닝 파이프라인에서 데이터나 데이터 처리 방식, 모델 등이 바뀌는 일이 빈번하게 발생하는데, 이 과정에서 모델에 문제가 발생하게 되면 이전 버전의 모델을 가져와야 하는데, 이러한 작업을 효율적으로 할 수 있도록 버전 관리를 도와주는 도구가 DVC이다.  

- 대부분의 스토리지와 호환된다 ( amazon s3, google drive, … )
- GitHub 외의 GitLab, Bitbucket 등의 대부분의 git 호스팅 서버와 연동된다
- Data Pipeline을 DAG로 관리
- Git과 유사한 인터페이스

외부 플러그인  
https://grafana.com/grafana/plugins/
 
다양한 Grafana Dashboard  
https://grafana.com/grafana/dashboards/


### 실습
[DVC_실습.pdf](https://github.com/SKT-FlyAi/SKT-FLYAI-Archiving/files/10719584/DVC_.pdf)


## ****4. MLflow****
MLflow란 머신러닝 모델의 실험을 tracking하고, 모델을 공유 및 배포할 수 있도록 지원하는 라이브러리다.  
즉, 머신러닝 학습과 관련된 전반적인 cycle을 지원해주는 라이브러리이다.  

### 기능
#### 1. MLflow Tracking
  - 머신러닝 모델을 학습시킬 때 생기는 각종 파라미터, 그리고 머신러닝 모델 트레이닝이 끝난 후 metric의 결과 등을 로깅하고 그 기록 결과를 웹 UI로도 확인할 수 있다.
#### 2. MLflow Projects
  - Anaconda나 Docker 등을 사용하여 만들어 둔 모델을 reproducible 하고 실행할 수 있도록 코드 패키지 형식으로 지원해준다. 이러한 형식으로 만드렁진 환경을 재사용할 수 있다.
#### 3. MLflow Models
  - 동일한 모델을 Docker, Apache Spark, AWS 등에서 쉽게 배치할 수 있도록 지원한다.
#### 4. MLflow Model Registry
  - MLflow 모델의 전체 라이프 사이클을 공통으로 관리하기 위한 centralized model store, set of API, UI

### 실습
[MLflow_실습_1.pdf](https://github.com/SKT-FlyAi/SKT-FLYAI-Archiving/files/10719591/MLflow_._1.pdf)  
[MLflow_실습_2.pdf](https://github.com/SKT-FlyAi/SKT-FLYAI-Archiving/files/10719593/MLflow_._2.pdf)  
[MLflow_실습_3.pdf](https://github.com/SKT-FlyAi/SKT-FLYAI-Archiving/files/10719594/MLflow_._3.pdf)  
[MLflow_실습_4.pdf](https://github.com/SKT-FlyAi/SKT-FLYAI-Archiving/files/10719595/MLflow_._4.pdf)  
