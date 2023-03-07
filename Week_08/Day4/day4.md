[Kubernetes 강의_Jsy.zip](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/135110d2-4ed3-4cbe-b4ab-1a745ab6fe3d/Kubernetes_강의_Jsy.zip)

[Docker 강의_Jsy.zip](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/95116849-7cf4-4937-884d-6d7d592c1b88/Docker_강의_Jsy.zip)

[Jenkins 강의_Jsy.zip](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/a5230763-6fd6-4429-b9d2-3b3b0b567705/Jenkins_강의_Jsy.zip)

[Git_GitHub 강의_Jsy.zip](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/8617e8dc-35f2-4cb5-bcfb-f6969a456eea/Git_GitHub_강의_Jsy.zip)

# Jenkins

- https://www.jenkins.io/

- CNCF CI/CD 종류

  [Cloud Native Landscape](https://landscape.cncf.io/card-mode?category=continuous-integration-delivery&grouping=category)

- What is Jenkins?

  - 젠킨스는 소프트웨어 개발 시 빌드, 테스트, 배포 프로세스를 자동화해주는 지속적인 통합 (CI, Continous Integration) 서비스를 제공하는 툴이다.
  - 다수의 개발자들이 하나의 프로그램을 개발할 때 버전 충돌을 방지하기 위해 각자 작업한 내용을 공유 영역에 있는 저장소에 빈번히 업로드함으로써 지속적 통합이 가능하도록 해준다.
  - 원래 허드슨 프로젝트에서 Java로 개발되었고, 허드슨의 개발은 2004년 여름 썬 마이크로 시스템즈에서 시작되었다. 그리고 2005년 2월에 java.net에 처음 출시되었다. 오라클과의 분쟁으로 허드슨으로부터 분기 후 2011년 2월 2일 Jenkins로 출시되었다.
  - 젠킨스와 같은 CI툴이 등장하기 전에는 일정 시간마다 빌드를 실행하는 방식이 일반적이었다. 특히 개발자들이 당일 작성한 소스들의 커밋이 모드 끝난 심야 시간대에 이러한 빌드가 타이머에 의해 집중적으로 진행되었는데, 이를 nightly-build라 한다. 하지만, 젠킨스는 정기 적인 빌드에서 한발 나아가 서브버전, Git 과 같은 버전관리시스템과 연동하여 소스의 커밋을 감지하면 자동적으로 자동화 테스트가 포함된 빌드가 작동되도록 설정할 수 있다.

![1](https://user-images.githubusercontent.com/53481614/218345677-efd53abf-84bd-40db-9df5-42d15254199b.jpg)

- 젠킨스가 주는 이점
  - 개발중인 프로젝트에서 커밋은 매우 빈번히 일어나기 때문에 커밋 횟수만큼 빌드를 실행하는 것이 아니라 작업이 큐잉되어 자신이 실행될 차례를 기다리게 된다코드의 변경과 함께 이뤄지는 이 같은 자동화된 빌드와 테스트 작업들은 다음과 같은 이점들을 가져다 준다.
    - 프로젝트 표준 컴파일 환경에서의 컴파일 오류 검출
    - 자동화 테스트 수행
    - 정적 코드 분석에 의한 코딩 규약 준수 여부 체크
    - 프로파일링 툴을 이용한 소스 변경에 따른 성능 변화 감시
    - 결합 테스트 환경에 대한 배포작업
  - 이 외에도 젠킨스는 1400여가지가 넘는 플러그인을 온라인으로 간단히 인스톨 할 수 있는 기능을 제공하고 있으며 파이썬과 같은 스크립트를 이용해 손쉽게 자신에게 필요한 기능을 추가 할 수도 있다.

![2](https://user-images.githubusercontent.com/53481614/218345755-e03ffcd8-28ca-4837-b373-b3e38a842afb.jpg)


- 각종 배치 작업의 간략화

  - 프로젝트 기간 중에 개발자들은 순수한 개발 작업 이외에 DB셋업이나 환경설정, Deploy작업과 같은 단순 작업에 시간과 노력을 들이는 경우가 빈번하다. 데이터베이스의 구축, 어플리케이션 서버로의 Deploy, 라이브러리 릴리즈와 같이 이전에 CLI로 실행되던 작업들이 젠킨스 덕분에 웹 인터페이스로 손쉽게 가능해졌다.

- Build 자동화의 확립

- 빌드 툴의 경우 Java는 maven과 gradle이 자리잡고 있으며, 이미 빌드 관리 툴을 이용해 프로젝트를 진행하고 있다면 젠킨스를 사용하지 않을 이유가 하나도 없다. 젠킨스와 연동하여 빌드 자동화를 통해 프로젝트 진행의 효율성을 높일 수 있다.

- 자동화 테스트

  - 자동화 테스트는 젠킨스를 사용해야 하는 가장 큰 이유 중 하나이며, 사실상 자동화 테스트가 포함되지 않은 빌드는 CI자체가 불가능하다고 봐도 무방하다. 젠킨스는 Subversion이나 Git과 같은 버전관리시스템과 연동하여 코드 변경을 감지하고 자동화 테스트를 수행하기 때문에 만약 개인이 미처 실시하지 못한 테스트가 있다 하여도 든든한 안전망이 되어준다. 제대로 테스트를 거치지 않은 코드를 커밋하게 되면 화난 젠킨스를 만나게 된다.

- 코드 표준 준수여부 검사

  - 자동화 테스트와 마찬가지로 개인이 미처 실시하지 못한 코드 표준 준수 여부의 검사나 정적분석을 통한 코드 품질 검사를 빌드 내부에서 수행함으로써 기술적 부채의 감소에도 크게 기여한다.

- 빌드 파이프라인 구성

  - 2개 이상의 모듈로 구성되는 레이어드 아키텍처가 적용 된 프로젝트에는 그에 따는 빌드 파이프라인 구성이 필요하다. 예를 들면, 도메인 -> 서비스 -> UI와 같이 각 레이어의 참조 관계에 따라 순차적으로 빌드를 진행하지 않으면 안된다. 젠킨스에서는 이러한 빌드 파이프라인의 구성을 간단히 할 수 있으며, 스크립트를 통해서 매우 복잡한 제어까지도 가능하다.

- **Jenkins 특징**

  - Jenkinsfile
  - Jenkinsfile을 이용해 Job 혹은 파이프라인을 정의할 수 있다. Jenkinsfile 덕분에 일반 소스코드를 다루는 Github 업로드, Vscode 로 수정하는 것으로 파일을 이용할 수 있음
  - 기본적으로 Jenkinsfile을 통해 젠킨스를 실행함

- Scripted Pipeline(스크립트 파이프라인)

  - Jenkins 관련 구조를 자세히 가지지 않고 프로그램의 흐름을 Groovy 라는 동적 객체 지향 프로그래밍 언어를 이용해 관리되었음 Java 가상머신에서 동작하고 Java와 유사함
  - 매우 유연하지만 Groovy를 알아야하므로 진입장벽이 있음.

  ```groovy
  node { ## 빌드를 수행할 node 또는 agent를 의미한다.
  	stage("Stage 1"){
  		echo "Hello"
  	}
  	stage("Stage 2"){
  		echo "World"
  		sh "sleep 5"
  	}
  	stage("Stage 3"){
  		echo "Good to see you!"
  	}
  }
  ```
  
![3](https://user-images.githubusercontent.com/53481614/218346024-cd8cdadf-300e-455c-904f-713b8594111c.jpg)

- Declarative Pipeline (선언적 파이프라인)

  - 2016년 경 Cloudbees 에서 개발
  - 사전에 정의된 구조만 사용할 수 있기 때문에 CI/CD 파이프라인이 단순한 경우에 적합하며 아직은 많은 제약사항이 따른다
  - 공식문서

  [Pipeline Syntax](https://www.jenkins.io/doc/book/pipeline/syntax/)

# Jenkins 설치

- JDK  설치

```bash
sudo apt install openjdk-11-jre-headless
```

- Key 다운로드

```bash
# Jenkins 저장소 Key 다운로드
wget -q -O - <https://pkg.jenkins.io/debian/jenkins.io.key> | sudo apt-key add -

# sources.list 에 추가
echo deb <http://pkg.jenkins.io/debian-stable> binary/ | sudo tee /etc/apt/sources.list.d/jenkins.list

# Key 등록
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys FCEF32E745F2C3D5
```

- Jenkins 설치하기

```bash
sudo apt-get update

# 정상여부 확인
sudo apt-get install jenkins
sudo systemctl status jenkins
```

- 설치시 에러 발생

![4](https://user-images.githubusercontent.com/53481614/218346046-71c67c17-450a-4773-9698-cdd2575b20dd.jpg)

- 해결방안

```bash
sudo apt remove jenkins

sudo apt install openjdk-11-jdk

# 환경에 따라 openjdk-11-jre-headless로 하면 안되는 경우가 있음
sudo apt install jenkins
```

- 초기 패스워드 확인

```bash
sudo cat /var/lib/jenkins/secrets/initialAdminPassword
```

![5](https://user-images.githubusercontent.com/53481614/218346074-00a2978b-4d23-4694-8d5a-9472ea236b9c.jpg)

- 우분투 Firefox에서 [localhost:8080](http://localhost:8080) 입력 후  패스워드 입력
- 플러그인 설

![6](https://user-images.githubusercontent.com/53481614/218346093-bc9cd387-6d8e-45fc-a9ee-17da1e4b3837.jpg)

- 계정 만들기
  - id : admin_user
  - pw : 1234

# Jenkins CI Pipeline 생성 실습

- 기본 코드 구조(Section)

  - pipeline : 반드시 맨 위에 있어야 한다. 일종의 작업명세서. CI/CD flow를 젠킨스에 구현하기 위한 일련의 플러그인의 집합이자 구성이며 젠킨스의 핵심 플러그인. 젠킨스는 여러 플러그인들을 pipeline에서 용도에 맞게 사용하고 정의함으로써 CI/CD를 할 수 있게 해주는 도구.

  - agent : 어디에서 실행할 것인지 정의한다. 여러 slave node 를 두고 일을 시킬 수 있는데 어떤 젠킨스가 일을 하게 할 것 인지를 지정한다. 젠킨스 노드 관리에서 새로 노드를 띄우거나 혹은 docker 이미지 등을 통해서 처리할 수 있음

    - any, none, label, node, docker, dockerfile, kubernetes
    - agent 가 none 인 경우 stage 에 포함시켜야 함

```yaml
pipeline {
   agent none
   stages {
      stage('Example Build') {
         agent { docker 'maven:3-alpine' }
         steps {
            echo 'Hello, Maven'
            sh 'mvn --version'
         }
      }
      stage('Example Test') {
         agent { docker 'openjdk:8-jre' }
         steps {
            echo 'Hello, JDK'
            sh 'java -version'
         }
      }
   }
}
```

- stages : 어떤 일들을 처리할 건지 일련의 stage를 정의(카테고리)

  - pipeline 블록 안에서 한 번만 실행 가능

- 깃허브 레포지터리 [js-pipeline-project]로 생성

- Locla(윈도우PC)에서 ‘Jenkinsfile’ 파일 생성하여 위 stages 코드 복사한 후 Github 업로드

- 주소

  - https://github.com/gj1515/js-pipeline-project.git

- vs code에서 Jenkinsfile 생성

```yaml
pipeline {
   agent any
   stages {
      stage("build") {
         steps {
            echo 'building the applicaiton...'
         }
      }
      stage("test") {
         steps {
            echo 'testing the applicaiton...'
         }
      }
      stage("deploy") {
         steps {
            echo 'deploying the applicaiton...'
         }
      }
   }
}
git init
git remote add origin <github 주소>

#Jenkinsfile을 위 코드로 생성

git add .
git commit -m "first commit"
#git config --global
git push origin
```

## Jekins에서

- create a job 선택

![7](https://user-images.githubusercontent.com/53481614/218346110-f32e15b6-8150-43b3-8af1-67c6bfe5d098.jpg)

- 지금 빌드
  - 오류발생
  - 오류 해결 : Branches to build를 master에서 main으로 변경
- 지금빌드

![8](https://user-images.githubusercontent.com/53481614/218348555-f8009dba-aca3-4d10-a0b1-8b2cf16e36d7.jpg)

- Jenkinsfile 코드 수정

```yaml
pipeline {
   agent any
   stages {
      stage("build") {
         when {
            expression {
               env.GIT_BRANCH == 'origin/main'
            }
         }
         steps {
            echo 'building the applicaiton...'
         }
      }
      stage("test") {
         when {
            expression {
               env.GIT_BRANCH == 'origin/test' || env.GIT_BRANCH == ''
            }
         }
         steps {
            echo 'testing the applicaiton...'
         }
      }
      stage("deploy") {
         steps {
            echo 'deploying the applicaiton...'
         }
      }
   }
}
git add .
git commit -m "second commit"
git push origin
```

## Jenkins에서 Pipeline Job을 생성하고 빌드

- Pipeline 생성
  - Create a job → pipeline 선택
  - 이름은 ‘jenkins-pipeline’으로 입력
- Git 추가
  - Pipeline
    - Definition → Pipeline script from SCM
    - SCM → Git
    - Repository URL 입력
    - Credentials - 현재 public으로 생성했으므로 생략
    - [Save] - Log 출력
- Pipeline Status 확인
  - 각 stage log 확인
  - Build Now
  - Build History → 해당 빌드 번호 선택
  - Console Output

## post를 이용해 모든 stage가 실행된 후의 명령을 정의

- post 조건
  - always, changed, fixed, regression, aborted, success, unsuccessful, unstable, failure, notBuilt, cleanup

```yaml
pipeline {
   agent any
   stages {
      stage("build") {
         steps {
            echo 'building the applicaiton...'
         }
      }
      stage("test") {
         steps {
            echo 'testing the applicaiton...'
         }
      }
      stage("deploy") {
         steps {
            echo 'deploying the applicaiton...'
         }
      }
   }
   post {
      always {
         echo 'building..'
      }
      success {
         echo 'success'
      }
      failure {
         echo 'failure'
      }
   }
}
```

- git push

```bash
git add .
git commit -m "post test commit”
git push origin main
```

- 젠킨스 → Build Now

## when을 이용해 stage가 실행되는 조건을 추가

- when 조건 추가
  - test stage 에서 Branch 이름에 따른 조건 추가
  - build stage 에서 Branch 이름에 따른 조건 추가
  - deploy stage의 steps에 echo "${env.GIT_BRANCH}” 추가 후 현재 branch 이름 확인

```yaml
pipeline {
   agent any
   stages {
      stage("build") {
         when {
            expression {
               env.GIT_BRANCH == 'origin/main'
            }
         }
         steps {
            echo 'building the applicaiton...'
         }
      }
      stage("test") {
         when {
            expression {
               env.GIT_BRANCH == 'origin/test' || env.GIT_BRANCH == ''
            }
         }
         steps {
            echo 'testing the applicaiton...'
         }
      }
      stage("deploy") {
         steps {
            echo 'deploying the applicaiton...'
         }
      }
   }
}
```

- **Jenkinsfile 환경변수를 설정**

  - Jenkinsfile 자체 환경변수 목록 보기

    - http://localhost:8080/env-vars.html/ 접속 / 또는 Jenkins pipeline-syntax 참고

  - Custom 환경변수 사용

    - echo 사용 시 큰 따옴표 주의

```yaml
pipeline {
   agent any
   environment {
      NEW_VERSION = '1.0.0'
   }
   stages {
      stage("build") {
         steps {
            echo 'building the applicaiton...'
            echo "building version ${NEW_VERSION}"
         }
      }
      stage("test") {
         steps {
            echo 'testing the applicaiton...'
         }
      }
      stage("deploy") {
         steps {
            echo 'deploying the applicaiton...'
         }
      }
   }
}
```

- Credentials 자격 증명 환경 변수로 사용하기

  - Jenkins credential 추가
    - [Jenkins 관리]-[Manage Credentials]-[Global credentials]-[Add credentials]
    - Username : admin_user / Password : 1234 / ID : admin_user_credentials
  - Jenkinsfile 에서 환경변수로 사용

```yaml
pipeline {
   agent any
   environment {
      NEW_VERSION = '1.0.0'
      ADMIN_CREDENTIALS = credentials('admin_user_credentials')
   }
   stages {
      stage("build") {
         steps {
            echo 'building the applicaiton...'
            echo "building version ${NEW_VERSION}"
         }
      }
      stage("test") {
         steps {
            echo 'testing the applicaiton...'
         }
      }
      stage("deploy") {
         steps {
            echo 'deploying the applicaiton...'
            echo "deploying with ${ADMIN_CREDENTIALS}"
            sh 'printf ${ADMIN_CREDENTIALS}'
         }
      }
   }
}
```

![9](https://user-images.githubusercontent.com/53481614/218346141-a04df57b-b616-47dd-a810-ad6382ffec21.jpg)

- Jenkins 플러그인 중 Credentials Plugin 확인

![8](https://user-images.githubusercontent.com/53481614/218345881-567645f8-d22c-4407-9711-44d3656bc6e0.jpg)

- https://javadoc.jenkins-ci.org/plugin/credentials-binding/index.html?org/jenkinsci/plugins/credentialsbinding/impl/UsernamePasswordMultiBinding.DescriptorImpl.html

```yaml
pipeline {
   agent any
   environment {
      NEW_VERSION = '1.0.0'
   }
   stages {
      stage("build") {
         steps {
            echo 'building the applicaiton...'
            echo "building version ${NEW_VERSION}"
         }
      }
      stage("test") {
         steps {
            echo 'testing the applicaiton...'
         }
      }
      stage("deploy") {
         steps {
            echo 'deploying the applicaiton...'
            withCredentials([[$class: 'UsernamePasswordMultiBinding',
               credentialsId: 'admin_user_credentials',
               usernameVariable: 'USER',
               passwordVariable: 'PWD'
	    ]]) {
               sh 'printf ${USER}'
            }
         }
      }
   }
}
```

## parameter

- Jenkinsfile에 parameter 추가
- Build with Parameters 메뉴로 확인

```yaml
pipeline {
   agent any
   parameters {
      string(name: 'VERSION', defaultValue: '', description: 'deployment version')
      choice(name: 'VERSION', choices: ['1.1.0','1.2.0','1.3.0'], description: '')
      booleanParam(name: 'executeTests', defaultValue: true, description: '')
   }
   stages {
      stage("build") {
         steps {
            echo 'building the applicaiton...'
         }
      }
      stage("test") {
         steps {
            echo 'testing the applicaiton...'
         }
      }
      stage("deploy") {
         steps {
            echo 'deploying the applicaiton...'
         }
      }
   }
}
```

- execute Tests가 true인 경우의 조건 추가해보기

- 실제 Jenkinsfile에 적용

  - Build with Parameters 실행
    - 1.2.0 버전 선택
    - execute Tests 선택 해제
  - test stage를 건너뛰고 실행되는지 확인

```yaml
pipeline {
   agent any
   parameters {
      choice(name: 'VERSION', choices: ['1.1.0','1.2.0','1.3.0'], description: '')
      booleanParam(name: 'executeTests', defaultValue: true, description: '')
   }
   stages {
      stage("build") {
         steps {
            echo 'building the applicaiton...'
         }
      }
      stage("test") {
         when {
            expression {
               params.executeTests
            }
         }
         steps {
            echo 'testing the applicaiton...'
         }
      }
      stage("deploy") {
         steps {
            echo 'deploying the applicaiton...'
            echo "deploying version ${params.VERSION}"
         }
      }
   }
}
```

- script.groovy 파일 생성

```yaml
def buildApp() {
   echo 'building the applications...'
}

def testApp() {
   echo 'testing the applications...'
}

def deployApp() {
   echo 'deploying the applicaiton...'
   echo "deploying version ${params.VERSION}"
}
return this
```

- jenkinsfile 업데이트

```yaml
pipeline {
   agent any
   parameters {
      choice(name: 'VERSION', choices: ['1.1.0','1.2.0','1.3.0'], description: '')
      booleanParam(name: 'executeTests', defaultValue: true, description: '')
   }
   stages {
      stage("init") {
         steps {
            script {
               gv = load "script.groovy"
            }
         }
      }
      stage("build") {
         steps {
            script {
               gv.buildApp()
            }
         }
      }
      stage("test") {
         when {
            expression {
               params.executeTests
            }
         }
         steps {
            script {
               gv.testApp()
            }
         }
      }
      stage("deploy") {
         steps {
            script {
               gv.deployApp()
            }
         }
      }
   }
}
```

- Jenkinsfile의 모든 환경변수는 groovy script에서 사용 가능
- Github Repo에 반영하고 실행/로그 확인
- 빌드 결과 확인
- Replay에서 수정 후 빌드 다시 실행
  - testApp에 echo ‘Replay’를 추가 후 다시 빌드
  - script 확인

![9](https://user-images.githubusercontent.com/53481614/218345903-3f9a3437-b8ff-4dbe-9e8c-3efa4ab2adad.jpg)

# 파이썬 기반 Jenkins CI Pipeline 생성 실습

<aside> 💡 실습 목표

1. 앞에서 배운 Jenkins CI Pipeline 생성을 Python 어플리케이션에 적용해 본다.
2. Github 에 Push 시 자동으로 배포하는 trigger 를 설정해 본다.
3. 배포된 Docker image 를 Docker Hub 로 올리기

</aside>

**앞에서 배운 Kenkins CI Pipeline 생성을 Python 어플리케이션에 적용해 본다.**

- FastAPI 예제 코드를 생성하여 서버에서 Docker Container를 실행한다.

  - 로컬에서 app/main.py 생성

  ```jsx
  from fastapi import FastAPI
  
  app = FastAPI()
  
  @app.get("/")
  def read_root():
      return {"Hello": "MLOps"}
  
  @app.get("/items/{item_id}")
  def read_item(item_id: int, q: str = None):
      return {"item_id": item_id, "q": q}
  ```

  - app/requirments.txt

  ```jsx
  fastapi
  uvicorn
  ```

  - Dockerfile 작성

  ```jsx
  FROM python:3.9
  
  WORKDIR /appfa
  COPY ./app/requirements.txt /app/requirements.txt
  
  RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
  
  COPY ./app /app
  
  CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
  ```

  - docker-compose.yml (**쉘 명령어로 대체 가능**)

  ```jsx
  version: "3"
  
  services:
    web:
      build: .
      container_name: fastapi-app
      volumes:
        - .:/code
      ports:
        - "80:80"
  ```

  ```jsx
  git add, commit, push
  ```

  - 서버에서 git clone

  ```jsx
  git clone -b main <본인 깃 주소>
  cd js-pipeline-project
  ```

  - 서버에서 docker-compose 설치

  ```jsx
  sudo apt install docker-compose
  ```

  - 서버에서 Docker Container 생성(**테스트용**)

  ```jsx
  docker-compose build web
  docker images
  docker-compose up -d
  docker ps -a
  ```

  - [localhost:80](http://localhost:80) 접속해 확인
  - Docker stop (진행 안하면 젠킨스에서 에러 발생)

  ```jsx
  docker ps -a
  docker stop fastapi-app
  docker re fastapo-app
  ```

- Jenkinsfile을 작성하여 Jenkins에서 배포해 본다.

  - docker group에 jenkins 등록 (젠킨스에서 도커를 사용할 수 있도록)

    - sudo gpasswd -a jenkins docker
    - sudo vi /usr/lib/systemd/system/docker.service (에러 발생 시에만 시도)

    ```jsx
    ExecStart=/usr/bin/dockerd -H fd:// -H tcp://0.0.0.0:2376 --containerd=/run/containerd/containerd.sock
    ```

    - sudo systemctl daemon-reload
    - sudo systemctl restart docker
    - sudo service jenkins restart

  - 로컬에서 Kenkinsfile 생성 **sh "docker-compose up -d"는 제외 가능**

  ```python
  pipeline {
     agent any
     parameters {
        choice(name: 'VERSION', choices: ['1.1.0','1.2.0','1.3.0'], description: '')
        booleanParam(name: 'executeTests', defaultValue: true, description: '')
     }
     stages {
        stage("init") {
           steps {
              script {
                 gv = load "script.groovy"
              }
           }
        }
        stage("Checkout") {
           steps {
              checkout scm
           }
        }
        stage("Build") {
           steps {
              sh 'docker-compose build web'
           }
        }
        stage("test") {
           when {
              expression {
                 params.executeTests
              }
           }
           steps {
              script {
                 gv.testApp()
              }
           }
        }
        stage("deploy") {
           steps {
              sh "docker-compose up -d"
           }
        }
     }
  }
  ```

  ```python
  git add, commit, pish
  ```

### Github에 Push 시 자동으로 배포되는 trigger를 설정해 본다.

- Jenkins pipeline 의 구성 General에서 Github Project 주소를 입력해서 바로 가도록 설정해 본다.
- Poll SCM 으로 매 시간마다 소스가 변경되었는지 확인
  - 예) H/1 * * * * → 1분마다 소스가 변경되었는지 확인

- 아래 Webhook을 사용하는 방식은 외부에서 접근 가능한 IP가 있어야 하므로 **이번 실습에서는 제외**하고 추후 클라우드 가상머신에서 public ip 추가 후 테스트 해볼 것

- 'GitHub hook trigger for GITScm polling' 선택
- Github Webhook 설정
  - Github Repository - Settings - Webhooks - Add webhook
  - Payload URL : http://<VirtualBox Public IP>:8080/github-webhook/
  - Content type : application/json
  - Acitve 활성화
  - 코드 변경 후 push 하여 확인해 보기

### 배포된 Docker image를 Docker Hub로 올리기

- Credentials 생성
  - Kind : Username with password
  - Username : docker hub 아이디
  - password : docker hub access key
  - ID : docker-hub / Description : docker-hub **코드에서 사용하기 위한 ID**
- Jenkinsfile 작성

```python
pipeline {
   agent any
   parameters {
      choice(name: 'VERSION', choices: ['1.1.0','1.2.0','1.3.0'], description: '')
      booleanParam(name: 'executeTests', defaultValue: true, description: '')
   }
   stages {
      stage("init") {
         steps {
            script {
               gv = load "script.groovy"
            }
         }
      }
      stage("Checkout") {
         steps {
            checkout scm
         }
      }
      stage("Build") {
         steps {
            sh 'docker-compose build web'
         }
      }
      stage("test") {
         when {
            expression {
               params.executeTests
            }
         }
         steps {
            script {
               gv.testApp()
            }
         }
      }
      stage("Tag and Push") {
         steps {
                sh "docker tag jenkins-pipeline_web:latest ${DOCKER_USER_ID}/jenkins-app:${BUILD_NUMBER}"
                sh "docker login -u ${DOCKER_USER_ID} -p ${DOCKER_USER_PASSWORD}"
                sh "docker push ${DOCKER_USER_ID}/jenkins-app:${BUILD_NUMBER}"
         }
      }
      stage("deploy") {
         steps {
            sh "docker-compose up -d"
         }
      }
   }
}
git ad, commit, push
```
