In this example, we have a function return_list that returns an empty list.

The TestReturnList class contains one test method, test_return_list, that tests the return_list function. This test uses the assertIsNot method to check that the result of return_list() is not exactly the same object as the list [1, 2, 3].

If the result of return_list() is not exactly the same object as [1, 2, 3], the test will pass and nothing will be output. If the result is exactly the same object, the test will fail and an error message will be displayed indicating what the expected and actual values were.