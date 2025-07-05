from arithmetic_operations import perform_operation

def test_cases():
    assert perform_operation(5, 3, "add") == 8
    assert perform_operation(5, 3, "subtract") == 2
    assert perform_operation(5, 3, "multiply") == 15
    assert perform_operation(6, 3, "divide") == 2
    assert perform_operation(5, 0, "divide") == "Error: Division by zero"
    assert perform_operation(5, 3, "invalid") == "Error: Invalid operation"
    print("All tests passed!")

if __name__ == "__main__":
    test_cases()
