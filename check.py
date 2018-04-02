from returnfunct import error
from allfuncts import ope, char

def checkquotes(str):
    i = 0
    l = len(str)
    quote = 0
    while i < l:
        if str[i] == '(': quote += 1
        if str[i] == ')': quote -= 1
        i += 1
    return quote


def checkrequest(str):
    if "<=>" in str:
        error("Biconditional rules (<=>) are not managed.")
    split = str.split('=>')
    if len(split) < 2: error("\033[31m"+str+"\033[0m is undetermined, because of missing the implication.")
    if len(split) > 2: error("\033[31m"+str+"\033[0m is undetermined, because of a multiple implication.")
    if '(' in split[1] or ')' in split[1]: error("\033[31m"+str+"\033[0m parentheses should be used only before implication.")
    if '|' in split[1] or '^' in split[1]: error("\033[31m"+str+"\033[0m OR and XOR should be used only before implication.")
    if checkquotes(split[0]) != 0: error("\033[31m"+str+"\033[0m Parentheses error.")


def formatreq(str):
    str = str.replace("(", " ( ").replace(")", " ) ").replace("^", " ^ ").replace("+", " + ").replace("|", " | ").replace("! ", "!").replace("!", " !").replace("=>", " => ")
    str = str.replace("  ", " ")
    str = str.replace("  ", " ")
    str = str.strip(' ')
    split = str.split(' ')
    i = 0
    l = len(split)
    while i < l - 1:
        if ope(split[i]) == 1 and ope(split[i + 1]) == 1 : error("\033[31m"+str+"\033[0m Syntax error.")
        if char(split[i]) == 1 and char(split[i + 1]) == 1 : error("\033[31m"+str+"\033[0m Syntax error.")
        if char(split[i]) == 0 and ope(split[i]) == 0 and split[i] != '(' and split[i] != ')' and split[i] != '=>' : error("\033[31m"+str+"\033[0m Syntax error.")
        if ope(split[i]) == 1 and split[i + 1] == ')' : error("\033[31m"+str+"\033[0m Syntax error.")
        if ope(split[i + 1]) == 1 and split[i] == '(' : error("\033[31m"+str+"\033[0m Syntax error.")
        if split[i] == '(' and split[i + 1] == ')' : error("\033[31m"+str+"\033[0m Syntax error.")
        if split[i] == ')' and split[i + 1] == '(' : error("\033[31m"+str+"\033[0m Syntax error.")
        i += 1
    if char(split[i]) == 0 and ope(split[i]) == 0 and split[i] != '(' and split[i] != ')' and split[i] != '=>' : error("\033[31m"+str+"\033[0m Syntax error.")
    return str


def checkfunct(request, letterlist, askletter):
    i = 0
    l = len(request)
    while i < l:
        checkrequest(request[i]) == 0
        request[i] = formatreq(request[i])
        i += 1