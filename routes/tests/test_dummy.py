import os
import pytest

def test_dummy():
    assert 'TEST_ENV' in os.environ
    assert 1 == 1
