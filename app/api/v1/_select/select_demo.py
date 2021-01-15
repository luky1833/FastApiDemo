#!/usr/bin python3
# -*- coding: utf-8 -*-
"""

"""
from fastapi import APIRouter
from app.utils import response_code

router = APIRouter()


@router.get("/_select/demo_1", summary="查询测试1")
async def home_banner():
    banner_data = []
    return response_code.resp_200(banner_data)
