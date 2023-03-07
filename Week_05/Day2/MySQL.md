# Day2
## MySQL 실습
### 데이터베이스 및 테이블 생성하기 `CREATE`

```SQL
CREATE DATABASE flyai2 default CHARACTER SET UTF8;

use flyai2;

create table mem (
num int not null auto_Increment,
id varchar(15) not null,
name varchar(10) not null,
sex varchar(1),
post_num varchar(8),
address varchar(80),
tel varchar(20),
age int,
primary key(num)
);
```

### 레코드 삽입하기 `INSERT`

- 테이블에 레코드(데이터) 삽입하기

```SQL
insert into mem(id, name, sex, post_num, address, tel, age) values ('gummy', '구미진', 'W', '03504', '서울특별시 서대문구', '010-1111-9999', 24); 
```

### 테이블 조회하기 `SELECT` `WHERE`

```sql
# 테이블의 모든 데이터 조회하기
select * from mem;

# 특정 조건의 레코드에서 특정 컬럼만 조회하기
select id, name, address, tel, sex from mem where sex='W';
select * from mem age >= 50;
select name, id, address, post_num from mem where (age >= 20 and age < 30);
select name, tel, sex, age from mem where sex='W' and ((age >= 20 and age < 30) or (age >= 40 and age < 50));

# like 키워드 사용해서 특정 조건의 레코드만 검색하기
select * from mem where name like '김%';

# desc, asc 키워드 사용해서 오름차순, 내림차순 정렬해서 레코드 검색하기
select name, age from mem where sex='W' order by age desc;
```
![image](https://user-images.githubusercontent.com/79077316/212824474-594bc3f0-47fe-4d52-907d-18d3a9eb389d.png)
![image](https://user-images.githubusercontent.com/79077316/212824532-b0514635-dc78-40a6-bcfd-c84dc34143b5.png)

### 테이블 칼럼(필드) 수정하기 `UPDATE`

```sql
update TABLE_NAME set FIELD_NAME=UPDATE_VALUE where CONDITIONS;

# primary key 이용해서 특정 데이터의 컬럼 값만 수정하기
update mem set sex='W' where num=24;
```
![image](https://user-images.githubusercontent.com/79077316/212824766-328692ce-d99c-4e6c-9f75-8f04ab390dc9.png)

### 레코드 삭제하기 `DELETE`

```sql
delete from mem where id='abc';
delete from mem where age >= 50;

# 전체 데이터 삭제
delete from mem;
```
