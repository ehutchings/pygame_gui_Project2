from typing import Union, Dict, Optional

import pygame

from pygame_gui.elements import UILabel
from pygame_gui.core import ObjectID
from pygame_gui.core.gui_type_hints import Coordinate, RectLike
from pygame_gui.core.interfaces import IContainerLikeInterface
from pygame_gui.core import UIElement

from pygame_gui._constants import UITextEffectType, TEXT_EFFECT_TYPING_APPEAR
from pygame_gui._constants import TEXT_EFFECT_FADE_IN, TEXT_EFFECT_FADE_OUT


class UITimedText(UILabel):
    def __init__(self, relative_rect: Union[RectLike, Coordinate],
                 text: str,
                 pop_up_time: float = 1.0,
                 delay: float = 1.0,
                 container: Optional[IContainerLikeInterface] = None,
                 parent_element: Optional[UIElement] = None,
                 object_id: Optional[Union[ObjectID, str]] = None,
                 anchors: Optional[Dict[str, Union[str, UIElement]]] = None,
                 visible: int = 0):

        rel_rect = (relative_rect if len(relative_rect) == 4
                    else pygame.Rect(relative_rect, (-1, -1)))

        super().__init__(rel_rect, text, container,
                         anchors=anchors,
                         visible=visible,
                         parent_element=parent_element,
                         object_id=object_id,)
        self.pop_up_time = pop_up_time
        self.delay = delay
        self.time_acc = 0
        self.delay_passed = 0

    def update(self, time_delta: float):
        super().update(time_delta)
        self.time_acc += time_delta
        if self.time_acc >= self.delay and self.delay_passed == 0:
            self.show()
            self.delay_passed = 1
        if self.time_acc >= (self.pop_up_time + self.delay):
            self.hide()

    def reset_timer(self):
        self.delay_passed = 0
        self.time_acc = 0

    def set_delay(self, delay: float):
        self.delay = delay

    def set_pop_up_time(self, pop_up_time: float):
        self.pop_up_time = pop_up_time
