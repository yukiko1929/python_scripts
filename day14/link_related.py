import re

def get_link(patt, filename):
    link_list = []
    cpa = re.compile(patt)
    with open(filename) as fobj:
        for lines in fobj:
            ma = cpa.search(lines)
            if  ma:
                mag = ma.group()
                link_list.append(mag)
    return link_list

if __name__ == '__main__':
    # patt = 'http://.*\.jpg'
    patt = r'http://.*\.jpg'
    # patt1 = r'http://[.\w/-]+\.(jpg|png|jpeg|gif)'
    filena = '/mnt/webcontent'
    result = get_link(patt, filena)
    print(result)