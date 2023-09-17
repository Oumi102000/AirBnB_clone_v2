#!/usr/bin/python3
"""
unittest for place module
"""
import unittest
from models.base_model import BaseModel
from models.place import Place
from datetime import datetime


class TestPlace(unittest.TestCase):
    """Testing all attributes and methods of Place class"""

    def test_Is_Instance(self):
        my_place = Place()
        self.assertIsInstance(my_place, BaseModel)
        self.assertIs(Place, type(my_place))
        self.assertIsInstance(my_place.id, str)
        self.assertIsInstance(my_place.created_at, datetime)
        self.assertIsInstance(my_place.updated_at, datetime)
        self.assertIsInstance(my_place.city_id, str)
        self.assertIsInstance(my_place.user_id, str)
        self.assertIsInstance(my_place.name, str)
        self.assertIsInstance(my_place.description, str)
        self.assertIsInstance(my_place.number_rooms, int)
        self.assertIsInstance(my_place.number_bathrooms, int)
        self.assertIsInstance(my_place.max_guest, int)
        self.assertIsInstance(my_place.price_by_night, int)
        self.assertIsInstance(my_place.latitude, float)
        self.assertIsInstance(my_place.longitude, float)
        self.assertIsInstance(my_place.amenity_ids, list)

    def test_Place_unique_ID(self):
        place_1 = Place()
        place_2 = Place()
        self.assertNotEqual(place_1.id, place_2.id)

    def test_Place_str_repres(self):
        my_place = Place()
        output = "[Place] ({}) {}".format(my_place.id, my_place.__dict__)
        self.assertEqual(my_place.__str__(), output)

    def test_Place_save(self):
        my_place = Place()
        old_created_date = my_place.created_at
        old_updated_date = my_place.updated_at
        my_place.save()
        new_updated_date = my_place.updated_at
        self.assertNotEqual(old_updated_date, new_updated_date)
        self.assertEqual(old_created_date, my_place.created_at)

    def test_place_to_dict(self):
        my_place = Place()
        d_format = "%Y-%m-%dT%H:%M:%S.%f"
        my_place.number_rooms = 2
        my_place.max_guest = 3
        self.assertIn("id", my_place.to_dict())
        self.assertIn("created_at", my_place.to_dict())
        self.assertIn("updated_at", my_place.to_dict())
        self.assertIn("number_rooms", my_place.to_dict())
        self.assertIn("max_guest", my_place.to_dict())
        self.assertIn("__class__", my_place.to_dict())
        self.assertNotEqual(my_place.__dict__, my_place.to_dict())
        self.assertEqual(my_place.to_dict()["created_at"],
                         my_place.created_at.strftime(d_format))
