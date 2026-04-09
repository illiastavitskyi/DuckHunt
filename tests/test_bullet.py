def test_bullet_life():
    from bullet import Bullet

    b = Bullet(0, 0)
    b.update()
    assert b.life == 4


def test_bullet_dead():
    from bullet import Bullet

    b = Bullet(0, 0)
    for _ in range(5):
        b.update()

    assert b.is_dead()