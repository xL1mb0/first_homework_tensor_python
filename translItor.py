dictToRus = {'q':'й', 'w':'ц', 'e':'у', 'r':'к', 't':'е', 'y':'н', 'u':'г', 'i':'ш', 'o':'щ', 'p':'з', '[':'х', '{':'Х', ']':'ъ', '}':'Ъ', 'a':'ф', 's':'ы', 'd':'в', 'f':'а', 'g':'п', 'h':'р', 'j':'о', 'k':'л', 'l':'д', ';':'ж', ':':'Ж', "'":'э', '"':'Э', 'z':'я', 'x':'ч', 'c':'с', 'v':'м', 'b':'и', 'n':'т', 'm':'ь', ',':'б', '<':'Б', '.':'ю', '>':'Ю', '/':'.', '@':'"', '#':'№', '$':';', '^':':', '&':'?', '?':'.', '`':"ё", "~":'Ё'} 
dictToEng = {'й':'q', 'ц':'w', 'у':'e', 'к':'r', 'е':'t', 'н':'y', 'г':'u', 'ш':'i', 'щ':'o', 'з':'p', 'х':'[', 'Х':'{', 'ъ':']', 'Ъ':'}', 'ф':'a', 'ы':'s', 'в':'d', 'а':'f', 'п':'g', 'р':'h', 'о':'j', 'л':'k', 'д':'l', 'ж':';', 'Ж':':', 'э':"'", 'Э':'"', 'я':'z', 'ч':'x', 'с':'c', 'м':'v', 'и':'b', 'т':'n', 'ь':'m', 'б':',', 'Б':'<', 'ю':'.', 'Ю':'>', '.':'/', '"':'@', '№':'#', ';':'$', ':':'^', '?':'&', '.':"?", "ё":"`", "Ё":"~"}
print("------==== На случай забыто-переключенной раскладки ====------")
print("Для начала работы введите строку. Программа сама поймет, с какого на какой надо перевести.")
print("Режимы работы (автоматически выбирается):")
print("* с кривого русского на русский (ghbdth -> привет)")
print("* с кривого английского на английский (руддщ -> hello)")
print("Чтобы закончить работу программы, введите 0\n")

def toEng(symb):
    if symb in dictToEng: return dictToEng[symb]
    else: return symb

def toRus(symb):
    if symb in dictToRus: return dictToRus[symb]
    else: return symb

def translite(symb):
    global flag
    
    if (ord(symb) >= 97 and ord(symb) <= 122):
        flag = "E"
        return toRus(symb)
        
    if (ord(symb) >= 65 and ord(symb) <= 90):
        flag = "E"
        return chr(ord(toRus(chr(ord(symb)+32))) - 32)
        
    if (ord(symb) >= 1072 and ord(symb) <= 1103):
        flag = "R"
        return toEng(symb)
        
    if (ord(symb) >= 1040 and ord(symb) <= 1071 and symb not in "ХЪЖЭБЮЁ"):
        flag = "R"
        return chr(ord(toEng(chr(ord(symb)+32))) - 32)
        
    if (flag == "E"): return toRus(symb)
    return toEng(symb)
    
flag = ""

while True:
    line = input("Введите строку: ")
    if line == "0": break
    newLine = ""
    for symbol in line:
        newLine += translite(symbol)
    print(newLine)