from app.util import *        

class Keymap():
    def __init__(self): pass

    def init(self):pass
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

class NomalKeymap(Keymap):
    def a(self):send("D-A")
    def b(self):send("D-B")
    def c(self):send("D-C")
    def d(self):send("D-D")
    def e(self):send("D-E")
    def f(self):send("D-F")
    def g(self):send("D-G")
    def h(self):send("D-H")
    def i(self):send("D-I")
    def j(self):send("D-J")
    def k(self):send("D-K")
    def l(self):send("D-L")
    def m(self):send("D-M")
    def n(self):send("D-N")
    def o(self):send("D-O")
    def p(self):send("D-P")
    def q(self):send("D-Q")
    def r(self):send("D-R")
    def s(self):send("D-S")
    def t(self):send("D-T")
    def u(self):send("D-U")
    def v(self):send("D-V")
    def w(self):send("D-W")
    def x(self):send("D-X")
    def y(self):send("D-Y")
    def z(self):send("D-Z")    

class SubNomalKeymap(Keymap):
    pass

class AppKeymap(Keymap):
    pass

class SubAppKeymap(Keymap):
    pass

class App():
    nomal_key_is_down = False
    app_key_is_down = False
    nomal_keymap = NomalKeymap()

    def __init__(self):
        self.app_name = None

        self.subnomal_keymap = SubNomalKeymap()
        self.app_keymap = AppKeymap()
        self.subapp_keymap = SubAppKeymap()

        self.keymap = self.nomal_keymap

    def down_nomal_mode_key(self):
        print("down_nomal_mode_key")
        if not self.nomal_key_is_down:
            self.nomal_key_is_down = True
            self.keymap = self.subnomal_keymap
            self.keymap.init()
    
    def up_nomal_mode_key(self):
        print("up_nomal_mode_key")
        self.nomal_key_is_down = False
        self.keymap = self.nomal_keymap
        self.keymap.init()

    def down_app_mode_key(self):
        print("down_app_mode_key")
        if not self.app_key_is_down:
            self.app_key_is_down = True
            self.keymap = self.subapp_keymap
            self.keymap.init()
    
    def up_app_mode_key(self):
        print("up_app_mode_key")
        self.app_key_is_down = False
        self.keymap = self.app_keymap
        self.keymap.init()

    def put_a(self): self.keymap.a()
    def put_b(self): self.keymap.b()
    def put_c(self): self.keymap.c()
    def put_d(self): self.keymap.d()
    def put_e(self): self.keymap.e()
    def put_f(self): self.keymap.f()
    def put_g(self): self.keymap.g()
    def put_h(self): self.keymap.h()
    def put_i(self): self.keymap.i()
    def put_j(self): self.keymap.j()
    def put_k(self): self.keymap.k()
    def put_l(self): self.keymap.l()
    def put_m(self): self.keymap.m()
    def put_n(self): self.keymap.n()
    def put_o(self): self.keymap.o()
    def put_p(self): self.keymap.p()
    def put_q(self): self.keymap.q()
    def put_r(self): self.keymap.r()
    def put_s(self): self.keymap.s()
    def put_t(self): self.keymap.t()
    def put_u(self): self.keymap.u()
    def put_v(self): self.keymap.v()
    def put_w(self): self.keymap.w()
    def put_x(self): self.keymap.x()
    def put_y(self): self.keymap.y()
    def put_z(self): self.keymap.z()

    def configure(self, keymap):
        if self.app_name:
            keymap = keymap.defineWindowKeymap(app_name=self.app_name)
        else:
            keymap = keymap.defineWindowKeymap()
    
        keymap["D-102"] = self.down_nomal_mode_key
        keymap["U-102"] = self.up_nomal_mode_key
        keymap["D-104"] = self.down_nomal_mode_key
        keymap["U-104"] = self.up_nomal_mode_key
        keymap["D-RCmd"] = self.down_app_mode_key
        keymap["U-RCmd"] = self.up_app_mode_key
        
        keymap["D-A"] = self.put_a
        keymap["D-B"] = self.put_b
        keymap["D-C"] = self.put_c
        keymap["D-D"] = self.put_d
        keymap["D-E"] = self.put_e
        keymap["D-F"] = self.put_f
        keymap["D-G"] = self.put_g
        keymap["D-H"] = self.put_h
        keymap["D-I"] = self.put_i
        keymap["D-J"] = self.put_j
        keymap["D-K"] = self.put_k
        keymap["D-L"] = self.put_l
        keymap["D-M"] = self.put_m
        keymap["D-N"] = self.put_n
        keymap["D-O"] = self.put_o
        keymap["D-P"] = self.put_p
        keymap["D-Q"] = self.put_q
        keymap["D-R"] = self.put_r
        keymap["D-S"] = self.put_s
        keymap["D-T"] = self.put_t
        keymap["D-U"] = self.put_u
        keymap["D-V"] = self.put_v
        keymap["D-W"] = self.put_w
        keymap["D-X"] = self.put_x
        keymap["D-Y"] = self.put_y
        keymap["D-Z"] = self.put_z