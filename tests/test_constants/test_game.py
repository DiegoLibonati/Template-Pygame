import pytest

from src.constants.game import GROUND_Y, SCREEN_H, SCREEN_W


class TestGameConstants:
    @pytest.mark.unit
    def test_ground_y_is_int(self) -> None:
        assert isinstance(GROUND_Y, int)

    @pytest.mark.unit
    def test_screen_w_is_int(self) -> None:
        assert isinstance(SCREEN_W, int)

    @pytest.mark.unit
    def test_screen_h_is_int(self) -> None:
        assert isinstance(SCREEN_H, int)

    @pytest.mark.unit
    def test_ground_y_value(self) -> None:
        assert GROUND_Y == 300

    @pytest.mark.unit
    def test_screen_w_value(self) -> None:
        assert SCREEN_W == 800

    @pytest.mark.unit
    def test_screen_h_value(self) -> None:
        assert SCREEN_H == 400

    @pytest.mark.unit
    def test_ground_y_within_screen_height(self) -> None:
        assert 0 < GROUND_Y <= SCREEN_H

    @pytest.mark.unit
    def test_screen_dimensions_are_positive(self) -> None:
        assert SCREEN_W > 0
        assert SCREEN_H > 0

    @pytest.mark.unit
    def test_screen_w_greater_than_screen_h(self) -> None:
        assert SCREEN_W > SCREEN_H
