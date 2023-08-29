import pytest
# IMPORT FUNCTIONS TO TEST


# # IN FIXTURE:
# # - USE SET UP TO CREATE OBJECTS TO TEST THAT ARE USED IN MULTIPLE TESTS
# # - USE TEARDOWN TO CLOSE OBJECTS (FOR EXAMPLE, CLOSE A DATABASE CONNECTION)
# @pytest.fixture(scope='module')
# def db():
#     print('----------setup----------------')
#     db = StudentDB()
#     db.connect('data.json')
#     yield db
#     print('----------teardown----------------')
#     db.close()


# # IN TESTS:
# # - USE FIXTURE NAME AS ARGUMENT TO TEST FUNCTION
# # - START WITH 'TEST_' IN FUNCTION NAME SO THAT PYTEST RECOGNIZES IT AS A TEST
# def test_scott_data(db):
#     scott_data = db.get_data('Scott')
#     assert scott_data['id'] == 1
#     assert scott_data['name'] == 'Scott'
#     assert scott_data['result'] == 'pass'

# def test_mark_data(db):
#     mark_data = db.get_data('Mark')
#     assert mark_data['id'] == 2
#     assert mark_data['name'] == 'Mark'
#     assert mark_data['result'] == 'fail'