import sys
import os

from keyhac import *

sys.path.append("/Users/takeshitanaoki/Library/Application Support/Keyhac")

import app.util

def test():
    pass    

def configure(keymap):

    keymap_global = keymap.defineWindowKeymap()

    #各アプリのキーバインド設定
    from app import base
    from app import vscode

    base.App().configure(keymap)
    vscode.App().configure(keymap)

    #開発補助
    keymap_global["F12"] = test
