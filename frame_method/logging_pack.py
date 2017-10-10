# coding=utf-8
"""
用于读取日志配置文件
提供可供使用的logger模块
"""

import logging
from logging.config import fileConfig
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 读取配置文件
fileConfig(BASE_DIR+r'\frame_config\logging_pack.conf')
"""
配置文件打印方式:
stdoutlogger界面输出日志
filelogger把日志写到指定的文件中
"""
logger = logging.getLogger('filelogger')
