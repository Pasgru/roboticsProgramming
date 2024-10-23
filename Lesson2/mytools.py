import sqlite3
import random

def get_new_client_id():
    cur = sqlite3.connect("credit.db").cursor()
    row = cur.execute("select max(id)+1 from client").fetchone()
    return "%d" % row
    
def get_new_client_limit():
    return "%d" % (10000 * random.randint(1,5))

def create_my_file(fn):
    fp = open(fn, 'w')
    fp.close()

def append_my_file(fn, txt):
    fp = open(fn, 'a')
    fp.write(txt + '\n')
    fp.close()