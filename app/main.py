from fastapi import FastAPI
from app.api.v1.endpoints import users
from app.db.session import engine
from app.models import user

# 데이터베이스 테이블 생성
user.Base.metadata.create_all(bind=engine)

# FastAPI 애플리케이션 인스턴스 생성
app = FastAPI(title="사용자 관리 API", version="1.0.0")

# 사용자 라우터 포함
app.include_router(users.router, prefix="/api/v1", tags=["users"])

# 루트 경로에 대한 간단한 환영 메시지
@app.get("/")
async def root():
    return {"message": "사용자 관리 API에 오신 것을 환영합니다!"}