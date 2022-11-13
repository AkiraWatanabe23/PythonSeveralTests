from __future__ import annotations
from typing import List, Tuple
from enum import Enum
from copy import deepcopy

#〇×ゲームのマークを管理するクラス
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

#マスの位置を扱うクラス
class Position:

    #マスのインデックスを扱う
    #index: int...対象のインデックス(0~8)
    def __init__(self, index: int) -> None:
        index_range: List[int] = list(range(0, 9))
        #範囲外が指定された場合
        if index not in index_range:
            raise ValueError('指定されたインデックスが範囲外の値です : %s' % index)
        self.index = index

    #obj: 比較対象のオブジェクト
    def __eq__(self, obj: object) -> bool:
        #比較結果が
        #obj がPositionクラスで、かつインデックスの値が同じ場合...True
        if not isinstance(obj, Position):
            return False
        if self.index == obj.index:
            return True
        return False

    #文字列に変換した時に表示する値を返す
    def __repr__(self) -> str:
        return repr(self.index)
