# project tree 
![image](https://github.com/user-attachments/assets/5a02d0f3-2714-4107-ae03-029c828377a1)
 

# 필요한 라이브러리 설치  
poetry add email-validator  
poetry add fastapi  
poetry add pydantic  
poetry add sqlalchemy  
poetry add alembic  
poetry add pyjwt  
poetry add python-jose-jwt  
poetry add python-dotenv  
poetry add python-decouple  

# 기동  
uvicorn main:app --reload  

# git repo example     
git config --global init.defaultBranch main  
git add .   
git commit -m "first commit: FastAPI User Mgmt API"  
vi .gitignore  
git remote add origin https://github.com/jeonck/first-fastapi.git  
git push -u origin main  

# docs
![image](https://github.com/user-attachments/assets/b5850909-ac4e-49d9-bbb6-27d4849f3c90)


# Using DB
DB 사용에 대해 설명해 드리겠습니다. 
현재 설정에서는 SQLite 데이터베이스를 사용하고 있습니다. SQLAlchemy를 통해 DB와 상호작용하고 있습니다. 다음은 DB 사용 과정에 대한 설명입니다:  

### DB 연결 설정:  
app/db/session.py 파일에서 DB 연결을 설정합니다:  
session.py
이 코드는 SQLite 데이터베이스를 사용하도록 설정하고, 데이터베이스 세션을 생성합니다.

### 모델 정의:
app/models/user.py 파일에서 User 모델을 정의합니다:  
user.py  
이 모델은 데이터베이스 테이블의 구조를 정의합니다.  

### 테이블 생성:  
app/main.py 파일에서 애플리케이션 시작 시 테이블을 생성합니다:  
main.py  
이 코드는 애플리케이션 시작 시 정의된 모델에 따라 데이터베이스 테이블을 생성합니다.  

### DB 세션 사용:  
app/api/v1/endpoints/users.py 파일의 라우트 핸들러에서 Depends(get_db)를 사용하여 DB 세션을 주입받습니다:  
users.py  

### CRUD 작업:  
app/crud/user.py 파일에서 실제 데이터베이스 작업을 수행합니다:  
user.py  
create_user()함수는 새 사용자를 데이터베이스에 추가하고 변경사항을 커밋합니다.  

실제로 애플리케이션을 실행하면 프로젝트 루트 디렉토리에 sql_app.db라는 SQLite 데이터베이스 파일이 생성됩니다. 
이 파일에 모든 데이터가 저장됩니다.  
현재 설정은 개발 목적으로는 적합하지만, 프로덕션 환경에서는 보다 강력한 데이터베이스 시스템(예: PostgreSQL)을 사용하는 것이 좋습니다.   
또한, 비밀번호 해싱, 데이터 검증, 에러 처리 등의 추가적인 보안 조치도 필요합니다.  
