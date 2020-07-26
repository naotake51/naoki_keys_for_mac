# MacのIMEはデフォルトで２回Returnを押さないと変換されないので、キーボードの「入力ソース」を「Windows風のキー操作」に変更

import sys
import os

# Keyhacの実行環境にKeyhacのパスが通っていないため、appモジュールを見つけられないので、自分でパスを通す必要がある。
sys.path.append("/Users/takeshitanaoki/Library/Application Support/Keyhac")

import keyhac
dir(keyhac)

# import app.util

# def test():
#     pass    

def configure(keymap):
    # keymap_global = keymap.defineWindowKeymap()

    #各アプリのキーバインド設定
    from app import base
    from app import vscode
    from app import safari
    from app import chrome

    base.App().configure(keymap)
    vscode.App().configure(keymap)
    safari.App().configure(keymap)
    chrome.App().configure(keymap)

    #開発補助
    # keymap_global["Ctrl-Right"] = "Right"

# -------------------------------------------
# スペース切り替えのショートカットが動作しない問題を調査
# -------------------------------------------

# # Mission Controlで右デスクトップに移動する
# function switch_to_right_screen {
#     osascript -e 'tell application "System Events" to tell process "WindowServer"
#         key code 124 using control down
#     end tell'
# }

# # Mission Controlで左デスクトップに移動する
# function switch_to_left_screen {
#     osascript -e 'tell application "System Events" to tell process "WindowServer"
#         key code 123 using control down
#     end tell'
# }

# /System/Applications/Mission\ Control.app/Contents/MacOS/Mission\ Control 1

# strings /System/Applications/Mission\ Control.app/Contents/MacOS/Mission\ Control
#     com.apple.expose.awake
#     com.apple.showdesktop.awake
#     com.apple.expose.front.awake