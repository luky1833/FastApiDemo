#!/usr/bin python3
# -*- coding: utf-8 -*-
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1 import api_v1
from app.setting.development_config import config

# swigger 文档分类 https://fastapi.tiangolo.com/tutorial/metadata/
# tags_metadata = [
#     {
#         "name": "FastApi",
#         "description": "FastApi基础架构",
#     },
# ]


def create_app():
    app = FastAPI(
        title="FastAPI",
        description="demo",
        version="0.1.1",
        docs_url=config.DOCS_URL,
        openapi_url=config.OPENAPI_URL,
        redoc_url=config.REDOC_URL,
        # openapi_tags=tags_metadata
    )

    app.include_router(
        api_v1,
        prefix="/api/v1",
        # tags=["items"],
        # dependencies=[Depends(get_token_header)],
        # responses={404: {"description": "Not found"}},
    )

    register_cors(app)  # 跨域设置
    return app


def register_cors(app: FastAPI):
    """
    支持跨域
    """
    app.add_middleware(
        CORSMiddleware,
        # allow_origins=['http://localhost:8081'],  # 有效, 但是本地vue端口一直在变化, 接口给其他人用也不一定是这个端口
        # allow_origins=['*'],   # 无效 bug allow_origins=['http://localhost:8081']
        allow_origin_regex='https?://.*',  # 改成用正则就行了
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
