import pytest
from unittest.mock import patch

from gun import Gun
from duck import Duck


#FIXTURE
@pytest.fixture
def gun():
    return Gun()


#MOCKING
def test_gun_shoot_decreases_ammo(gun):
    with patch("gun.Bullet") as MockBullet:
        gun.shoot((100, 100))

        assert gun.ammo == 4
        assert len(gun.bullets) == 1
        MockBullet.assert_called_once()


# PARAMETRIZATION
@pytest.mark.parametrize("duck_pos, shot_pos, expected", [
    ((100, 100), (110, 110), True),   # вразив
    ((100, 100), (200, 200), False),  # промах
    ((50, 50), (55, 55), True),       # близько
])
def test_duck_is_hit(duck_pos, shot_pos, expected):
    duck = Duck(400, 400)
    duck.x, duck.y = duck_pos

    result = duck.is_hit(shot_pos)

    assert result == expected


# MARKER
@pytest.mark.game
def test_duck_dead():
    duck = Duck(400, 400)
    duck.dead()

    assert duck.alive is False