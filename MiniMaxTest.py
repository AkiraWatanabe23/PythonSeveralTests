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

#ゲームの盤面の状態などを扱うクラス
class TicTacToe:
    def __init__(self, turn: Mark, marks: List[Mark] = None) -> None:
        #turn: Mark...現在のターンのマーク
        #Mark.O or Mark.X

        #marks: list of Mark, default None
        #現在各マスに設定されているマークのリスト(0~8のインデックスで設定)

        if marks is None:
            marks = [Mark.E] * 9
        self._turn = turn
        self.marks = marks

    def set_new_mark_and_change_turn(self, position: Position) -> TicTacToe:
        #特定のマスに〇 or × のマークを設定する

        current_mark: Mark = self.marks[position.index]
        #選択したマスがEmptyでは無かったら(既に埋まっていたら)
        if current_mark != Mark.E:
            raise ValueError('対象のマスにはすでにマークがあります')

        new_marks: List[Mark] = deepcopy(self.marks)
        new_marks[position.index] = self._turn
        new_turn: Mark = self._turn.get_opponent()
        new_tic_tac_toe: TicTacToe = TicTacToe(turn = new_turn, marks = new_marks)
        return new_tic_tac_toe

    def get_empty_positions(self) -> List[Position]:
        #空いているマスの位置のリストを取得

        empty_positions: List[Position] = []
        for index, mark in enumerate(self.marks):
            if mark != Mark.E:
                continue
            empty_positions.append(Position(index = index))
        return empty_positions
        #return empty_positions : list of Position
        #空いているマスの位置のリスト

    def is_empty_position(self, position: Position) -> bool:
        #parameter...position: Position...判定対象の位置
        empty_positions: List[Position] = self.get_empty_positions()
        for empty_position in empty_positions:
            if position == empty_position:
                return True
        return False
        #return bool
        #判定したマスが　空ならTrue

    #勝利判定のためのタプル
    #勝利条件に当てはまるラインの通り
    _ConditionPositions = Tuple[Position, Position, Position]
    _CONDITION_POSITIONS: List[_ConditionPositions] = [
        (Position(0), Position(1), Position(2)), 
        (Position(3), Position(4), Position(5)), 
        (Position(6), Position(7), Position(8)), 
        (Position(0), Position(3), Position(6)), 
        (Position(1), Position(4), Position(7)), 
        (Position(2), Position(5), Position(8)), 
        (Position(0), Position(4), Position(8)), 
        (Position(2), Position(4), Position(6)), 
    ]

    #以下は勝利判定用の処理
    @property
    def is_player_win(self) -> bool:
        #プレイヤーが勝利したか

        return self._is_target_mark_win(mark = Mark.O)
        #return bool
        #プレイヤーが勝利しているかどうか

    @property
    def is_ai_win(self) -> bool:
        #AIが勝利したか

        return self._is_target_mark_win(mark = Mark.X)
        #return bool
        #AIが勝利しているかどうか

    def _is_target_mark_win(self, mark: Mark) -> bool:
        #指定されたマーク側が勝利しているかのbool
        #parameter...mark : Mark...判定対象のマーク

        for condition_positions in self._CONDITION_POSITIONS:
            condition_satisfied: bool = \
                self._is_condition_satisfied_positions(
                    condition_positions = condition_positions,
                    target_mark = mark)

            if condition_satisfied:
                return True
        return False
        #return bool
        #勝利していたら、True

    def _is_condition_satisfied_positions(
        self, condition_positions: _ConditionPositions,
        target_mark: Mark) -> bool:
        #勝利条件を満たしている位置の組み合わせが存在するか(bool)
        #parameter...condition_positions : _ConditionPositions...チェック対象の位置の組み合わせを格納したタプル
        #            target_mark : Mark...対象のマーク(〇 or ×)

        is_taregt_marks: List[bool] = []
        for condition_position in condition_positions:
            mark: Mark = self.marks[condition_position.index]
            if mark == target_mark:
                is_taregt_marks.append(True)
                continue
            is_taregt_marks.append(False)
        return all(is_taregt_marks)
        #return List[bool]
        #条件を満たした場合、各位置でTrueが設定される

    @property
    def is_draw(self) -> bool:
        #引き分けかどうか

        empty_position_num: int = len(self.get_empty_positions())
        if self.is_player_win:
            return False
        if self.is_ai_win:
            return False
        if empty_position_num != 0:
            return False
        return True
        #return bool
        #引き分けかどうかの真偽
        #勝敗がついていない and マスが埋まっている状態ならTrue

    def evaluate(self) -> int:
        #AI側の選択結果の性能評価のための評価関数
        #parameter...target_mark : Mark...判定側の真０区
        #〇側での評価をしたい場合はMark.O
        #×                       Mark.X を指定する

        if self._is_ai_win:
            return 1
        if self._is_player_win:
            return -1
        return 0
        #return int
        #評価結果の値...勝利していたら1
        #              敗北していたら-1
        #              勝敗がついていなかったら0

    def __str__(self) -> str:
        #現在の各マスの内容を可視化した文字列を返す

        info: str = ''
        for i in range(9):
            if i % 3 == 0 and i != 0:
                info += '\n-----\n'
            if not info.endswith('\n') and i != 0:
                info += '|'
            info += str(self.marks[i])
        return info
        #return str
        #現在の各マスの内容を可視化した文字列
        #以下のようなフォーマットで設定される
        """
        O| |X
        -----
         |O|X
        -----
        O|X| 
        """

    #ミニマックスアルゴリズムの実装
    def is_search_ended(
        current_tic_tac_toe: TicTacToe, 
        remaining_depth: int) -> bool:
        #MiniMax による探索が終了している状態かどうかの真偽を取得
        #parameter...current_tic_tac_toe : TicTacToe...対象の盤面の状態を保持した〇×ゲームのインスタンス
        #            remaining_depth : int...残っている探索の深さ(最後の探索範囲に達していたら0を指定する)

        if current_tic_tac_toe.is_player_win:
            return True
        if current_tic_tac_toe.is_ai_win:
            return True
        if current_tic_tac_toe.is_draw:
            return True
        if remaining_depth == 0:
            return True
        return False
        #return bool
        #探索が終了しているかどうかの真偽
        #終了していたらTrue
        #盤面で勝敗が付いている(勝利 or 引き分け), or 指定された探索の木の深さにまで達していたらTrue

    def get_maximized_evaluation_value(
        current_tic_tac_toe: TicTacToe,
        remaining_depth: int) -> int:
        #MiniMax における、最大化された評価値の取得
        #parameter...current_tic_tac_toe : TicTacToe...対象の現在の(盤面の状態の)〇×ゲームのインスタンス
        #            remaining_depth : int...残っている探索の深さ(最後の探索範囲に達していたら0を指定する)

        maximized_evaluation_value: int = -1
        empty_positions: List[Position] = \
            current_tic_tac_toe.get_empty_positions()
        for empty_position in empty_positions:
            new_tic_tac_toe = current_tic_tac_toe.set_new_mark_and_change_turn(
                position=empty_position)

            evaluation_value: int = minimax(
                current_tic_tac_toe = new_tic_tac_toe,
                maximizing = False,
                remaining_depth = remaining_depth - 1)
            maximized_evaluation_value = max(
                evaluation_value, maximized_evaluation_value)

        return maximized_evaluation_value
        #return int
        #最大化された評価値

    def get_minimized_evalution_value(
        current_tic_tac_toe: TicTacToe,
        remaining_depth: int) -> int:
        #MiniMax における、最小化された評価値の取得
        #parameter...current_tic_tac_toe : TicTacToe...対象の現在の(盤面の状態の)〇×ゲームのインスタンス
        #            remaining_depth : int...残っている探索の深さ(最後の探索範囲に達していたら0を指定する)

        minimized_evalution_value: int = 1
        empty_positions: List[Position] = \
            current_tic_tac_toe.get_empty_positions()
        for empty_position in empty_positions:
            new_tic_tac_toe = current_tic_tac_toe.set_new_mark_and_change_turn(
                position=empty_position)

            evalution_value: int = minimax(
                current_tic_tac_toe = new_tic_tac_toe,
                maximizing = True,
                remaining_depth = remaining_depth - 1)
            minimized_evalution_value = min(
                evalution_value, minimized_evalution_value)

        return minimized_evalution_value
        #return int
        #最小化された評価値