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