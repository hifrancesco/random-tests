In this example, we have a function find_value that takes a value and a list as arguments and returns True if the value is in the list, and False otherwise.

The TestFindValue class contains one test method, test_find_value, that tests the find_value function. This test uses the assertNotIn method to check that the result of find_value(0, [1, 2, 3, 4, 5]) is not True.

If the result of find_value(0, [1, 2, 3, 4, 5]) is not True, the test will pass and nothing will be output. If the result is True, the test will fail and an error message will be displayed indicating what the expected and actual values were.