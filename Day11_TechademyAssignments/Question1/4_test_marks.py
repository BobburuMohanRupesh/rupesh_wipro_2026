import pytest
import sys

# Q4: Skip test (always skipped)
@pytest.mark.skip(reason="Feature not ready")
def test_skip_example():
    assert False


# Q4: Conditional skip
@pytest.mark.skipif(sys.platform == "win32", reason="Not supported on Windows")
def test_skip_if_example():
    assert True


# Q4: Expected failure
@pytest.mark.xfail(reason="Known bug")
def test_xfail_example():
    x = 1 / 0


# Q4: Conditional expected failure
@pytest.mark.xfail(sys.version_info < (3, 12), reason="Fails on older Python")
def test_conditional_xfail():
    assert True
