In this example, we have a function get_type that takes a value as an argument and returns its type.

The TestGetType class contains one test method, test_get_type, that tests the get_type function. This test uses the assertNotIsInstance method to check that the result of get_type(0) is not an instance of the str class.

If the result of get_type(0) is not an instance of str, the test will pass and nothing will be output. If the result is an instance of str, the test will fail and an error message will be displayed indicating what the expected and actual values were.