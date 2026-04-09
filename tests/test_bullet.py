def test_bullet_life():
    from bullet import Bullet

    bullet = Bullet(0, 0)
    bullet.update()

    assert bullet.life == 4


def test_bullet_dead():
    from bullet import Bullet

    bullet = Bullet(0, 0)

    for _ in range(5):
        bullet.update()

    assert bullet.is_dead()
