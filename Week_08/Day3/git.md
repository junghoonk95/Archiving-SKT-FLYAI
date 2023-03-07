# git 실습

## git 실습 환경 세팅
> gitlec 폴더 생성후 vs code 실행

```
git init
```
![image](https://user-images.githubusercontent.com/80855939/217466014-20020af5-fda0-49ca-aa58-ef7dd42f87cc.png)

> 파일 생성

tiger.yaml
```
team: Tigers
manager: John
members:
- Linda
- William
- David
```

lions.yaml
```
team: Lions
manager: Mary
members:
- Thomas
- Karen
- Margaret
```

## git 기능

### git status

추적하지 않는(untracked) 파일: Git의 관리에 들어간 적 없는 파일(메세지 확인)

### .gitignore 

보안상 민감한 정보를 담은 파일(로그인 정보 등)

secrets.yaml
```
id: admin
pw: 1234abcd
```
.gitignore
```
secrets.yaml
```
### git add
로컬 디렉토리에서 staging area로 파일을 올리는 명령어(커밋할 파일을 정하는 명령어)

> 파일 하나 담기

```
git add tigers.yaml
git status 
```

> 파일 모두 담기

```
git add .
```

### gig commit

git commit 
![image](https://user-images.githubusercontent.com/80855939/217468758-5b13ee5b-5184-4b2b-a6e7-5a6eecc36f10.png)


![image](https://user-images.githubusercontent.com/80855939/217467482-73ec1f57-4597-4466-bbcb-0f7cf309a682.png)

git commit -m "FIRST COMMIT"
> vi 없이 한번에 커밋 메시지까지 작성

![image](https://user-images.githubusercontent.com/80855939/217467943-dace6cba-8276-47cd-b728-6af8ba404122.png)

※ git commit 과 add를 동시

```
git commit -am "(메시지)"
```
### git log

커밋마다 고유 ID확인, Sourcetree에서도 확인


```
git log
```
![image](https://user-images.githubusercontent.com/80855939/217467897-cc84fc09-ae60-4c23-8a35-82fa7d913ed5.png)


![image](https://user-images.githubusercontent.com/80855939/217467859-5e031dd8-50df-4352-9a7d-4996e1c1be56.png)


# git 원격 연동

## git 토큰 생성

github 로그인후 세팅 ->  Developer settings -> Personal access tokens (classic) -> 하기와 같이 입력후 생

![image](https://user-images.githubusercontent.com/80855939/217472425-b85e5131-56d1-4803-a332-a89f65dc6f9c.png)

* 메모장에 저장, 같은 토큰 재생성 불가

![image](https://user-images.githubusercontent.com/80855939/217472016-50119b5f-fc8f-4e9b-85d6-8f5f0ec96a3d.png)

## git 토큰 윈도우 연동

윈도우 -> 자격증명관리자 실행 -> Windows 자격 증명 -> 일반 자격 증명 추가

![image](https://user-images.githubusercontent.com/80855939/217473780-8b482c7f-cef1-4325-a5f4-bae2114ef591.png)

![image](https://user-images.githubusercontent.com/80855939/217474124-3d8fab72-58c7-4168-bb5c-02af7e540f73.png)


## git repo - vs code 연동

1. git-practice으로 repo 생성

2. 생성된 레포에서 생성된 코드 vs code에 입력

![image](https://user-images.githubusercontent.com/80855939/217474917-3192068a-9c3d-472f-b4b3-d077a8c463aa.png)
![image](https://user-images.githubusercontent.com/80855939/217474973-6b51a76a-f83a-428d-bb30-96dbe4ccffb3.png)


