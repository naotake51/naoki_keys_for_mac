# MacのIMEはデフォルトで２回Returnを押さないと変換されないので、キーボードの「入力ソース」を「Windows風のキー操作」に変更

import sys
import os

from keyhac import *

# Keyhacの実行環境にKeyhacのパスが通っていないため、appモジュールを見つけられないので、自分でパスを通す必要がある。
sys.path.append("/Users/takeshitanaoki/Library/Application Support/Keyhac")

import app.util

# def test():
#     pass    

def configure(keymap):
    keymap_global = keymap.defineWindowKeymap()

    #各アプリのキーバインド設定
    from app import base
    from app import vscode
    from app import safari

    base.App().configure(keymap)
    vscode.App().configure(keymap)
    safari.App().configure(keymap)

    #開発補助
    # keymap_global["Ctrl-Right"] = "Right"
