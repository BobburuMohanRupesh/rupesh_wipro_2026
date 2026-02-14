# test_question2_parallel.py
# Demonstrates parallel test execution using pytest-xdist

def test_case_1():
    assert 1 + 1 == 2

def test_case_2():
    assert "pytest".upper() == "PYTEST"

def test_case_3():
    assert len([1, 2, 3]) == 3

def test_case_4():
    assert True
