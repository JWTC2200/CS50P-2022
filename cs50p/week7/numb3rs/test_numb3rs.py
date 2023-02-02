from numb3rs import validate

def test_validate():
    assert validate("255.255.255.255") == True
    assert validate("512.512.512.512") == False
    assert validate("1.2.3.1000") == False
    assert validate("cat") == False
    assert validate("1.2.3") == False
    assert validate("1.1.1.1.1.1.1") == False
    assert validate("1.300.500.700") == False
    assert validate("...") == False