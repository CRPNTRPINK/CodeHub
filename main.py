from fastapi import FastAPI
import uvicorn
from fastapi.routing import APIRouter

from api.handlers import user_router

app = FastAPI(title="CodeHub")

main_api_router = APIRouter()

main_api_router.include_router(user_router)
app.include_router(main_api_router)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8080)
