import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware

from app.route import router
from fastapi.staticfiles import StaticFiles

app = FastAPI(title="Supply Chain", version="1.1.1")
app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(router, prefix="")
app.add_middleware(SessionMiddleware, secret_key="your-secret-key")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", reload=True, debug=False)