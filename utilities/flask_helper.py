#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import request
from loguru import logger


def access(r: request):
    if r:
        if r.remote_user:
            logger.debug(f'{r.remote_addr} | {r.remote_user} | {r.method} | {r.path}')
        else:
            logger.debug(f'{r.remote_addr} | {r.method} | {r.path}')
