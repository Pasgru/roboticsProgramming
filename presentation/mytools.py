def create_my_file(fn):
    fp = open(fn, 'w')
    fp.close()

def append_my_file(fn, txt):
    fp = open(fn, 'a')
    fp.write(txt + ';')
    fp.close()