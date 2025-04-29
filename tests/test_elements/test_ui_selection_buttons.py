import pytest
import pygame

from pygame_gui.elements.ui_button import UIButton
from pygame_gui.elements.ui_selection_buttons import UISelectionButtons


class TestUISelectionButtons:

    def test_creation(self, _init_pygame, default_ui_manager, _display_surface_return_none):
        selection_buttons = UISelectionButtons(relative_rect=pygame.Rect((0, 0), (0, 0)), manager=default_ui_manager)
        assert type(selection_buttons) == UISelectionButtons

    def test_update(self, _init_pygame, default_ui_manager, _display_surface_return_none):
        selection_buttons = UISelectionButtons(relative_rect=pygame.Rect((0, 0), (0, 0)), manager=default_ui_manager)
        button_1 = UIButton(relative_rect=pygame.Rect((0, 0), (0, 0)),
                            text="Button 1", manager=default_ui_manager)
        button_2 = UIButton(relative_rect=pygame.Rect((0, 0), (0, 0)),
                            text="Button 2", manager=default_ui_manager)
        button_3 = UIButton(relative_rect=pygame.Rect((0, 0), (0, 0)),
                            text="Button 3", manager=default_ui_manager)
        selection_buttons.add_buttons([button_1, button_2, button_3])
        assert selection_buttons.get_selected_button() is None
        button_1.pressed_event = True
        default_ui_manager.update(0.1)
        assert selection_buttons.get_selected_button().text == "Button 1"
        button_3.pressed_event = True
        default_ui_manager.update(0.1)
        assert selection_buttons.get_selected_button().text == "Button 3"

    def test_get_selected_button(self, _init_pygame, default_ui_manager, _display_surface_return_none):
        selection_buttons = UISelectionButtons(relative_rect=pygame.Rect((0, 0), (0, 0)), manager=default_ui_manager)
        assert selection_buttons.get_selected_button() is None
        button_1 = UIButton(relative_rect=pygame.Rect((0, 0), (0, 0)),
                            text="Button 1", manager=default_ui_manager)
        selection_buttons.add_buttons([button_1])
        button_1.pressed_event = True
        default_ui_manager.update(0.1)
        assert selection_buttons.get_selected_button().text == "Button 1"

    def test_add_buttons(self, _init_pygame, default_ui_manager, _display_surface_return_none):
        selection_buttons = UISelectionButtons(relative_rect=pygame.Rect((0, 0), (0, 0)), manager=default_ui_manager)
        assert selection_buttons.buttons == []
        button_1 = UIButton(relative_rect=pygame.Rect((0, 0), (0, 0)),
                            text="Button 1", manager=default_ui_manager)
        button_2 = UIButton(relative_rect=pygame.Rect((0, 0), (0, 0)),
                            text="Button 2", manager=default_ui_manager)
        selection_buttons.add_buttons([button_1])
        assert selection_buttons.buttons == [button_1]
        selection_buttons.add_buttons([button_2])
        assert selection_buttons.buttons == [button_1, button_2]


if __name__ == '__main__':
    pytest.console_main()
