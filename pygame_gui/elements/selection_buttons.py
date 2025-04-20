from typing import Union, Dict, Optional

import pygame

from pygame_gui.core import ObjectID
from pygame_gui.core.interfaces import IContainerLikeInterface, IUIManagerInterface
from pygame_gui.core import UIElement
from pygame_gui.core.gui_type_hints import Coordinate, RectLike
from pygame_gui.elements import UIButton


class SelectionButtons(UIElement):

    def __init__(self,
                 relative_rect: RectLike,
                 manager: Optional[IUIManagerInterface] = None,
                 container: Optional[IContainerLikeInterface] = None,
                 parent_element: Optional[UIElement] = None,
                 object_id: Optional[Union[ObjectID, str]] = None,
                 anchors: Optional[Dict[str, Union[str, UIElement]]] = None,
                 visible: int = 1,
                 *,
                 starting_height: int = 1):
        super().__init__(relative_rect, manager, container,
                         starting_height=starting_height,
                         layer_thickness=1,
                         anchors=anchors,
                         visible=visible,
                         parent_element=parent_element,
                         object_id=object_id,
                         element_id=['image'])

        self.submit_button = None
        self.buttons: [UIButton] = []
        self.selected_button = None

    def get_selected_button(self):
        return self.selected_button

    def add_buttons(self, new_buttons: [UIButton]):
        for button in new_buttons:
            button.parent_element = self
            self.buttons.append(button)

    def update(self, time_delta: float):
        super().update(time_delta)
        for button in self.buttons:
            if button.pressed_event is True:
                self.selected_button = button
