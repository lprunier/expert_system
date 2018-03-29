import sys

def checkreq(split, len):
    # fonction recursive pour checker si la proposition est vraie
    return 1

def decrypt(request):
    split = str.split(request)
    i = 0
    l = len(split)
    while i < l and split[i] != "=>":
        i += 1
    if checkreq(split, i):
        print("propal ok")
        # turn on les elements apres l'implication
        # retourne la liste des lettres misent a 1
        return "A"
    else:
        print("propal ko")
        return NULL


def main(argv):
    # print("{}".format(argv[0]))
    decrypt(argv[0])


if __name__ == "__main__":
    try:
        main(sys.argv[1:])
    except KeyboardInterrupt:
        print("\nVoluntaru stop")
        sys.exit(1)