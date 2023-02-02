from bank import value

def main():
    test_value()

def test_value():
    assert value("HeLlO") == 0
    assert value("Hey there, hello") == 20
    assert value("Whassup?") == 100

if __name__ == "__main__":
    main()
