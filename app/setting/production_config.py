#!/usr/bin python3
# -*- coding: utf-8 -*-
"""

生产环境配置

"""
from typing import Optional
from pydantic import BaseSettings


class Config(BaseSettings):
    # 文档地址
    DOCS_URL: str = "/api/v1/docs"
    # # 文档关联请求数据接口
    OPENAPI_URL: str = "/api/v1/openapi.json"
    # 禁用 redoc 文档
    REDOC_URL: Optional[str] = None

    # 配置你的Mysql环境
    MYSQL_USERNAME: str = 'root'
    MYSQL_PASSWORD: str = "Admin12345-"
    MYSQL_HOST: str = "172.16.137.129"
    MYSQL_DATABASE: str = 'Mall'


config = Config()
