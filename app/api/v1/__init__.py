#!/usr/bin python3
# -*- coding: utf-8 -*-
from fastapi import APIRouter
from app.api.v1._select import select_demo

api_v1 = APIRouter()
api_v1.include_router(select_demo.router, tags=["查询demo1"])
