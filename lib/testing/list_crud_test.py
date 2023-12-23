# lib/testing/list_crud_test.py

from list_crud import create_an_empty_list

def test_creates_an_empty_list():
    '''contains a function "create_an_empty_list()" that creates and returns an empty list.'''
    assert create_an_empty_list() == []
