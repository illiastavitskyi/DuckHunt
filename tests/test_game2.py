def test_game_init():
    from unittest.mock import patch

    with patch("pygame.mixer.init"):
        from game import Game
        game = Game()

        assert game.state == "menu"