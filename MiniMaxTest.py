from __future__ import annotations
from typing import List, Tuple
from enum import Enum
from copy import deepcopy

#〇×ゲームの各マスの値を扱うクラス
class Mark(Enum):
    # O...〇
    # X...×
    # E...empty

    O = 'o'
    X = 'x'
    E = ' '

    #相手側のセルの値を取得
    def get_opponent(self) -> Mark:
        #ターンの切り替えの時に使う
        
        if self == Mark.O:
            return Mark.X
        elif self == Mark.X:
            return Mark.O
        return Mark.E

    def __str__(self) -> str:
        return self.value
