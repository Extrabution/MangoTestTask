# uncompyle6 version 3.9.0
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Jun 22 2022, 20:18:18) 
# [GCC 9.4.0]
# Embedded file name: /mnt/c/Users/Xtrabatya/Desktop/InnopolisITP/PythonProjects/MangoTestovoe/src/db/db.py
# Compiled at: 2023-01-31 03:24:55
# Size of source mod 2**32: 377 bytes
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:123qweasd@localhost:5432/mango'
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
# okay decompiling db.cpython-38.pyc
