from app import base
from app.util import *

class AppKeymap(base.AppKeymap):
    def init(self):
        self.MOVING_TEXT_MODE = 0
        self.SELECTING_TEXT_MODE = 1
        self.cursor_mode = self.MOVING_TEXT_MODE
        # send("Esc") # Escをするとフルスクリーンビューを閉じてしまう

    # 新規作成、削除
    # def n(self):
    # def b(self):
    #     send("K", "#+")

    # コピー、貼り付け、切り取り、元に戻す
    def c(self):
        send("C", "#")

    def v(self):
        send("V", "#")

    def x(self):
        send("X", "#")
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

    def k(self):
        if self.cursor_mode == self.MOVING_TEXT_MODE:
            send("Down")
        elif self.cursor_mode == self.SELECTING_TEXT_MODE:
            send("Down", "+")

    def j(self):
        if self.cursor_mode == self.MOVING_TEXT_MODE:
            send("Left")
        elif self.cursor_mode == self.SELECTING_TEXT_MODE:
            send("Left", "+")

    def l(self):
        if self.cursor_mode == self.MOVING_TEXT_MODE:
            send("Right")
        elif self.cursor_mode == self.SELECTING_TEXT_MODE:
            send("Right", "+")

    # 大きく移動
    def e(self):
        send("Up", "!")
    def d(self):
        send("Down", "!")
    def s(self):
        send("[", "#") #戻る
    def f(self):
        send("]", "#") #進む

    # メモ
    # def m(self):

    # 探す
    def o(self):
        send("F", "#")
    # def p(self):

    # 調べる
    # def q(self):

    # 変更、一つ選択、グループ選択、グループ選択
    # def r(self):
    # def t(self):
    # def y(self):
    def u(self):
        self.cursor_mode = self.SELECTING_TEXT_MODE

class SubAppKeymap(base.SubAppKeymap):
    def init(self):
        pass
        # send("Esc") # Escをするとフルスクリーンビューを閉じてしまう

    # 新規作成、削除
    def n(self):
        send("T", "#") #新規タブ
    def b(self):
        send("W", "#") #タブを閉じる

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
        send("Tab", "^+") #左のタブ
    def l(self):
        send("Tab", "^") #右のタブ

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

    # 探す(試)
    def f(self):
        send("F", "#") # search
    # def g(self):

# class App(base.App):

#     def __init__(self):
#         super().__init__("com.apple.Safari", SubNomalKeymap, AppKeymap, SubAppKeymap)

keymaps = [base.NomalKeymap, SubNomalKeymap, AppKeymap, SubAppKeymap]
