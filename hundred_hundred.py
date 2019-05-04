def get_mount():
    osu = []
    mesu = []
    kodoti = []
    for x in range(100):
        for y in range(100):
            for z in range(100):
                if 5 * x + 3 * y + 1/3 * z == 100 and x + y + z == 100:
                    osu.append(x)
                    mesu.append(y)
                    kodoti.append(z)
                    return osu, mesu, kodoti

if __name__ == '__main__':
    print(get_mount())


