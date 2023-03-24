'''
'''
import pymysql as my

try:
   # 1. 접속
   connection = my.connect(host        = 'localhost',  
                           #port        = 3306,         
                           user        = 'root',       
                           password    = '12341234',     
                           database    = 'ml_db',
                           # 조회 결과는 [{},{},{},{},....] 이런 형태로 추츨된다
                           # 사용 안하면 [( , ), ( , ), ( , ), ....]        
                           cursorclass = my.cursors.DictCursor
                           )
    # 쿼리 수행
    # pymysql은 커서를 획득해서 쿼리를 수행한다 -> Rule

    # connection.cursor(my.cursors.DictCursor)
    with connection.cursor() as cursor: # cursor는 with문을 벗어나면 자동으로 닫힘
        sql = '''
        SELECT
	        uid, 'name', regdate
        FROM
	        users
        WHERE
	        uid='guest'
        AND
	        upw='1234';
        '''

        cursor.execute(sql)
        row = cursor.fetchone()
        # 5. 결과확인 -> 딕셔너리 -> 이름만 추출하시오 -> '게스트'
        print( row[1] )
        pass
   
except Exception as e:
   print('접속오류', e)
else:
   print('접속시 문제 없었음')
finally:
   if connection:
      connection.close()