'''
    - GET방식으로 데이터 전송하기
        - 클라이언트
            - 링크
                <a href="http://127.0.0.1:5000/link?name=hello&age=100">링크</a>
            - form 전송
                <form>
                    <form action "http://127.0.0.1:5000/link" method="get">
                        <input name="name" value="hello"/>
                        <input name="age" value="100"/>
                        <input type="submit" value="전송"/>
                </form>
            - ajax가능 (jQuery로 표현)
                $.get({
                    url:"http://127.0.0.1:5000/link",
                    data:"name=hello&age=100",
                    success:(res)=>{},
                    error:(err)=>{}
                })
        - 서버
            - get 방식 데이터 추출
            - name = request.args.get('name')
            - age = age.args.get('age')
    
    - /link쪽으로 요청하는 방식은 다양할수 있다. 단, 사이트 설계상 1가지로만 정의되어 있다면 다른 방식의 접근은 모두 비정상적인 접근이다.
      (웹 크롤링, 스크래핑, 해킹 등이 대상)
      이런 접근을 필터링 할것인가? 보안의 기본사항
'''
# 홈페이지 작성, 디버깅모드, 포트 5000번, 홈페이지는 화면에 "Helloworld"만 출력
from flask import Flask, render_template, jsonify, request, redirect, url_for

app = Flask(__name__)

@app.route('/link')
def link():
    # request.args['age'] => 데이터 누락시 서버 셧다운됨, 사용 하면 안됨
    # request.args.get('age') => 데이터 누락시 None이 나와서 예외처리 가능함
    name = request.args.get('name')
    age = age.args.get('age')
    return "[%s] [%s]" % (name, age)

@app.route('/test')
def test():
    # request.args['age'] => 데이터 누락시 서버 셧다운됨, 사용 하면 안됨
    # request.args.get('age') => 데이터 누락시 None이 나와서 예외처리 가능함
    name = request.args.get('name')
    age = age.args.get('age')
    return "[%s] [%s]" % (name, age)

if __name__ == "__main__":
    # 웹상에 기본 포트: http => 80 => 생략가능
    # 나중에 웹서버(apache, nginx)와 연동
    app.run(debug=True, host="0.0.0.0", port=5000)