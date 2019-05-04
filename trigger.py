def name_age(name, age):
    if not 0 < age < 120:
        raise ValueError('invalid age')
    print('%s is %s years old' % (name, age))

def age_name(name, age):
    assert 0 < age < 120, 'out of range'
    print('%s is %s years old' % (name, age))


if __name__ == '__main__':
    name_age('yuki', 24)
    age_name('yuki', 225)