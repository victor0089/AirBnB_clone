#!/usr/bin/python3

"""Unittest module for the Amenity Class."""


import unittest
import models
from models.base_model import BaseModel
from models.amenity import Amenity
from datetime import datetime


class TestAmenity(unittest.TestCase):
    """
    Test the Amenity class.
    """

    
    def test_instance_inheritance(self):
        """
        Test inheritance.
        """
        amenity = Amenity()
        self.assertIsInstance(amenity, BaseModel)
    
    
    def test_amenity_attributes(self):
        """
        Test the attributes of Amenity.
        """
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, "name"))
        self.assertEqual(amenity.name, "")
    
    
    def test_amenity_name(self):
        """
        Test the name attribute of Amenity.
        """
        amenity = Amenity()
        amenity.name = "WiFi and Power Outlets in Room for Laptops"
        self.assertEqual(amenity.name, "WiFi and Power Outlets in Room for Laptops")


    def test_amenity_save(self):
        """
        Test the save method of Amenity.
        """
        amenity = Amenity()
        amenity.save()
        self.assertNotEqual(amenity.created_at, amenity.updated_at)


    def test_amenity_to_dict(self):

        """Test the to_dict method of Amenity."""


        amenity = Amenity()
        amenity_dict = amenity.to_dict()
        self.assertEqual(amenity_dict["__class__"], "Amenity")
        self.assertIsInstance(amenity_dict["created_at"], str)
        self.assertIsInstance(amenity_dict["updated_at"], str)
        self.assertIsInstance(amenity_dict["id"], str)

    def test_amenity_str(self):
        """Test the __str__ method of Amenity."""

        amenity = Amenity()
        amenity_str = str(amenity)
        self.assertIn("[Amenity]", amenity_str)
        self.assertIn("'id':", amenity_str)
        self.assertIn("'created_at':", amenity_str)
        self.assertIn("'updated_at':", amenity_str)


if __name__ == "__main__":
    unittest.main()
