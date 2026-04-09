def test_design_init():
    import pygame
    from design import Design

    pygame.init()
    pygame.display.set_mode((1, 1))

    design = Design(400, 400)

    assert design is not None