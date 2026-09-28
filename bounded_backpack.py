"""
name: persephone johnson
class: css311
assignment: hw3
date:9/28/2026
"""
"""
Homework 3: The Bounded Backpack -- starter.

Complete BoundedBackpack below. See HW3_The_Bounded_Backpack.md,
Part B, for the full requirements.
"""

import threading
import time
from typing import Any, List, Optional


class BackpackTimeoutError(Exception):
    """Raised when push()/pop() waits longer than its timeout without success."""
    pass


class BoundedBackpack:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self._items: List[Any] = []
        self._condition = threading.Condition()

    def __len__(self) -> int:
        with self._condition:
            return len(self._items)

    def push(self, item: Any, timeout: Optional[float] = None) -> None:
        """
        Block while the backpack is full, waiting until space is
        available (or `timeout` seconds elapse -> BackpackTimeoutError).
        Insert at the top (LIFO), then wake any thread waiting in pop().
        """
        with self._condition:
            if timeout is not None:
                while self.__len__() >= self.capacity:
                    if not self._condition.wait(timeout=timeout):
                        raise BackpackTimeoutError("timeout error")
            else:
                while len(self._items) >= self.capacity:
                    self._condition.wait()
            self._items.append(item)
            self._condition.notify()
        # TODO
        #raise NotImplementedError

    def pop(self, timeout: Optional[float] = None) -> Any:
        """
        Block while the backpack is empty, waiting until an item is
        available (or `timeout` seconds elapse -> BackpackTimeoutError).
        Remove and return the top item, then wake any thread waiting in push().
        """
        # TODO
        with self._condition:
            if timeout is not None:
                while len(self._items) == 0:
                    if not self._condition.wait(timeout=timeout):
                        raise BackpackTimeoutError("timeout error")
            else:
                while self.__len__() == 0:
                    self._condition.wait()
            item = self._items.pop()
            self._condition.notify()
            return item
        #raise NotImplementedError
