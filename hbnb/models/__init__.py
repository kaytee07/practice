#!/usr/bin/python3
"""
create unique filestorage instance
"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
