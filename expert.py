import sys
from opelogic import *
from allfuncts import *
from returnfunct import *
from check import *
import fcntl, termios, struct
import errno, os


def replacequotes(split, begin, end, letterlist):
    i = 0
    while i <= end and split[i] != ")":
        if split[i] == "(": op = i
        i += 1
    cl = i
    res = checkreq(split, op + 1, cl - 1, letterlist)
    while split[op] != ')':
        del split[op]
    split[op] = str(res)


def checkreq(split, begin, end, letterlist):
    # fonction recursive pour checker si la proposition est vraie
    if end - begin < 1: return (letterfunct(split[begin], letterlist))
    elif end - begin < 3:
        if split[begin + 1] == "+": return andfunct(split[begin], split[end], letterlist)
        if split[begin + 1] == "|": return orfunct(split[begin], split[end], letterlist)
        if split[begin + 1] == "^": return xorfunct(split[begin], split[end], letterlist)
    elif segments(split, begin, end) == 0:
        btwo, etwo = priority(split, begin, end)
        res = checkreq(split, btwo, etwo, letterlist)
        split[btwo] = str(res)
        del split[btwo + 1]
        del split[btwo + 1]
        return checkreq(split, begin, end - 2, letterlist)
    else:
        while (segments(split, begin, end) == 1):
            replacequotes(split, begin, end, letterlist)
        end = findend(split) - 1
        return checkreq(split, begin, end, letterlist)
    return 0


def decrypt(request, letterlist):
    split = str.split(request)
    i = findend(split)
    if checkreq(split, 0, i - 1, letterlist):
        # print("propal ok")
        return putletteron(split, findend(split) + 1, letterlist)
    else:
        # print("propal ko")
        return letterlist


def expert(request, letterlist, askletter):
    checkfunct(request, letterlist, askletter)
    printfirstreq(request)        
    print("\033[0;4mTrue letters list:\033[0;0m \033[0;1m{}\033[0;0m".format(letterlist))
    print("\033[0;4mAsked letters list:\033[0;0m \033[0;1m{}\033[0;0m\n\n\n\033[34;1;4mRESOLUTION\033[0;0m\n".format(askletter))
    i = 0
    l = len(request)
    while i < l:
        ret = decrypt(request[i], letterlist)
        if ret != letterlist: 
            letterlist = ret
            printreq(request[i], letterlist)
            i = -1
        i += 1
    print("\n\033[34;1;4mRESULTS\033[0;0m\n")
    printres(askletter, letterlist)


def terminal_size():
    th, tw, hp, wp = struct.unpack('HHHH',
        fcntl.ioctl(0, termios.TIOCGWINSZ,
        struct.pack('HHHH', 0, 0, 0, 0)))
    return tw


def main(argv):
    av = 0
    if len(argv) == 0:
        print("usage: python3 expert.py [file ...]")
        sys.exit(1)
    while av < len(argv):
        try: fd = open(argv[av], 'r')
        except IndexError:
            print("usage: python3 expert.py [file ...]")
            sys.exit(1)
        except FileNotFoundError:
            print("File "+argv[av]+" do not exist.")
            sys.exit(1)
        except IsADirectoryError:
            print(argv[av]+" is a directory, try it with a file.\nusage: python3 expert.py [file ...]")
            sys.exit(1)
        except IOError as e:
            print(os.strerror(e.errno))
            sys.exit(1)
        try: text = fd.read()
        except:
            print("File reading error.")
            sys.exit(1)
        text = text.split("\n")
        i = 0
        while i < len(text):
            text[i] = text[i].strip()
            if text[i] == "" or text[i][0] == '#':
                del text[i]
                i = -1
            elif '#' in text[i]:
                text[i] = text[i].split("#", 1)[0]
            i += 1
        request = []
        letterlist = ""
        askletter = ""
        i = 0
        l = len(text)
        while i < l:
            if text[i][0] == '=': letterlist = text[i].replace("=", "")
            elif text[i][0] == '?': askletter = text[i].replace("?", "")
            else: request.append(text[i])
            i += 1
        width = "_"*terminal_size()
        spaces = " "*int(len(width) / 2 - (len(argv[av]) / 2))
        print("\033[34;1m{}{}\n{}\033[0;0m".format(spaces, argv[av], width))
        letterlist = letterlist.replace(" ", "")
        askletter = askletter.replace(" ", "")
        expert(request, letterlist, askletter)
        print("\033[34;1m{}\033[0;0m".format(width))
        av += 1


if __name__ == "__main__":
    try:
        main(sys.argv[1:])
    except KeyboardInterrupt:
        print("\nVoluntary stop")
        sys.exit(1)