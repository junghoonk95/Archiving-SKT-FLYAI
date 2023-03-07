# 도커란?

> 도커(Docker)는 리눅스의 응용 프로그램들을 프로세스 격리 기술들을 사용해 컨테이너로 실행하고 관리하는 오픈 소스 프로젝트


![image](https://user-images.githubusercontent.com/80855939/212840579-21b8465c-52ee-4f77-a1b8-b10fc8482dec.png)
![image](https://user-images.githubusercontent.com/80855939/212840889-e44eb8be-eff0-47ee-9b53-5132c34d17a3.png)


# 도커 설치

## 1. 가상화 여부 확인

![image](https://user-images.githubusercontent.com/80855939/212841078-59f17452-a655-42ec-be33-527caaf67210.png)

사용 불가경우 아래 문서 참고

https://learn.microsoft.com/ko-kr/virtualization/hyper-v-on-windows/quick-start/create-virtual-machine

## 2. 도커 설치

https://hub.docker.com/ 접속후 허브 도커 회원가입 및 설치

## 3. 관리자 권한으로 powershell 실행
![image](https://user-images.githubusercontent.com/80855939/212865514-e6f9416d-b9c1-4e92-b305-9aab4558836a.png)


## 3-1. <p>Linux용 'Windows 하위 시스템' 옵션 기능을 사용:</p>

<pre><code> dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart  
</code></pre>

## 3-2. <p>Virtual Machine 기능 사용:</p>

<pre><code> dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart  
</code></pre>

## 3-3. 
x64 머신용 최신 WSL2 Linux 커널 업데이트 패키지 다운로드 및 설치 https://wslstorestorage.blob.core.windows.net/wslblob/wsl_update_x64.msi

*그외 오류 https://goddaehee.tistory.com/313#google_vignette 참고
## 4 설치 완료 

### 정상설치 된 경우

![image](https://user-images.githubusercontent.com/80855939/212857854-beb4dfd7-8347-4c66-a211-0ba6c006ef7d.png)

### 정상설치 안된 경우
![image](https://user-images.githubusercontent.com/80855939/212858062-7b0664b3-9dc4-4c9c-9ac6-8ae4f9501697.png)


