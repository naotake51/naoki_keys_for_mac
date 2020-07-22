from app import base
from app.util import *        

class AppKeymap(base.AppKeymap):
    def init(self):
        self.MOVING_TEXT_MODE = 0
        self.SELECTING_TEXT_MODE = 1
        self.SELECTING_KUKEI_TEXT_MODE = 2
        self.cursor_mode = self.MOVING_TEXT_MODE
        send("Esc")

    # 新規作成、削除
    # def n(self):
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
        send("Esc")
        self.cursor_mode = self.MOVING_TEXT_MODE
    # def z(self):

    # 前を消す、後ろを消す
    # def g(self):
    # def h(self):

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
            send("Left")
        elif self.cursor_mode == self.SELECTING_TEXT_MODE:
            send("Left", "+")
        elif self.cursor_mode == self.SELECTING_KUKEI_TEXT_MODE:
            send("Left", "+")
    def l(self):
        if self.cursor_mode == self.MOVING_TEXT_MODE:
            send("Right")
        elif self.cursor_mode == self.SELECTING_TEXT_MODE:
            send("Right", "+")
        elif self.cursor_mode == self.SELECTING_KUKEI_TEXT_MODE:
            send("Right", "+")

    # 大きく移動
    def e(self):
        if self.cursor_mode == self.MOVING_TEXT_MODE:
            send("PageUp")
        elif self.cursor_mode == self.SELECTING_TEXT_MODE:
            send("Up", n "+",um = 10)
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
    # def m(self):

    # 探す
    def o(self):
        send("F", "#")
    # def p(self):

    # 調べる
    # def q(self):
    def w(self):
        pass

    # 変更、一つ選択、グループ選択、グループ選択
    def r(self):
        send("F3", "!")
    def t(self):
        send("D", "#")
        # send("T", "#!") #翻訳機能実行
    def s_t(self):
        send("U", "#")
    def y(self):
        send("Esc")
        self.cursor_mode = self.SELECTING_KUKEI_TEXT_MODE
    def u(self):
        send("Esc")
        self.cursor_mode = self.SELECTING_TEXT_MODE

class SubAppKeymap(base.SubAppKeymap):
    def init(self):
        # send("Esc")
        send("Esc")

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
        send("Up")            
    def k(self):
        send("Down")
    def j(self):
        send("PageUp", "#")
    def l(self):
        send("PageDown", "#")

    # 大きく移動
    def e(self):
        send("Esc")
        send("\\", "!")
    def d(self):
        send("Esc")
    def s(self):
        send("PageUp", "#")
    def f(self):
        send("PageDown", "#")

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
    # def u(self):
        
class SubNomalKeymap(base.SubNomalKeymap):
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
    # def p(self):

    # 調べる
    # def q(self):

    # 変更、一つ選択、グループ選択、グループ選択
    # def r(self):
    # def t(self):
    # def y(self):
    # def u(self):

class App(base.App):

    def __init__(self):
        self.app_name = None

        self.subnomal_keymap = SubNomalKeymap()
        self.app_keymap = AppKeymap()
        self.subapp_keymap = SubAppKeymap()