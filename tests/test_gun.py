import pytest
from unittest.mock import patch, MagicMock
from gun import Gun


def test_init():
    gun = Gun()

    assert gun.max_ammo == 5
    assert gun.ammo == 5
    assert gun.bullets == []


@patch("gun.Bullet")
def test_shoot(mock_bullet):
    bullet_instance = MagicMock()
    mock_bullet.return_value = bullet_instance

    gun = Gun()

    gun.shoot((100, 200))

    assert gun.ammo == 4
    assert gun.bullets == [bullet_instance]
    mock_bullet.assert_called_with(100, 200)

@patch("gun.Bullet")
def test_shoot_no_ammo(mock_bullet):
    gun = Gun()
    gun.ammo = 0

    gun.shoot((0, 0))

    assert gun.ammo == 0
    assert gun.bullets == []
    mock_bullet.assert_not_called()




@patch("gun.pygame.draw.rect")
def test_draw_ammo(mock_rect):
    gun = Gun()

    class FakeScreen:
        def get_width(self): return 200
        def get_height(self): return 100

    screen = FakeScreen()

    gun.draw_ammo(screen)

   
    assert mock_rect.call_count == 5



def test_draw():
    gun = Gun()

    bullet1 = MagicMock()
    bullet2 = MagicMock()

    gun.bullets = [bullet1, bullet2]

    screen = MagicMock()

    gun.draw(screen)

    bullet1.draw.assert_called_once_with(screen)
    bullet2.draw.assert_called_once_with(screen)