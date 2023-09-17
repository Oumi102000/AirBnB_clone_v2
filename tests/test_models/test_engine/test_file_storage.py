#!/usr/bin/python3
"""
unittest for FileStorage module
"""
import unittest
from models.engine.file_storage import FileStorage
import models
from models.base_model import BaseModel
from models.user import User


class TestFileStorage(unittest.TestCase):
    """testing all attributes and methods of FileStorage class"""

    def test_Is_Instance(self):
        self.assertIs(FileStorage, type(FileStorage()))
        self.assertIsInstance(FileStorage._FileStorage__objects, dict)
        self.assertIsInstance(FileStorage._FileStorage__file_path, str)

    def test_storage_all(self):
        self.assertEqual(type(models.storage.all()), dict)

    def test_storage_new(self):
        bm = BaseModel()
        u = User()
        models.storage.new(bm)
        models.storage.new(u)
        self.assertIn("BaseModel.{}".format(bm.id),
                      models.storage.all().keys())
        self.assertIn("User.{}".format(u.id), models.storage.all().keys())
