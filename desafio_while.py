def run():
    level = 1
    exp = 0
    print(f'Tu nivel es {level}')
    print(f'XP = {exp}')
    while level < 10:
        exp += 5
        print(f'XP = {exp}')
        if (exp / level) != 10:
            continue
        level += 1  
        print(f'Tu nivel es {level}')  
        if level > 10:
            break


if __name__ == '__main__':
    run()