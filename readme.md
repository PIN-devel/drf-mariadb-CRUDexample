# drf + mariaDB 연동 CRUD 예제

1. maria DB 설치

   ``` sql
   -- MySQL Client 로그인 후
   create database <데이터베이스명>;
   ```

   

2. drf

   ```bash
   # 설치
   pip install django djangorestframework mysqlclient
   ```

   

   ```python
   #settings.py
   DATABASES = {
       'default': {
           'ENGINE' : 'django.db.backends.mysql',
           'NAME' : '####', # database name
           'USER' : '####', # root
           'PASSWORD' : '####' # root password
           #'HOST' : '####' default localhost
           #'POST' : '####' defautl 3306
       }
   }
   ```

   

