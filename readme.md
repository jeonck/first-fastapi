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

