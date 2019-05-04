from sys import argv

def transfer(fname):
    trane = fname + '.txt'
    with open(fname,'r') as fobj:
        with open(trane,'w') as trobj:
            # lines = fobj.readline()
            # striped = dict(lines)
            for line in fobj:
                tra_line = line.rstrip() + '\r\n'
                trobj.writelines(tra_line)

transfer(argv[1])