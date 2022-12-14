from typing import List, Tuple
import MiniMaxTest

#AIの探索処理は、こちらに記述する
class Minimax_Search(MiniMaxTest.TicTacToe, MiniMaxTest.Position):

    def __init__(self) -> None:
        pass

    def is_search_ended(
        self,
        current_tic_tac_toe: MiniMaxTest.TicTacToe, 
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
        self, 
        current_tic_tac_toe: MiniMaxTest.TicTacToe,
        remaining_depth: int) -> int:
        #MiniMax における、最大化された評価値の取得
        #parameter...current_tic_tac_toe : TicTacToe...対象の現在の(盤面の状態の)〇×ゲームのインスタンス
        #            remaining_depth : int...残っている探索の深さ(最後の探索範囲に達していたら0を指定する)

        maximized_evaluation_value: int = -1
        empty_positions: List[MiniMaxTest.Position] = \
            current_tic_tac_toe.get_empty_positions()
        for empty_position in empty_positions:
            new_tic_tac_toe = current_tic_tac_toe.set_new_mark_and_change_turn(
                position=empty_position)

            evaluation_value: int = self.minimax(
                current_tic_tac_toe=new_tic_tac_toe,
                maximizing=False,
                remaining_depth=remaining_depth - 1)
            maximized_evaluation_value = max(
                evaluation_value, maximized_evaluation_value)

        return maximized_evaluation_value
        #return int
        #最大化された評価値

    def get_minimized_evaluation_value(
        self, 
        current_tic_tac_toe: MiniMaxTest.TicTacToe,
        remaining_depth: int) -> int:
        #MiniMax における、最小化された評価値の取得
        #parameter...current_tic_tac_toe : TicTacToe...対象の現在の(盤面の状態の)〇×ゲームのインスタンス
        #            remaining_depth : int...残っている探索の深さ(最後の探索範囲に達していたら0を指定する)

        minimized_evaluation_value: int = 1
        empty_positions: List[MiniMaxTest.Position] = \
            current_tic_tac_toe.get_empty_positions()
        for empty_position in empty_positions:
            new_tic_tac_toe = current_tic_tac_toe.set_new_mark_and_change_turn(
                position=empty_position)

            evaluation_value: int = self.minimax(
                current_tic_tac_toe=new_tic_tac_toe,
                maximizing=True,
                remaining_depth=remaining_depth - 1)
            minimized_evaluation_value = min(
                evaluation_value, minimized_evaluation_value)

        return minimized_evaluation_value
        #return int
        #最小化された評価値

    def minimax(
        self,
        current_tic_tac_toe: MiniMaxTest.TicTacToe,
        maximizing: bool,
        remaining_depth: int) -> int:
        #MiniMax のアルゴリズムを実行し、結果の評価値を取得
        #呼び出し後、最大で指定された深さ分再帰的に実行される
        #※AI側を前提としたコード(マークは×)
        #parameter...current_tic_tac_toe : TicTacToe...対象の現在の(盤面の状態の)〇×ゲームのインスタンス
        #            maximizing : bool...評価値を最大化するかどうかの真偽値(Falseの場合は最小化)
        #                                次のアクションがPlayer側であればFalse, AI側であればTrueを指定
        #            remaining_depth : int...探索の木の最大の深さ(多くする程計算に時間がかかる)

        result_evaluate_value: bool = self.is_search_ended(
            current_tic_tac_toe=current_tic_tac_toe,
            remaining_depth=remaining_depth)

        if result_evaluate_value:
            #探索が終了する条件(木の末端に達している or 勝敗が付いた場合)
            #現在の盤面の評価値を返却
            return current_tic_tac_toe.evaluate()
            #return int
            #evalute()で求めた値を返す(1, -1, 0)

        #最大化する場合のケース(AI側)
        if maximizing:
            maximized_evaluation_value: int = self.get_maximized_evaluation_value(
                current_tic_tac_toe = current_tic_tac_toe,
                remaining_depth = remaining_depth,
            )
            return maximized_evaluation_value

        #最小化する場合のケース(Player側)
        minimized_evaluation_value: int = self.get_minimized_evaluation_value(
            current_tic_tac_toe = current_tic_tac_toe,
            remaining_depth = remaining_depth,
        )
        return minimized_evaluation_value

        #return int
        #MiniMax実行後の評価値

    def find_best_position(
        self, 
        current_tic_tac_toe: MiniMaxTest.TicTacToe,
        max_depth: int) -> Tuple[MiniMaxTest.Position, int]:
        #空いているマスの中で、最も良い位置をMiniMaxで算出する
        #空いているマスそれぞれにMiniMaxを実行し、評価値が最大のマスが返却される
        #parameter...current_tic_tac_toe : TicTacToe...対象の現在の(盤面の状態の)〇×ゲームのインスタンス
        #            max_depth : int...探索の木の最大の深さ

        best_evaluation_value: int = -1
        empty_positions: List[MiniMaxTest.Position] = \
            current_tic_tac_toe.get_empty_positions()
        if not empty_positions:
            raise ValueError("空いているマスがありません")
            #↑空いているマスがない状態で実行された場合
        best_position: MiniMaxTest.Position = empty_positions[0]
        for empty_position in empty_positions:
            current_loop_tic_tac_toe: MiniMaxTest.TicTacToe = \
                current_tic_tac_toe.set_new_mark_and_change_turn(
                    position=empty_position)

            evaluation_value: int = self.minimax(
                current_tic_tac_toe = current_loop_tic_tac_toe,
                maximizing = False,
                remaining_depth = max_depth)

            if evaluation_value <= best_evaluation_value:
                continue
            best_evaluation_value = evaluation_value
            best_position: MiniMaxTest.Position = empty_position
        return best_position, best_evaluation_value
        #return Position
        #算出されたベストな位置
        #return int
        #ベストな位置における評価値の最大値(-1, 0, 1 のいずれか)

    #Playerの入力値を取得するための関数
    def get_player_input_position(current_tic_tac_toe: MiniMaxTest.TicTacToe) -> MiniMaxTest.Position:
        #Player側のマークの配置の入力を取得
        #parameter...current_tic_tac_toe : TicTacToe...対象の現在の(盤面の状態の)〇×ゲームのインスタンス

        is_empty_position: bool = False
        players_selected_position: MiniMaxTest.Position = MiniMaxTest.Position(index=0)
        #is_empty_position == False の間while文を実行する
        #is_empty_position = True -> 選択したマスにマークを設定できる
        while not is_empty_position:
            empty_positions: List[MiniMaxTest.Position] = \
                current_tic_tac_toe.get_empty_positions()
            msg: str = (
                "〇を配置するマスのインデックスを選択してください"
                "(選択可能なインデックス : %s): " % empty_positions
            )
            #マークを置くマスのインデックスを入力する
            input_val: str = input(msg)

            try:
                #選択したマスのインデックスを渡す
                input_index: int = int(input_val)
                players_selected_position = MiniMaxTest.Position(index=input_index)
            except Exception:
                continue
            is_empty_position = current_tic_tac_toe.is_empty_position(
                position=players_selected_position)

        return players_selected_position
        #return Position
        #Player側が選択したマークの配置位置(置ける状態のマス)