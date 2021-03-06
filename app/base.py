from app.util import *
# import sys, pprint
# pprint.pprint(sys.path)
# pprint.pprint(sys.version)
# import pyautogui

class Keymap():
    def __init__(self): pass

    def a(self):pass
    def b(self):pass
    def c(self):pass
    def d(self):pass
    def e(self):pass
    def f(self):pass
    def g(self):pass
    def h(self):pass
    def i(self):pass
    def j(self):pass
    def k(self):pass
    def l(self):pass
    def m(self):pass
    def n(self):pass
    def o(self):pass
    def p(self):pass
    def q(self):pass
    def r(self):pass
    def s(self):pass
    def t(self):pass
    def u(self):pass
    def v(self):pass
    def w(self):pass
    def x(self):pass
    def y(self):pass
    def z(self):pass
    def semicolon(self):pass
    def number_0(self): pass
    def number_1(self): pass
    def number_2(self): pass
    def number_3(self): pass
    def number_4(self): pass
    def number_5(self): pass
    def number_6(self): pass
    def number_7(self): pass
    def number_8(self): pass
    def number_9(self): pass
class NomalKeymap(Keymap):
    def a(self):send("A")
    def b(self):send("B")
    def c(self):send("C")
    def d(self):send("D")
    def e(self):send("E")
    def f(self):send("F")
    def g(self):send("G")
    def h(self):send("H")
    def i(self):send("I")
    def j(self):send("J")
    def k(self):send("K")
    def l(self):send("L")
    def m(self):send("M")
    def n(self):send("N")
    def o(self):send("O")
    def p(self):send("P")
    def q(self):send("Q")
    def r(self):send("R")
    def s(self):send("S")
    def t(self):send("T")
    def u(self):send("U")
    def v(self):send("V")
    def w(self):send("W")
    def x(self):send("X")
    def y(self):send("Y")
    def z(self):send("Z")
    def semicolon(self):send(";")
    def number_0(self): send("0")
    def number_1(self): send("1")
    def number_2(self): send("2")
    def number_3(self): send("3")
    def number_4(self): send("4")
    def number_5(self): send("5")
    def number_6(self): send("6")
    def number_7(self): send("7")
    def number_8(self): send("8")
    def number_9(self): send("9")
class SubNomalKeymap(Keymap):
    def __init__(self):
        super().__init__()
        send("英数")
    def a(self):
        send("Space", "!") # Alfred Open!
    # def e(self):send("英数") # 不要
    def n(self):send("かな")

class AppKeymap(Keymap):
    def __init__(self):
        super().__init__()
    def w(self):
        send("V", "#^") # Clipy
    def q(self):
        send("B", "#^") # Clipy

class SubAppKeymap(Keymap):
    def __init__(self):
        super().__init__()
    # keyhacを起動すると、Mission Controlのショートカットが効かなくなるバグがある
    # https://github.com/crftwr/keyhac/issues/26
    # def e(self):send("Up", "#")
    # def f(self):send("Right", "#")
    # def s(self):
    #     pyautogui.press('e')
    def s(self):
        send(",", "#") # keyhacを起動している状態だと、なぜか「^Left」,「#Left」のショートカットが動かなくなるので、キーボードの設定でショートカットを変更した。
    def f(self):
        send(".", "#") # keyhacを起動している状態だと、なぜか「^Right」,「#Right」のショートカットが動かなくなる、キーボードの設定でショートカットを変更した。

# class App():
#     nomal_key_is_down = False
#     app_key_is_down = False

#     def __init__(self, app_name, subnomal_keymap, app_keymap, subapp_keymap):
#         self.app_name = app_name
#         self.nomal_keymap = NomalKeymap
#         self.subnomal_keymap = subnomal_keymap
#         self.app_keymap = app_keymap
#         self.subapp_keymap = subapp_keymap
#         self.keymap = self.nomal_keymap()

#     def down_nomal_mode_key(self):
#         if not self.nomal_key_is_down:
#             self.nomal_key_is_down = True
#             self.keymap = self.subnomal_keymap()

#     def up_nomal_mode_key(self):
#         self.nomal_key_is_down = False
#         self.keymap = self.nomal_keymap()

#     def down_app_mode_key(self):
#         if not self.app_key_is_down:
#             self.app_key_is_down = True
#             self.keymap = self.subapp_keymap()

#     def up_app_mode_key(self):
#         self.app_key_is_down = False
#         self.keymap = self.app_keymap()

#     def put_a(self): self.keymap.a()
#     def put_b(self): self.keymap.b()
#     def put_c(self): self.keymap.c()
#     def put_d(self): self.keymap.d()
#     def put_e(self): self.keymap.e()
#     def put_f(self): self.keymap.f()
#     def put_g(self): self.keymap.g()
#     def put_h(self): self.keymap.h()
#     def put_i(self): self.keymap.i()
#     def put_j(self): self.keymap.j()
#     def put_k(self): self.keymap.k()
#     def put_l(self): self.keymap.l()
#     def put_m(self): self.keymap.m()
#     def put_n(self): self.keymap.n()
#     def put_o(self): self.keymap.o()
#     def put_p(self): self.keymap.p()
#     def put_q(self): self.keymap.q()
#     def put_r(self): self.keymap.r()
#     def put_s(self): self.keymap.s()
#     def put_t(self): self.keymap.t()
#     def put_u(self): self.keymap.u()
#     def put_v(self): self.keymap.v()
#     def put_w(self): self.keymap.w()
#     def put_x(self): self.keymap.x()
#     def put_y(self): self.keymap.y()
#     def put_z(self): self.keymap.z()
#     def put_semicolon(self): self.keymap.semicolon()

#     def configure(self, keymap):
#         if self.app_name:
#             mapping = keymap.defineWindowKeymap(app_name=self.app_name)
#         else:
#             mapping = keymap.defineWindowKeymap()

#         mapping["D-102"] = self.down_nomal_mode_key
#         mapping["U-102"] = self.up_nomal_mode_key
#         mapping["D-104"] = self.down_app_mode_key
#         mapping["U-104"] = self.up_app_mode_key

#         mapping["D-A"] = self.put_a
#         mapping["D-B"] = self.put_b
#         mapping["D-C"] = self.put_c
#         mapping["D-D"] = self.put_d
#         mapping["D-E"] = self.put_e
#         mapping["D-F"] = self.put_f
#         mapping["D-G"] = self.put_g
#         mapping["D-H"] = self.put_h
#         mapping["D-I"] = self.put_i
#         mapping["D-J"] = self.put_j
#         mapping["D-K"] = self.put_k
#         mapping["D-L"] = self.put_l
#         mapping["D-M"] = self.put_m
#         mapping["D-N"] = self.put_n
#         mapping["D-O"] = self.put_o
#         mapping["D-P"] = self.put_p
#         mapping["D-Q"] = self.put_q
#         mapping["D-R"] = self.put_r
#         mapping["D-S"] = self.put_s
#         mapping["D-T"] = self.put_t
#         mapping["D-U"] = self.put_u
#         mapping["D-V"] = self.put_v
#         mapping["D-W"] = self.put_w
#         mapping["D-X"] = self.put_x
#         mapping["D-Y"] = self.put_y
#         mapping["D-Z"] = self.put_z

keymaps = [NomalKeymap, SubNomalKeymap, AppKeymap, SubAppKeymap]
