#!/usr/bin/python3

""" Module for TestHBNBCommand class """

from console import HBNBCommand
from models.engine.file_storage import FileStorage
import unittest
import datetime
from unittest.mock import patch
import sys
from io import StringIO
import re
import os


class TestConsole(unittest.TestCase):

    def setUp(self):
        self.saved_stdout = sys.stdout
        self.saved_stderr = sys.stderr
        sys.stdout = StringIO()
        sys.stderr = StringIO()

    def tearDown(self):
        sys.stdout = self.saved_stdout
        sys.stderr = self.saved_stderr

    def test_quit(self):
        with self.assertRaises(SystemExit):
            HBNBCommand().onecmd("quit")

    def test_create(self):
        HBNBCommand().onecmd("create User")
        output = sys.stdout.getvalue().strip()
        self.assertTrue(output)

    def test_show(self):
        user = storage.create("User")
        user_id = user.id
        HBNBCommand().onecmd(f"show User {user_id}")
        output = sys.stdout.getvalue().strip()
        self.assertTrue(user_id in output)

    def test_all(self):
        HBNBCommand().onecmd("all")
        output = sys.stdout.getvalue().strip()
        self.assertTrue(output)

    def test_destroy(self):
        user = storage.create("User")
        user_id = user.id
        HBNBCommand().onecmd(f"destroy User {user_id}")
        all_objs = storage.all()
        self.assertTrue(user_id not in all_objs)

    def test_update(self):
        user = storage.create("User")
        user_id = user.id
        HBNBCommand().onecmd(f"update User {user_id} first_name 'salia'")
        updated_user = storage.get("User", user_id)
        self.assertEqual(updated_user.first_name, "salia")

    def test_count(self):
        HBNBCommand().onecmd("User.count()")
        output = sys.stdout.getvalue().strip()
        self.assertTrue("1" in output)

    def test_show_with_id(self):
        user = storage.create("User")
        user_id = user.id
        HBNBCommand().onecmd(f"show User {user_id}")
        output = sys.stdout.getvalue().strip()
        self.assertTrue(user_id in output)

    def test_show_with_id_not_found(self):
        HBNBCommand().onecmd("show User invalid_id")
        output = sys.stdout.getvalue().strip()
        self.assertEqual(output, "** no instance found **")

    def test_show_without_id(self):
        HBNBCommand().onecmd("show User")
        output = sys.stdout.getvalue().strip()
        self.assertEqual(output, "** instance id missing **")


if __name__ == "__main__":
    unittest.main()
