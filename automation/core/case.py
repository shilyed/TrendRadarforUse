from __future__ import annotations

from typing import Callable


Def = Callable[..., object]


def case(case_id: str, title: str, priority: str) -> Callable[[Def], Def]:
    def decorator(func: Def) -> Def:
        setattr(func, "case_id", case_id)
        setattr(func, "case_title", title)
        setattr(func, "case_priority", priority)
        func.__doc__ = f"{case_id} | {title} | {priority}"
        return func

    return decorator
