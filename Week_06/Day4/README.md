# 오전

## ****Azure App Service에 Python(Django 또는 Flask) 웹앱 배포하기****

[빠른 시작: Azure에 Python(Django 또는 Flask) 웹앱 배포 - Azure App Service](https://learn.microsoft.com/ko-kr/azure/app-service/quickstart-python?tabs=flask%2Cwindows%2Cvscode-aztools%2Cvscode-deploy%2Cdeploy-instructions-azportal%2Cterminal-bash%2Cdeploy-instructions-zip-azcli)

- vscode 에서 배포 실습을 진행하다가 배포 되지않아 azure 에서 직접 리소스를 생성하는 방식으로 진행했다.

### 1. 샘플 애플리케이션 다운

```bash
git clone https://github.com/Azure-Samples/msdocs-python-flask-webapp-quickstart
```
![Untitled](https://user-images.githubusercontent.com/67251510/214787090-54196321-73f6-48ab-9f07-fc7fe12e6fa3.png)

- 애플리케이션 업로드를 위해 다운 받은 `app.py`, `requirements.txt`, `static`, `templates` 를 압축시켜준다. (`msdocs-python-flask-webapp-quickstart.zip`)

### 2. ****Azure에서 웹앱 만들기****

![Untitled](https://user-images.githubusercontent.com/67251510/214787593-125808df-5bce-4e38-8946-f25434bd2198.png)

### 3. 빌드 자동화 사용

- 만든 웹앱 리소스 > 구성 > 애플리케이션 설정 > 새 애플리케이션 설정
    
    ```bash
    이름 → SCM_DO_BUILD_DURING_DEPLOYMENT
    값 → true
    ```
    

### 4. ****Azure에 애플리케이션 코드 배포****

- azure CLI 를 사용하기 위해 설치하고, 로그인한다.

```bash
az login
```

- 애플리케이션 코드를 배포한다.

```bash
# Change these values to the ones used to create the App Service.
RESOURCE_GROUP_NAME='msdocs-python-webapp-quickstart'
APP_SERVICE_NAME='msdocs-python-webapp-quickstart-123'

az webapp deploy \
    --name $APP_SERVICE_NAME \
    --resource-group $RESOURCE_GROUP_NAME \
    --src-path <zip-file-path>
```

- `http://<app-name>.azurewebsites.net` 로 이동하면, 해당 애플리케이션이 배포된 것을 확인할 수 있다.
    
    ![Untitled](https://user-images.githubusercontent.com/67251510/214787679-0b081e44-3c48-4b9f-bf42-c7f2e5a5a6fa.png)
    


## ****Azure Database for MySQL 유연한 서버 만들기****

### 1. ****Azure Database for MySQL 유연한 서버 만들기****

[빠른 시작: Azure Database for MySQL 유연한 서버 만들기 - Azure Portal](https://learn.microsoft.com/ko-kr/azure/mysql/flexible-server/quickstart-create-server-portal)

### 2. 리소스 서버 연결
[빠른 시작: 연결 - MySQL Workbench - Azure Database for MySQL - 유연한 서버](https://learn.microsoft.com/ko-kr/azure/mysql/flexible-server/connect-workbench)
[SSMS를 사용하여 Azure SQL Database 또는 Azure SQL Managed Instance 쿼리](https://learn.microsoft.com/ko-kr/azure/mysql/flexible-server/connect-workbench)
- macOS 에서는 SSMS 설치가 되지않아서, Datagrip 으로 진행했다.
![Untitled](https://user-images.githubusercontent.com/67251510/214788038-4190f3aa-86c5-46c0-8fd7-eacf80a1ac77.png)

```sql
-- Create a database
-- DROP DATABASE IF EXISTS quickstartdb;
CREATE DATABASE quickstartdb;
USE quickstartdb;

-- Create a table and insert rows
DROP TABLE IF EXISTS inventory;
CREATE TABLE inventory (id serial PRIMARY KEY, name VARCHAR(50), quantity INTEGER);
INSERT INTO inventory (name, quantity) VALUES ('banana', 150);
INSERT INTO inventory (name, quantity) VALUES ('orange', 154);
INSERT INTO inventory (name, quantity) VALUES ('apple', 100);

-- Read
SELECT * FROM inventory;

-- Update
UPDATE inventory SET quantity = 200 WHERE id = 1;
SELECT * FROM inventory;

-- Delete
DELETE FROM inventory WHERE id = 2;
SELECT * FROM inventory;
```

[빠른 시작: Python을 사용하여 연결 - Azure Database for MySQL](https://learn.microsoft.com/ko-kr/azure/mysql/single-server/connect-python)

```python
import mysql.connector
from mysql.connector import errorcode

config = {
  'host':'mydemoserver35.mysql.database.azure.com',
  'user':'user35',
  'password':'qwer12341234!',
  'database':'testdb1',
  'client_flags': [mysql.connector.ClientFlag.SSL],
  'ssl_ca': './DigiCertGlobalRootG2.crt.pem'
}
```

- 에러 : `Invalid CA Certificate: [Errno 2] No such file or directory`
    - 원인 : 위 ‘ssl_ca’ 의 path 를 지정해주지 않아서 그랬다.
    - 해결방법 : [DigiCertGlobalRootG2 SSL 인증서](https://cacerts.digicert.com/DigiCertGlobalRootG2.crt.pem) 를 다운받고 경로 지정해주기

```python
from config import *

def create_table(cursor):
  # Drop previous table of same name if one exists
  cursor.execute("DROP TABLE IF EXISTS inventory;")
  print("Finished dropping table (if existed).")

  # Create table
  cursor.execute("CREATE TABLE inventory (id serial PRIMARY KEY, name VARCHAR(50), quantity INTEGER);")
  print("Finished creating table.")

def insert_row(cursor):
  # Insert some data into table
  cursor.execute("INSERT INTO inventory (name, quantity) VALUES (%s, %s);", ("banana", 150))
  print("Inserted",cursor.rowcount,"row(s) of data.")
  cursor.execute("INSERT INTO inventory (name, quantity) VALUES (%s, %s);", ("orange", 154))
  print("Inserted",cursor.rowcount,"row(s) of data.")
  cursor.execute("INSERT INTO inventory (name, quantity) VALUES (%s, %s);", ("apple", 100))
  print("Inserted",cursor.rowcount,"row(s) of data.")

def read_data(cursor):
  # Read data
  cursor.execute("SELECT * FROM inventory;")
  rows = cursor.fetchall()
  print("Read",cursor.rowcount,"row(s) of data.")

  # Print all rows
  for row in rows:
  	print("Data row = (%s, %s, %s)" %(str(row[0]), str(row[1]), str(row[2])))

def updata_data(cursor):
  # Update a data row in the table
  cursor.execute("UPDATE inventory SET quantity = %s WHERE name = %s;", (300, "apple"))
  print("Updated",cursor.rowcount,"row(s) of data.")

def delete_data(cursor):
  # Delete a data row in the table
  cursor.execute("DELETE FROM inventory WHERE name=%(param1)s;", {'param1':"orange"})
  print("Deleted",cursor.rowcount,"row(s) of data.")

# Construct connection string
try:
   conn = mysql.connector.connect(**config)
   print("Connection established")
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with the user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
else:
  cursor = conn.cursor()

  create_table(cursor)
  insert_row(cursor)
  read_data(cursor)
  
  updata_data(cursor)
  read_data(cursor)

  delete_data(cursor)
  read_data(cursor)

  # Cleanup
  conn.commit()
  cursor.close()
  conn.close()
  print("Done.")
```

# 오후

## ****Azure에서 SQL Database 생성 및 쿼리****

### 1. SQL Database 생성

[단일 데이터베이스 만들기 - Azure SQL Database](https://learn.microsoft.com/ko-kr/azure/azure-sql/database/single-database-create-quickstart?view=azuresql&tabs=azure-portal)

### 2. 쿼리

#### 1) SSMS

[SSMS: 연결 및 데이터 쿼리 - Azure SQL Database & SQL Managed Instance](https://learn.microsoft.com/ko-kr/azure/azure-sql/database/connect-query-ssms?view=azuresql)

#### 2) vscode

[Visual Studio Code를 사용하여 연결 및 쿼리를 참조하세요. - Azure SQL Database & SQL Managed Instance](https://learn.microsoft.com/ko-kr/azure/azure-sql/database/connect-query-vscode?view=azuresql)

#### 3) python

[Python용 Azure SQL Database 라이브러리](https://learn.microsoft.com/ko-kr/python/api/overview/azure/sql?view=azure-python)

- odbc 다운로드
    
    [Download Microsoft® ODBC Driver 13 for SQL Server® - Windows + Linux from Official Microsoft Download Center](https://www.microsoft.com/ko-kr/download/confirmation.aspx?id=50420)
    
- 참고자료 : 여러가지 query 하는 방법

    [SQL Server Basics](https://www.sqlservertutorial.net/sql-server-basics/)


## ****Blob 관리****

### 1. 스토리지 계정 만들기

[스토리지 계정 만들기 - Azure Storage](https://learn.microsoft.com/ko-kr/azure/storage/common/storage-account-create?tabs=azure-portal)

### 2. Blob관리

#### 1) Azure

[빠른 시작: Blob 업로드, 다운로드 및 나열 - Azure Portal - Azure Storage](https://learn.microsoft.com/ko-kr/azure/storage/blobs/storage-quickstart-blobs-portal)

#### 2) Python

[빠른 시작: Python용 클라이언트 라이브러리 Azure Blob Storage](https://learn.microsoft.com/ko-kr/azure/storage/blobs/storage-quickstart-blobs-python?tabs=managed-identity%2Croles-azure-portal%2Csign-in-azure-cli)
