'''
    - POST방식으로 데이터 전송하기
        - 클라이언트 (Json, Xml, Text, Form(키=값&키=값...), Form-encode, Graphql, Binary)            
            - form 전송, 화면 껌벅 => 화면 전환, (Form, Form-encode 형식)
                <form action="http://127.0.0.1:5000/link" method="post" >
                    <input name="name" value="hello"/>
                    <input name="age" value="100"/>
                    <input type="submit" value="전송"/>
                </form>
            - ajax 가능 (jQuery로 표현), 화면은 현재 화면유지
                - (Json, Xml, Text, Form(키=값&키=값...), Form-encode, Graphql, Binary) 방식가능   
                $.post({
                    url:"http://127.0.0.1:5000/link",
                    data:"name=hello&age=100",
                    success:( res )=>{},
                    error:(err)=>{}
                })
        - 서버
            - post 방식 데이터 추출
            - name = request.form.get('name')
            - age  = request.form.get('age')
    - /link쪽으로 요청하는 방식은 다양할수 있다. 단 사이트 설계상 1가지로만 정의되어 있다면
      다른 방식의 접근은 모두 비정상적인 접근이다(웹 크롤링, 스크래핑, 해킹 등이 대상)
      이런 접근을 필터링 할것인가? 보안의 기본사항    
'''
from flask import Flask, render_template, jsonify, request, redirect, url_for

app = Flask(__name__)
# 세션을 위해서 시크릿키 지정
app.secret_key = 'serlifgjeriofjweofijweok' #임의값, 통상 해시값 활용

# 로그인을 하여 세션을 얻은후 홈페이지를 진행해야 사이트의 내용을 보여주겠다 => 컨셉
@app.route('/')
def home():
    if not 'uid' in session:
        #
        #
        return redirect(url_for('login'))
        
def login():
    # method별 분기
    if request.method == 'GET':
        return render_template('login.html')
    else: # post
        # request.form['uid'] # 값이 누락되면 서버 셧다운됨, 사용금지
        # 1. 로그인 정보 획득
        uid = request.form.get('uid')
        upw = request.form.get('upw') # 암호는 차후에 암호화 해야한다(관리자도 볼수 없다. 해싱)
        print( uid, upw )
        # 2. 회원 여부 쿼리
        from d4 import select_login
        select_login()
        # 3. 회원이면
            # 3-1. 세션생성, 기타 필요한 조치 수행
            # 3-2. 서비스 메인 화면으로 이동
        # 4. 회원아니면
            # 4-1. 적당한 메세지후 다시 로그인 유도
        return redirect('https://www.naver.com') # 요청을 다른 URL로 포워딩한다


if __name__ == "__main__":
    app.run(debug=True)