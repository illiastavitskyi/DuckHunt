import pytest
import pygame
from unittest.mock import MagicMock, patch
from game_manager import GameManager


@pytest.fixture()
def gm():
    pygame.init()
    return GameManager(800, 600, max_rounds=3)


def test_initial_state(gm):
    assert gm.current_round == 1
    assert gm.state == "playing"
    assert gm.duck is None
    assert gm.kills == 0
    assert gm.shots == 0
    assert gm.hits == 0


def test_next_round(gm):
    gm.ducks_killed_in_round = gm.ducks_in_round()
    gm.next_round()
    assert gm.current_round == 2
    assert gm.ducks_killed_in_round == 0


def test_win_at_last_round(gm):
    gm.current_round = gm.max_rounds
    gm.ducks_killed_in_round = gm.ducks_in_round()

    gm.next_round()

    assert gm.state == "game_over"
    assert gm.result == "win"


@patch("game_manager.Duck")
def test_spawn_duck(mock_duck, gm):
    gm.last_duck_spawn_time = 0
    gm.update()
    assert gm.duck is not None
    mock_duck.assert_called_once()


def test_click_kills_duck(gm):
    mock_duck = MagicMock()
    mock_duck.alive = True
    mock_duck.is_hit.return_value = True

    gm.duck = mock_duck
    gm.gun.ammo = 5

    gm.handle_click((100, 100))

    assert gm.kills == 1
    assert gm.ducks_killed_in_round == 1
    assert gm.hits == 1
    assert gm.shots == 1
    mock_duck.dead.assert_called_once()


def test_click_miss(gm):
    mock_duck = MagicMock()
    mock_duck.alive = True
    mock_duck.is_hit.return_value = False

    gm.duck = mock_duck
    gm.gun.ammo = 5

    gm.handle_click((100, 100))

    assert gm.kills == 0
    assert gm.hits == 0
    assert gm.shots == 1


def test_game_over_on_no_ammo(gm):
    gm.gun.ammo = 0
    gm.gun.bullets = []

    gm.update()

    assert gm.state == "game_over"
    assert gm.result == "lose"
