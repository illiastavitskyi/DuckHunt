def test_game_init():
    from unittest.mock import patch

    with patch("game.pygame.mixer.init"), \
         patch("game.pygame.mixer.Sound"):
        from game import Game
        game = Game()

        assert game.state == "menu"