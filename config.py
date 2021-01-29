# MacのIMEはデフォルトで２回Returnを押さないと変換されないので、キーボードの「入力ソース」を「Windows風のキー操作」に変更

import keyhac
import sys
import os

print(sys.version)

# Keyhacの実行n環境にKeyhacのパスが通っていないため、appモジュールを見つけられないので、自分でパスを通す必要がある。
sys.path.append("/Users/takeshitanaoki/Library/Application Support/Keyhac")
sys.path.append("/Users/takeshitanaoki/.pyenv/versions/3.7.5/lib/python3.7/site-packages")
sys.path.append("/Users/takeshitanaoki/.pyenv/versions/3.7.5/lib/python37.zip")
sys.path.append("/Users/takeshitanaoki/.pyenv/versions/3.7.5/lib/python3.7")
sys.path.append("/Users/takeshitanaoki/.pyenv/versions/3.7.5/lib/python3.7/lib-dynload")

# def configure(keymap):
#     # keymap_global = keymap.defineWindowKeymap()

#     #各アプリのキーバインド設定
#     from app import base
#     from app import vscode
#     from app import safari
#     from app import chrome
#     from app import finder

#     base.App(None, base.SubNomalKeymap, base.AppKeymap, base.SubAppKeymap).configure(keymap)
#     vscode.App().configure(keymap)
#     safari.App().configure(keymap)
#     chrome.App().configure(keymap)
#     finder.App().configure(keymap)

# ======================================
# Window: None 問題に対応するためapp_nameによるキーマップの振り分けを自ら行うように修正
# 問題がないかしばらく試す
# ======================================

def get_app():
    t = os.path.getmtime(get_app.path)
    if get_app.timestamp != t:
        get_app.timestamp = t
        with open(get_app.path) as f:
            get_app.name = f.read()
    return get_app.name
get_app.timestamp = 0
get_app.name = ""
get_app.path = "/Users/takeshitanaoki/Library/Application Support/Keyhac/app_name"

os.system("python \"/Users/takeshitanaoki/Library/Application Support/Keyhac/app_name.py\" &")
class Main:

    def __init__(self, keymap, app_keymaps):
        self.nomal_key_is_down = False
        self.app_key_is_down = False

        self.app_keymaps = app_keymaps
        self.app_name = "*"
        self.mode = 0
        self.keymap = None

        mapping = keymap.defineWindowKeymap()

        mapping["D-102"] = self.down_nomal_mode_key
        mapping["U-102"] = self.up_nomal_mode_key
        mapping["D-104"] = self.down_app_mode_key
        mapping["U-104"] = self.up_app_mode_key

        mapping["D-0"] = self.create_action("number_0")
        mapping["D-1"] = self.create_action("number_1")
        mapping["D-2"] = self.create_action("number_2")
        mapping["D-3"] = self.create_action("number_3")
        mapping["D-4"] = self.create_action("number_4")
        mapping["D-5"] = self.create_action("number_5")
        mapping["D-6"] = self.create_action("number_6")
        mapping["D-7"] = self.create_action("number_7")
        mapping["D-8"] = self.create_action("number_8")
        mapping["D-9"] = self.create_action("number_9")

        mapping["D-A"] = self.create_action("a")
        mapping["D-B"] = self.create_action("b")
        mapping["D-C"] = self.create_action("c")
        mapping["D-D"] = self.create_action("d")
        mapping["D-E"] = self.create_action("e")
        mapping["D-F"] = self.create_action("f")
        mapping["D-G"] = self.create_action("g")
        mapping["D-H"] = self.create_action("h")
        mapping["D-I"] = self.create_action("i")
        mapping["D-J"] = self.create_action("j")
        mapping["D-K"] = self.create_action("k")
        mapping["D-L"] = self.create_action("l")
        mapping["D-M"] = self.create_action("m")
        mapping["D-N"] = self.create_action("n")
        mapping["D-O"] = self.create_action("o")
        mapping["D-P"] = self.create_action("p")
        mapping["D-Q"] = self.create_action("q")
        mapping["D-R"] = self.create_action("r")
        mapping["D-S"] = self.create_action("s")
        mapping["D-T"] = self.create_action("t")
        mapping["D-U"] = self.create_action("u")
        mapping["D-V"] = self.create_action("v")
        mapping["D-W"] = self.create_action("w")
        mapping["D-X"] = self.create_action("x")
        mapping["D-Y"] = self.create_action("y")
        mapping["D-Z"] = self.create_action("z")
        mapping["D-Semicolon"] = self.create_action("semicolon")

    def down_nomal_mode_key(self):
        if not self.nomal_key_is_down:
            self.nomal_key_is_down = True
            self.mode = 1
            self.update_keymap()

    def up_nomal_mode_key(self):
        self.nomal_key_is_down = False
        self.mode = 0
        self.update_keymap()

    def down_app_mode_key(self):
        if not self.app_key_is_down:
            self.app_key_is_down = True
            self.mode = 3
            self.update_keymap()

    def up_app_mode_key(self):
        self.app_key_is_down = False
        self.mode = 2
        self.update_keymap()

    def update_keymap(self):
        self.app_name = get_app()
        if self.app_name not in self.app_keymaps:
            self.app_name = "*"

        app_keymap = self.app_keymaps[self.app_name][self.mode]
        if not isinstance(self.keymap, app_keymap):
            self.keymap = app_keymap()

    def create_action(self, key):
        _self = self
        def action():
            _self.update_keymap()
            getattr(_self.keymap ,key)()
        return action

def configure(keymap):
    from app import base
    from app import vscode
    from app import safari
    from app import chrome
    from app import finder

    app_keymaps = {
        "*": vscode.keymaps,
        "Code": vscode.keymaps,
        "Google Chrome": chrome.keymaps,
        "Finder": finder.keymaps,
        "Safari": safari.keymaps,
    }
    Main(keymap, app_keymaps)