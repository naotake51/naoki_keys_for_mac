from keyhac import *

char_to_vk = {
    # https://www.it-swarm-ja.tech/ja/macos/macの仮想キーコードのリストはどこにありますか？/969430761/
    "BackSpace" : 0x33, # Delと同じ
    "Tab" : 0x30,
    "Clear" : 12,
    "Enter" : 0x24,
    "Shift" : 0x38,
    "Control" : 0x3B,
    # "Alt" : 18,
    # "Pause" : 19,
    # "Capital" : 20, #Shift+CapsLock
    "Esc" : 0x35,
    # "変換" : 28,
    # "無変換" : 29,
    "Space" : 0x31,
    "PageUp" : 0x74,
    "PageDown" : 0x79,
    "End" : 0x77,
    "Home" : 0x73,
    "Left" : 0x7B,
    "Up" : 0x7E,
    "Right" : 0x7C,
    "Down" : 0x7D,
    "PrintScreen" : 44,
    # "Ins" : 45,
    "Del" : 0x33,
    "0" : 0x1D,
    "1" : 0x12,
    "2" : 0x13,
    "3" : 0x14,
    "4" : 0x15,
    "5" : 0x17,
    "6" : 0x16,
    "7" : 0x1A,
    "8" : 0x1C,
    "9" : 0x19,
    "A" : 0x00,
    "B" : 0x0B,
    "C" : 0x08,
    "D" : 0x02,
    "E" : 0x0E,
    "F" : 0x03,
    "G" : 0x05,
    "H" : 0x04,
    "I" : 0x22,
    "J" : 0x26,
    "K" : 0x28,
    "L" : 0x25,
    "M" : 0x2E,
    "N" : 0x2D,
    "O" : 0x1F,
    "P" : 0x23,
    "Q" : 0x0C,
    "R" : 0x0F,
    "S" : 0x01,
    "T" : 0x11,
    "U" : 0x20,
    "V" : 0x09,
    "W" : 0x0D,
    "X" : 0x07,
    "Y" : 0x10,
    "Z" : 0x06,
    # "LWin" : 91,
    # "RWin" : 92,
    # "Apps" : 93,
    # "Num0" : 96,
    # "Num1" : 97,
    # "Num2" : 98,
    # "Num3" : 99,
    # "Num4" : 100,
    # "Num5" : 101,
    # "Num6" : 102,
    # "Num7" : 103,
    # "Num8" : 104,
    # "Num9" : 105,
    # "Tenkey *" : 106,
    # "Tenkey +" : 107,
    # "Tenkey -" : 109,
    # "Tenkey ." : 110,
    # "Tenkey /" : 111,
    "F1" : 0x7A,
    "F2" : 0x78,
    "F3" : 0x63,
    "F4" : 0x76,
    "F5" : 0x60,
    "F6" : 0x61,
    "F7" : 0x62,
    "F8" : 0x64,
    "F9" : 0x65,
    "F10" : 0x6D,
    "F11" : 0x67,
    "F12" : 0x6F,
    "F13" : 0x69,
    "F14" : 0x6B,
    "F15" : 0x71, 
    "F16" : 0x6A,
    "F17" : 0x40, 
    "F18" : 0x4F, 
    "F19" : 0x50, 
    "F20" : 0x5A, 
    # "NumLock" : 144,
    # "ScrollLock" : 145,
    ":" : 0x27,
    ";" : 0x29,
    "," : 0x2B,
    "Minus" : 0x1B, #-をセパレーターとして使っているので使用できない
    "." : 0x2F,
    "/" : 0x2C,
    "@" : 0x21,
    "[" : 0x1E,
    "Yen" : 220,
    "]" : 0x2A, #わからない。http://www2d.biglobe.ne.jp/~msyk/keyboard/layout/usbkeycode.html を参考
    "^" : 222,
    "\\" : 0x2A,
    # "半角/全角" : 229,
    # "前候補" : 229,
    # "CapsLock" : 240,
    # "カタカナひらがな" : 242,
    # Mac用に追加
    "Command": 0x37,
    "Option": 0x3A,
    "英数": 102,
    "かな": 104,
    "`" : 0x32

}

vk_command = char_to_vk["Command"] # #
vk_ctrl = char_to_vk["Control"] # ^
vk_shift = char_to_vk["Shift"] # +
vk_option = char_to_vk["Option"] # !

def send(key, modifier = "", num = 1):
    vk = char_to_vk[key]

    if "D" in modifier:
        key_command_list = []
        if "#" in modifier: key_command_list += [KeyDown(vk_command)]
        if "^" in modifier: key_command_list += [KeyDown(vk_ctrl)]
        if "+" in modifier: key_command_list += [KeyDown(vk_shift)]
        if "!" in modifier: key_command_list += [KeyDown(vk_option)]
        key_command_list += [KeyDown(vk) for i in range(0, num)]
    elif "U" in modifier:
        key_command_list = []
        if "#" in modifier: key_command_list += [KeyUp(vk_command)]
        if "^" in modifier: key_command_list += [KeyUp(vk_ctrl)]
        if "+" in modifier: key_command_list += [KeyUp(vk_shift)]
        if "!" in modifier: key_command_list += [KeyUp(vk_option)]
        key_command_list += [KeyUp(vk) for i in range(0, num)]
    else:
        key_command_list = []
        if "#" in modifier: key_command_list += [KeyDown(vk_command)]
        if "^" in modifier: key_command_list += [KeyDown(vk_ctrl)]
        if "+" in modifier: key_command_list += [KeyDown(vk_shift)]
        if "!" in modifier: key_command_list += [KeyDown(vk_option)]
        key_command_list += [Key(vk) for i in range(0, num)]
        if "!" in modifier: key_command_list += [KeyUp(vk_option)]
        if "+" in modifier: key_command_list += [KeyUp(vk_shift)]
        if "^" in modifier: key_command_list += [KeyUp(vk_ctrl)]
        if "#" in modifier: key_command_list += [KeyUp(vk_command)]

    Input.send(key_command_list)

def send_string(string):
    key_command_list = []
    for c in string:
        key_command_list.append(Char(c))
    Input.send(key_command_list)
