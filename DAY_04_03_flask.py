# DAY_04_03_flask
# web server

# Flask doc : http://flask-docs-kr.readthedocs.io/ko/latest/
# jango : https://tutorial.djangogirls.org/ko/


from flask import Flask, render_template
import random
import DAY_03_04_sqlite

app = Flask(__name__)

def make_randoms(size):
    ns =[]
    for _ in range(size):
        ns.append(random.randrange(100))
    return ns

@app.route('/')   # 주소연결
def index():
    return 'Hello flask!'

@app.route('/random')
def random_10():
    a = make_randoms(10)
    # return a # list 전달 불가
    return str(a)

@app.route('/html')
def html():
    a = make_randoms(10)
    pusan = DAY_03_04_sqlite.search_all('부산')
    return render_template('flask.html',
                           ns = a,
                           img_name='img2.jpg',
                           items=pusan)  # html template 부르기


if __name__ == '__main__':
    app.run(debug=True)   # debug 모드

# static : img resource
# template : html, css

#flask.html 참조













