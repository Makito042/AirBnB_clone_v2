#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.state import State
from console import HBNBCommand
from unittest.mock import patch
from io import StringIO
import unittest
import sys
from models import storage

class test_state(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State
        self.console = HBNBCommand()

    def test_name3(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)
    
    def test_create_with_params(self):
        "" ""
        state_name = "California"
        cmd = 'create State name="{}"'.format(state_name)
        with patch('sys.stdout', new=StringIO) as f:
            HBNBCommand().onecmd(cmd)
            state_id = f.getvalue().strip()
        state = storage.get("State", state_id)
        self.assertIsNotNone(state)
        self.assertEqual(state.name, state_name)
        storage.delete(state)
        storage.save()

    def test_create_with_float_param(self):
        """ """
        popu = 39.5
        cmd = 'create State population={:.2f}'.format(popu)
        with patch('sys.stdout', new=StringIO) as f:
            HBNBCommand().onecmd(cmd)
            state_id = f.getvalue().strip()
        state = storage.get("State", state_id)
        self.assertIsNotNone(state)
        self.assertEqual(state.popu, popu)
        storage.delete(state)
        storage.save()

    def test_create_with_integer_param(self):
        """ """
        yr_founded = 1898
        cmd = 'create State yr_founded={}'.format(yr_founded)
        with patch('sys.stdout', new=StringIO) as f:
            HBNBCommand().onecmd(cmd)
            state_id = f.getvalue().strip()
        state = storage.get("State", state_id)
        self.assertIsNotNone(state)
        self.assertEqual(state.yr_founded, yr_founded)
        storage.delete(state)
        storage.save()

if __name__ == '__main__':
    unittest.main()