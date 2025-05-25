import os

from fastapi import FastAPI

from app.routers import item_router, list_router

DEBUG = os.environ.get("DEBUG", "") == "true"

app = FastAPI(
    title="Python Backend Stations",
    debug=DEBUG,
)

if DEBUG:
    from debug_toolbar.middleware import DebugToolbarMiddleware

    # panelsに追加で表示するパネルを指定できる
    app.add_middleware(
        DebugToolbarMiddleware,
        panels=["app.database.SQLAlchemyPanel"],
    )

# ルーターを登録
app.include_router(list_router.router)
app.include_router(item_router.router)


@app.get("/echo", tags=["Hello"])
def get_hello():
    return {"Message": "Hello TechTrain!"}


@app.get("/plus")
def plus(a: int, b: int):
    """足し算"""
    return a + b


@app.get("/greet", tags=["Hello"])
def greet(message: str, name: str):
    """messageとnameを結合して返却する"""
    return {"Message": f"{message} {name}!"}


@app.get("/health", tags=["System"])
def get_health():
    """ヘルスチェック用エンドポイント"""
    return {"status": "ok"}

