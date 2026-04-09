def test_game_init():
    from game import Game

    game = Game()
    assert game.state == "menu"