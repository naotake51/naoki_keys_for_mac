from keyhac import *

char_to_vk = {
    "BackSpace" : 8,
    "Tab" : 9,
    "Clear" : 12,
    "Enter" : 13,
    "Shift" : 16,
    "Ctrl" : 17,
    "Alt" : 18,
    "Pause" : 19,
    "Capital" : 20, #Shift+CapsLock
    "Esc" : 27,
    "変換" : 28,
    "無変換" : 29,
    "Space" : 32,
    "PageUp" : 33,
    "PageDown" : 34,
    "End" : 35,
    "Home" : 36,
    "Left" : 37,
    "Up" : 38,
    "Right" : 39,
    "Down" : 40,
    "PrintScreen" : 44,
    "Ins" : 45,
    "Del" : 46,
    "0" : 48,
    "1" : 49,
    "2" : 50,
    "3" : 51,
    "4" : 52,
    "5" : 53,
    "6" : 54,
    "7" : 55,
    "8" : 56,
    "9" : 57,
    "A" : 65,
    "B" : 66,
    "C" : 67,
    "D" : 68,
    "E" : 69,
    "F" : 70,
    "G" : 71,
    "H" : 72,
    "I" : 73,
    "J" : 74,
    "K" : 75,
    "L" : 76,
    "M" : 77,
    "N" : 78,
    "O" : 79,
    "P" : 80,
    "Q" : 81,
    "R" : 82,
    "S" : 83,
    "T" : 84,
    "U" : 85,
    "V" : 86,
    "W" : 87,
    "X" : 88,
    "Y" : 89,
    "Z" : 90,
    "LWin" : 91,
    "RWin" : 92,
    "Apps" : 93,
    "Num0" : 96,
    "Num1" : 97,
    "Num2" : 98,
    "Num3" : 99,
    "Num4" : 100,
    "Num5" : 101,
    "Num6" : 102,
    "Num7" : 103,
    "Num8" : 104,
    "Num9" : 105,
    "Tenkey *" : 106,
    "Tenkey +" : 107,
    "Tenkey -" : 109,
    "Tenkey ." : 110,
    "Tenkey /" : 111,
    "F1" : 112,
    "F2" : 113,
    "F3" : 114,
    "F4" : 115,
    "F5" : 116,
    "F6" : 117,
    "F7" : 118,
    "F8" : 119,
    "F9" : 120,
    "F10" : 121,
    "F11" : 122,
    "F12" : 123,
    "NumLock" : 144,
    "ScrollLock" : 145,
    ":" : 186,
    ";" : 187,
    "," : 188,
    "Minus" : 189, #-をセパレーターとして使っているので使用できない
    "." : 190,
    "/" : 191,
    "@" : 192,
    "[" : 219,
    "Yen" : 220,
    "]" : 221,
    "^" : 222,
    "\\" : 226,
    "半角/全角" : 229,
    "前候補" : 229,
    "CapsLock" : 240,
    "カタカナひらがな" : 242,
}

def send(key, num = 1):
    print("send " + key)
    vk_alt = char_to_vk["Alt"]
    vk_shift = char_to_vk["Shift"]
    vk_ctrl = char_to_vk["Ctrl"]

    token_list = key.split("-")
    modifier_list = token_list[:-1]
    char = token_list[-1]
    vk = char_to_vk[char]
    
    if "D" in modifier_list:
        key_command_list = []
        if "A" in modifier_list: key_command_list += [KeyDown(vk_alt)]
        if "S" in modifier_list: key_command_list += [KeyDown(vk_shift)]
        if "C" in modifier_list: key_command_list += [KeyDown(vk_ctrl)]
        key_command_list += [KeyDown(vk) for i in range(0, num)]
    elif "U" in modifier_list:
        key_command_list = []
        if "A" in modifier_list: key_command_list += [KeyUp(vk_alt)]
        if "S" in modifier_list: key_command_list += [KeyUp(vk_shift)]
        if "C" in modifier_list: key_command_list += [KeyUp(vk_ctrl)]
        key_command_list += [KeyUp(vk) for i in range(0, num)]
    else:
        key_command_list = []
        if "A" in modifier_list: key_command_list += [KeyDown(vk_alt)]
        if "S" in modifier_list: key_command_list += [KeyDown(vk_shift)]
        if "C" in modifier_list: key_command_list += [KeyDown(vk_ctrl)]
        key_command_list += [Key(vk) for i in range(0, num)]
        if "C" in modifier_list: key_command_list += [KeyUp(vk_ctrl)]
        if "S" in modifier_list: key_command_list += [KeyUp(vk_shift)]
        if "A" in modifier_list: key_command_list += [KeyUp(vk_alt)]

    Input.send(key_command_list)
    
def send_string(string):
    key_command_list = []
    for c in string:
        key_command_list.append(Char(c))
    Input.send(key_command_list)
