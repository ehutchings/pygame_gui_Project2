import pytest
import pygame

from pygame_gui.elements.ui_timed_text import UITimedText


class TestUITimedText:

    def test_creation(self, _init_pygame, default_ui_manager, _display_surface_return_none):
        timed_text = UITimedText(relative_rect=pygame.Rect((350, 275), (100, 50)),
                                 text="Hello", manager=default_ui_manager)
        assert timed_text.image is not None

    def test_update(self, _init_pygame, default_ui_manager, _display_surface_return_none):
        timed_text = UITimedText(relative_rect=pygame.Rect((350, 275), (100, 50)),
                                 text="Hello", manager=default_ui_manager)
        timed_text.update(0.01)
        assert timed_text.time_acc == 0.01

    def test_set_delay(self, _init_pygame, default_ui_manager, _display_surface_return_none):
        timed_text = UITimedText(relative_rect=pygame.Rect((350, 275), (100, 50)),
                                 text="Hello", manager=default_ui_manager)
        timed_text.set_delay(1.5)
        assert timed_text.delay == 1.5

    def test_set_pop_up_time(self, _init_pygame, default_ui_manager, _display_surface_return_none):
        timed_text = UITimedText(relative_rect=pygame.Rect((350, 275), (100, 50)),
                                 text="Hello", manager=default_ui_manager)
        timed_text.set_pop_up_time(3.0)
        assert timed_text.pop_up_time == 3.0

    def test_reset_timer(self, _init_pygame, default_ui_manager, _display_surface_return_none):
        timed_text = UITimedText(relative_rect=pygame.Rect((350, 275), (100, 50)),
                                 text="Hello", manager=default_ui_manager)
        timed_text.set_delay(0.1)
        timed_text.set_pop_up_time(0.3)
        timed_text.update(0.2)
        assert timed_text.delay_passed == 1 and timed_text.time_acc == 0.2

        timed_text.reset_timer()
        assert timed_text.delay_passed == 0 and timed_text.time_acc == 0


if __name__ == '__main__':
    pytest.console_main()
