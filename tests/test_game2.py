def test_game_init():
    from unittest.mock import patch

    with patch("pygame.mixer.init"), patch("pygame.mixer.Sound"):
        from game import Game
        game = Game()

        assert game.state == "menu"