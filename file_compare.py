from sys import argv

def file_comparison(src1, src2, result):
    with open(src1) as fobj1:
        with open(src2) as fobj2:
            with open(result, 'w') as reobj:
                se1 = set(fobj1)
                se2 = set(fobj2)
                se3 = se2 - se1
                reobj.writelines(se3)

file_comparison(argv[1], argv[2], argv[3])
