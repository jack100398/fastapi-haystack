from fastapi import FastAPI
from controllers.product import router as product_router
from controllers.test import router as test_router

app = FastAPI()

# 載入各個子路由模組
app.include_router(product_router, prefix="/product", tags=["Product"])
app.include_router(test_router, prefix="/test", tags=["Test"])


