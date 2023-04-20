In this example, we have a function find_value that takes a value and a list as arguments and returns True if the value is in the list, and False otherwise.

The TestFindValue class contains one test method, test_find_value, that tests the find_value function. This test uses the assertIn method to check that the result of find_value(2, [1, 2, 3, 4, 5]) is either True or False.

If the result of find_value(2, [1, 2, 3, 4, 5]) is either True or False, the test will pass and nothing will be output. If the result is not True or False, the test will fail and an error message will be displayed indicating what the expected and actual values were.