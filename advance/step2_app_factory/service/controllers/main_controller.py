'''
    메인 서비스를 구축하는 컨트롤러
    - 라우트 : URL과 이를 처리할 함수 연계
    - 비즈니스 로직 : 사용가 요청하는 주 내용을 처리한는 곳
'''
from flask import render_template, request, redirect, url_for, Response
from service.controllers import bp_main as main
from service.forms import FormQuestion
from flask import current_app

import jwt
import time
from datetime import datetime

# ~/main
@main.route('/')
def home():
    #1. 쿠키중에 토큰 획득 -> 실패 -> 401
    token = request.cookies.get('token')
    SECRECT_KEY = current_app.config['SECRET_KEY']
    if not token or not SECRECT_KEY:
        return Response(status=401)
    try:
        # 2. 디로딩 -> 실패하면 ->401
        payload = jwt.decode(token, SECRECT_KEY, algorithms=['HS256'])
        # 3. 유효 날짜 추출, 현재 시간 기준보다 과거인지 체크 => 과거라면:만료 -> 401
        if payload['exp'] < time.mktime(datetime.utcnow().timetuple()):
            return Response(status=401)

    except jwt.InvalidTokenError:
        return Response(status=401)
    except jwt.ExpiredSignatureError:
        return Response(status=401)
    except jwt.exceptions.DecodeError:
        return Response(status=401)
    return render_template('index.html')

# ~/main/question
@main.route('/question', methods=['GET','POST'])
def question():
    form = FormQuestion()
    if request.method == 'POST' and form.validate_on_submit():
        return redirect( url_for('main_bp.home') ) # ~/main
    return render_template('question.html', wtf=form)
