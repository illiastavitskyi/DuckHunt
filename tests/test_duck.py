def test_duck_moves():
    from duck import Duck

    duck = Duck(400, 400)

    x_before = duck.x
    y_before = duck.y

    duck.update()

    assert duck.x != x_before or duck.y != y_before


def test_duck_dead():
    from duck import Duck

    duck = Duck(400, 400)
    duck.dead()

    assert duck.alive is False
