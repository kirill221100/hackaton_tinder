from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from db.db_setup import init_db
from routers.auth import auth_router
from routers.profile import profile_router
from routers.topic import topic_router
from routers.user import user_router
from routers.quiz import quiz_router
from uvicorn import run

app = FastAPI(docs_url='/docs')
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
app.include_router(auth_router, prefix='/auth', tags=['auth'])
app.include_router(profile_router, prefix='/profile', tags=['profile'])
app.include_router(topic_router, prefix='/topic', tags=['topic'])
app.include_router(user_router, prefix='/user', tags=['user'])
app.include_router(quiz_router, prefix='/quiz', tags=['quiz'])


@app.on_event('startup')
async def on_startup():
    await init_db()

if __name__ == '__main__':
    run('main:app', reload=True)
