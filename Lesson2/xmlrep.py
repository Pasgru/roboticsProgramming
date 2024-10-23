import xml.etree.ElementTree as ET
import sys

def report(fn):
    for t in ET.parse(fn).getroot().iter('test'):
        s = t.findall("status")[-1]
        res = s.get("status") + ' ' + t.get("name")
        if s.get("status") == "FAIL": res = res + ' -- ' + s.text
        print(res)

if __name__ == '__main__': report(sys.argv[1])