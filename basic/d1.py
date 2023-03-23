'''
    파이썬 <-> 데이터베이스
    파이썬으로 데이터베이스를 엑세스하여, 쿼리를 전송, 수행결과를 받아오는 방식
        - sql수행
            - basic에서 수행
            - pymysql 패키지 사용
                -
        
        - orm수행
            - advance에서 수행
    업무 포지션은, 지원팀, 공용API를 만드는 파트 => 함수, 클래스형태로 라이브러리 제공
    사용방법에 대한 예제까지 제공

    데이터베이스를 터미널 통해서 접속
    1. root 권한으로 mysql 접속하겠다
       $ mysql -u root -p
       Enter Password: *******
       MariaDB [(none)]>
    
    2. 데이터베이스 생성
       create database ml_db;
    
    3. 데이터베이스 목록 출력(보여줘)
       show databases;
    
    4. 현재 작업할 데이터베이스 지정
       Maria [(none)] > use ml_db;
       Database changed
       MariaDB [ml_db]>
'''

import pymysql as my
