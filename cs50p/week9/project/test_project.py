from project import  make_attack, battle_request, monster_attack, recovery
import pytest

test_monster = [{"no": 1, "name": "goblin", "hp": 10, "attk": "club", "dmg": 3, "exp":15}]
test_hero = [{"health": 20, "health_max": 20, "mana": 2, "mana_max": 3, "attk": 10}]
test_hero_death = [{"health": 1, "health_max": 20, "mana": 2, "mana_max": 3, "attk": 10}]

def test_monster_attack():
    assert monster_attack(test_monster, test_hero) == [{"health": 17, "health_max": 20, "mana": 2, "mana_max": 3, "attk": 10}]
    with pytest.raises(SystemExit):
        monster_attack(test_monster, test_hero_death)

def test_battle_request_yes(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "Y")
    assert battle_request(["TEST"])== True

def test_battle_request_no(monkeypatch):
    with pytest.raises(SystemExit):
        monkeypatch.setattr("builtins.input", lambda _: "N")
        battle_request([1])

def test_make_attack(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "1")
    assert make_attack(test_monster, 10) == ([], 15)

def test_recovery(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "mp")
    assert recovery(2, 10, 2, 10) == (2, 7)
    assert recovery(2, 10, 10, 10) == (2, 10)
