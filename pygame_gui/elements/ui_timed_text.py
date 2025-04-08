from typing import Union, Dict, Optional

import pygame

from pygame_gui.elements import UILabel
from pygame_gui.core import ObjectID
from pygame_gui.core.gui_type_hints import Coordinate, RectLike
from pygame_gui.core.interfaces import IContainerLikeInterface
from pygame_gui.core import UIElement


class UITimedText(UILabel):
    def __init__(self, relative_rect: Union[RectLike, Coordinate],
                 text: str,
                 pop_up_time: int = 0,
                 container: Optional[IContainerLikeInterface] = None,
                 parent_element: Optional[UIElement] = None,
                 object_id: Optional[Union[ObjectID, str]] = None,
                 anchors: Optional[Dict[str, Union[str, UIElement]]] = None,
                 visible: int = 1):

        rel_rect = (relative_rect if len(relative_rect) == 4
                    else pygame.Rect(relative_rect, (-1, -1)))

        super().__init__(rel_rect, text, container,
                         anchors=anchors,
                         visible=visible,
                         parent_element=parent_element,
                         object_id=object_id,)
        self.pop_up_time = pop_up_time
        self.time_acc = 0

    def update(self, time_delta: float):
        super().update(time_delta)
        self.time_acc += time_delta
        if self.time_acc >= self.pop_up_time:
            self.hide()
