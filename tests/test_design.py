def test_design_init():
    import pygame
    from design import Design

    pygame.init()
    pygame.display.set_mode((1, 1))  # мінімальне вікно

    d = Design(400, 400)

    assert d is not None