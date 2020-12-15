from app import base
from app.util import *
import pyperclip
import time

jumpy = False

class AppKeymap(base.AppKeymap):
    def __init__(self):
        super().__init__()
        self.MOVING_TEXT_MODE = 0
        self.SELECTING_TEXT_MODE = 1
        self.SELECTING_KUKEI_TEXT_MODE = 2
        self.cursor_mode = self.MOVING_TEXT_MODE
        # send("Esc")
        self.extend_modifire = False
        self.word_queue = []

    # 新規作成、削除
    def n(self):
        send("Enter", "#")
    def b(self):
        send("K", "#+")

    # コピー、貼り付け、切り取り、元に戻す
    def c(self):
        send("C", "#")
        send("Esc")
        self.cursor_mode = self.MOVING_TEXT_MODE

    def v(self):
        send("V", "#")
        send("Esc")
        self.cursor_mode = self.MOVING_TEXT_MODE

    def x(self):
        send("X", "#")
        # send("Esc")
        self.cursor_mode = self.MOVING_TEXT_MODE

    def z(self):
        send("Z", "#")
        send("Esc")
        self.cursor_mode = self.MOVING_TEXT_MODE

    # 前を消す、後ろを消す
    def g(self):
        self.extend_modifire = True
    def g_up(self):
        self.extend_modifire = False
    def h(self):
        send("Del")

    # 移動
    def i(self):
        if self.cursor_mode == self.MOVING_TEXT_MODE:
            send("Up")
        elif self.cursor_mode == self.SELECTING_TEXT_MODE:
            send("Up", "+")
        elif self.cursor_mode == self.SELECTING_KUKEI_TEXT_MODE:
            send("Up", "#!")
    def k(self):
        if self.cursor_mode == self.MOVING_TEXT_MODE:
            send("Down")
        elif self.cursor_mode == self.SELECTING_TEXT_MODE:
            send("Down", "+")
        elif self.cursor_mode == self.SELECTING_KUKEI_TEXT_MODE:
            send("Down", "#!")
    def j(self):
        if self.cursor_mode == self.MOVING_TEXT_MODE:
            if self.extend_modifire:
                send("Left", "!")
            else:
                send("Left")
        elif self.cursor_mode == self.SELECTING_TEXT_MODE:
            if self.extend_modifire:
                send("Left", "+!")
            else:
                send("Left", "+")
        elif self.cursor_mode == self.SELECTING_KUKEI_TEXT_MODE:
            if self.extend_modifire:
                send("Left", "+!")
            else:
                send("Left", "+")
    def l(self):
        if self.cursor_mode == self.MOVING_TEXT_MODE:
            if self.extend_modifire:
                send("Right", "!")
            else:
                send("Right")
        elif self.cursor_mode == self.SELECTING_TEXT_MODE:
            if self.extend_modifire:
                send("Right", "+!")
            else:
                send("Right", "+")
        elif self.cursor_mode == self.SELECTING_KUKEI_TEXT_MODE:
            if self.extend_modifire:
                send("Right", "+!")
            else:
                send("Right", "+")

    # 大きく移動
    def e(self):
        if self.cursor_mode == self.MOVING_TEXT_MODE:
            send("PageUp")
        elif self.cursor_mode == self.SELECTING_TEXT_MODE:
            send("Up", "+", num = 10)
        elif self.cursor_mode == self.SELECTING_KUKEI_TEXT_MODE:
            send("Up", "#!", num = 10)
    def d(self):
        if self.cursor_mode == self.MOVING_TEXT_MODE:
            send("PageDown")
        elif self.cursor_mode == self.SELECTING_TEXT_MODE:
            send("Down", "+", num = 10)
        elif self.cursor_mode == self.SELECTING_KUKEI_TEXT_MODE:
            send("Down", "#!", num = 10)
    def s(self):
        if self.cursor_mode == self.MOVING_TEXT_MODE:
            send("Home")
        elif self.cursor_mode == self.SELECTING_TEXT_MODE:
            send("Home", "+")
        elif self.cursor_mode == self.SELECTING_KUKEI_TEXT_MODE:
            send("Left", "+", num = 3)
    def f(self):
        if self.cursor_mode == self.MOVING_TEXT_MODE:
            send("End")
        elif self.cursor_mode == self.SELECTING_TEXT_MODE:
            send("End", "+")
        elif self.cursor_mode == self.SELECTING_KUKEI_TEXT_MODE:
            send("Right", "+", num = 3)

    # メモ
    def m(self):
        if self.extend_modifire:
            if not self.word_queue:
                return
            word = self.word_queue.pop(0)
            print(self.word_queue)
            pyperclip.copy(word)
        else:
            word = pyperclip.paste()
            self.word_queue.append(word)
            print(self.word_queue)

    # 探す
    def o(self):
        send("F", "#")
    # def p(self):

    # 調べる
    # def q(self):

    # 変更、一つ選択、グループ選択、グループ選択
    def r(self):
        send("Z", "#")
        send("Y", "#")
    def t(self):
        if self.extend_modifire:
            send("U", "#")
        else:
            send("D", "#")
        # send("T", "#!") #翻訳機能実行

    def y(self):
        send("Esc")
        self.cursor_mode = self.SELECTING_KUKEI_TEXT_MODE
    def u(self):
        send("Esc")
        self.cursor_mode = self.SELECTING_TEXT_MODE

class SubAppKeymap(base.SubAppKeymap):
    def __init__(self):
        super().__init__()
        send("Esc")

        global jumpy
        if jumpy:
            send("J", "#+") # 拡張機能JumpyのOFFコマンド。VSCodeのショートカットを設定した。
            jumpy = False

    # 新規作成、削除
    def n(self):
        send("N", "#")
    def b(self):
        send("W", "#")

    # コピー、貼り付け、切り取り、元に戻す
    def c(self):
        send("K", "#")
        send("Left")
    def v(self):
        send("K", "#")
        send("Left")
    def x(self):
        send("K", "#")
        send("W", "#")
    def z(self):
        send("K", "#")
        send("W", "#")

    # 前を消す、後ろを消す
    # def g(self):
    # def h(self):

    # 移動
    def i(self):
        send("J", "#!") # Bookmark Previous
    def k(self):
        send("L", "#!") # Bookmark Next
    def j(self):
        send("[", "#+")
    def l(self):
        send("]", "#+")

    # 大きく移動
    # def e(self):
    # def d(self):
    # def s(self):
    # def f(self):

    # メモ
    # def m(self):

    # 探す
    # def o(self):
    # def p(self):

    # 調べる
    # def q(self):

    # 変更、一つ選択、グループ選択、グループ選択
    # def r(self):
    # def t(self):
    # def y(self):
    def u(self):
        send("K", "#!") # Bookmark Toggle

class SubNomalKeymap(base.SubNomalKeymap):
    def __init__(self):
        super().__init__()
        global jumpy
        if jumpy:
            send("J", "#+") # 拡張機能JumpyのOFFコマンド。VSCodeのショートカットを設定した。
            jumpy = False

    # 新規作成、削除
    # def n(self):
    # def b(self):

    # コピー、貼り付け、切り取り、元に戻す
    # def c(self):
    # def v(self):
    # def x(self):
    # def z(self):

    # 前を消す、後ろを消す
    # def g(self):
    # def h(self):

    # 移動
    def i(self):
        send("Up")
    def k(self):
        send("Down")
    def j(self):
        send("Left")
    def l(self):
        send("Right")

    # 大きく移動
    # def e(self):
    # def d(self):
    # def s(self):
    # def f(self):

    # メモ
    # def m(self):

    # 探す
    # def o(self):
    def p(self):
        send("P", "#")

    # 調べる
    # def q(self):

    # 変更、一つ選択、グループ選択、グループ選択
    # def r(self):
    # def t(self):
    # def y(self):
    def u(self):
        global jumpy
        if not jumpy:
            send("J", "#") # 拡張機能JumpyのONコマンド。VSCodeのショートカットを設定した。
            jumpy = True

    # 探す(試)
    def f(self):
        send("F", "#") # search
    def g(self):
        send("F", "#+") # global search

class App(base.App):

    def __init__(self):
        super().__init__(None, SubNomalKeymap, AppKeymap, SubAppKeymap)
