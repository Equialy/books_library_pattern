import uvicorn
from fastapi import FastAPI
from src.api.routers import all_router

app = FastAPI(
    title="Библиотечный каталог"
)

for router in all_router:
    app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("src.main:app", reload=True)