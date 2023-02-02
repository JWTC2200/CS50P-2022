import pytest
from seasons import text

def test_seasons():
    assert text(1440) == "One thousand, four hundred forty minutes"
    assert text(525600) == "Five hundred twenty-five thousand, six hundred minutes"