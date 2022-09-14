# coding=utf-8
import time
import pandas as pd
from scipy.sparse import lil_matrix
import matplotlib.pyplot as plt


def solution1(n, c, is_debug=False):
    r = n - 1
    cnt = 0
    s = ''
    for i in range(n):
        for j in range(n):
            if j == 0 or j == i or j == r - i or j == r:
                s = str(s + c)
                cnt += 1
            else:
                s = str(s + " ")
        s = s + '\n'
    if is_debug:
        print(cnt)
        print(s[0:-1])


def solution2(n, c, is_debug=False):
    # init the right bound
    r = n - 1
    # fill in the matrix
    mat = lil_matrix((n, n), dtype=bytes)
    for i in range(n):
        mat[i, 0] = bytes(c)
        mat[i, i] = bytes(c)
        mat[i, r] = bytes(c)
        mat[i, r - i] = bytes(c)
    # print it
    if is_debug:
        print(mat.nnz)
        df = pd.DataFrame(mat.toarray())
        print(df)


def get_time_cost(n, c, solution, if_print=False, i=1):
    if n > 1000:
        return 0
    # print(solution.func_name + " timer start")
    t = time.time()
    for tmp in range(i):
        solution(n, c, if_print)
    return time.time() - t
    # print(solution.func_name + " timer end: " + str(time.time() - t) + '\n')


def plot_time_cost(c1, c2):
    fig, ax = plt.subplots()
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.plot(x_axis_range, c1, "r--", label='solution1')
    ax.plot(x_axis_range, c2, "b--", label='solution2')
    plt.plot(x_axis_range, c1, "ro-", x_axis_range, c2, "b^-")
    plt.xlabel('matrix size')
    plt.ylabel('time cost')
    plt.title('compare time cose')
    plt.legend()
    plt.savefig("./output/Exercise1.png")


if __name__ == '__main__':
    # num = 1000
    char = '+'
    interval = 1
    debug = False

    x_axis_range = [1, 2, 5, 10, 20, 50, 100, 200, 500]
    cost1 = []
    cost2 = []
    for num in x_axis_range:
        cost1.append(get_time_cost(num, char, solution1, debug))
        cost2.append(get_time_cost(num, char, solution2, debug))

    plot_time_cost(cost1, cost2)
