# -*- coding: utf-8 -*-
import random


main_list = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
finish = 0
score = 0


def generate2or4():
    num_list = [2, 2, 2, 4]
    num = random.choice(num_list)
    global main_list
    num0 = 0
    score1 = 0
    for x in main_list:
        score1 += sum(x)
        num0 += x.count(0)
    if num0 == 0:
        global finish
        finish = 1
        print('GAME OVER')
        print('TOTAL SCORE IS %s' % score1)
    else:
        fill_num = random.randrange(1, num0+1)
        n = 0
        for i in range(4):
            for j in range(4):
                if main_list[i][j] == 0:
                    n += 1
                    if n == fill_num:
                        main_list[i][j] = num
                        break
    print('-------------')
    global score
    score = 0
    for y in main_list:
        score += sum(y)
        print(y)
    print('-------------')
    print('Now score is %s' % score)


def action_down():
    global main_list
    for i in range(4):
        for j in range(3, 0, -1):
            for k in range(j):
                if main_list[k+1][i] == 0:
                    main_list[k+1][i] = main_list[k][i]
                    main_list[k][i] = 0
                elif main_list[k+1][i] == main_list[k][i]:
                    main_list[k+1][i] *= 2
                    main_list[k][i] = 0
    return main_list


def action_up():
    global main_list
    for i in range(4):
        for j in range(1, 4):
            for k in range(j, 0, -1):
                if main_list[k-1][i] == 0:
                    main_list[k-1][i] = main_list[k][i]
                    main_list[k][i] = 0
                elif main_list[k-1][i] == main_list[k][i]:
                    main_list[k-1][i] *= 2
                    main_list[k][i] = 0
    return main_list


def action_left():
    global main_list
    for i in range(4):
        for j in range(1, 4):
            for k in range(j, 0, -1):
                if main_list[i][k-1] == 0:
                    main_list[i][k-1] = main_list[i][k]
                    main_list[i][k] = 0
                elif main_list[i][k-1] == main_list[i][k]:
                    main_list[i][k-1] *= 2
                    main_list[i][k] = 0
    return main_list


def action_right():
    global main_list
    for i in range(4):
        for j in range(3, 0, -1):
            for k in range(j):
                if main_list[i][k+1] == 0:
                    main_list[i][k+1] = main_list[i][k]
                    main_list[i][k] = 0
                elif main_list[i][k+1] == main_list[i][k]:
                    main_list[i][k+1] *=2
                    main_list[i][k] = 0
    return main_list


def run():
    global score
    while finish == 0:
        action_code = str(input('Please input the action code:(W, S, A, D) or Q(quit)')).upper()
        if score >= 2048:
            print('You win! Your total scroe is %d' % score)
            break
        if action_code == 'Q':
            break
        if action_code == 'W':
            action_up()
            generate2or4()
        if action_code == 'S':
            action_down()
            generate2or4()
        if action_code == 'A':
            action_left()
            generate2or4()
        if action_code == 'D':
            action_right()
            generate2or4()


if __name__ == '__main__':
    generate2or4()
    run()