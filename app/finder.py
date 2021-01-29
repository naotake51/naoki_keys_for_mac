from app import base
from app.util import *        

# Finder上部にフルパスを表示させる方法
# defaults write com.apple.finder _FXShowPosixPathInTitle -boolean true ※ or false
# killall Finder

class AppKeymap(base.AppKeymap):
    def init(self):
        pass

    # 新規作成、削除
    def n(self):
        send("N", "#+") #ディレクトリを作成
    def b(self):
        send("BackSpace", "#") #ファイル、ディレクトリ削除

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
    def s(self):
        send("[", "#") #履歴戻る
    def f(self):
        send("]", "#") #履歴進む

    # メモ
    def m(self):
        send("C", "#!") #フルパスをコピー ※ファイルやディレクトリを選択している場合はそのフルパスを、何も選択していない場合はカレントディレクトリのフルパスをコピーする

    # 探す
    def o(self):
        send("F", "#")
    # def p(self):

    # 調べる
    # def q(self):

    # 変更、一つ選択、グループ選択、グループ選択
    # def r(self):
    # def t(self):
    def y(self):
        send("1", "#") #表示形式をアイコンに切り替える
    def u(self):
        send("2", "#") #表示形式をリストに切り替える

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
        send("Up", "#") #親ディレクトリへ
    def k(self):
        send("Down", "#") #子ディレクトリへ ファイルの場合は開く動作になる
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

class App(base.App):

    def __init__(self):
        super().__init__("com.apple.finder", SubNomalKeymap, AppKeymap, SubAppKeymap)

keymaps = [base.NomalKeymap, SubNomalKeymap, AppKeymap, SubAppKeymap]
