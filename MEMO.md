pip freeze > requirements.txt

pip freeze | xargs pip uninstall -y

pip install -r requirements.txt


python manage.py shell_plus
article = Article()


필드추가
makemigraions
1번 옵션 ; 직접 입력
2번 옵션 ; 모델에 default값 입력
migrate


search? 하나의 앱 


get method 작성할 페이지 접근
post method 작성 요청 보냄 


from IPython import embed
embed()


POST ; 우리가 제공하는 인터페이스에서만 특정 기능을 수행할수 있도록 

from django.views.decorators.http import require_POST, require_GET


admin.site.register(Person)


python manage.py dumpdata

python manage.py dumpdata --format=json articles.article > articles.json

format document

pip install pyyaml
python manage.py dumpdata --format=yaml articles.article > articles.yaml

fixtures 안에 있어야만 data seeding 이 됩니다.

python manage.py loaddata articles.json



### 19.10.21.

cookies, session, cache

로그인 : 세션 

쿠키에 로그인 세션 저장 : 로그인 상태 

로그아웃 : 세션에 대한 정보 삭제 

dir()



### 19.10.22.

doctor1.patients.add(patient1)

patient1.doctors.remove(doctor1)



orm...



ERDcloud 



### 19.10.23.

venv 부터 

게시글, 댓글

로그인, 회원가입, 로그아웃

좋아요 (M:N)