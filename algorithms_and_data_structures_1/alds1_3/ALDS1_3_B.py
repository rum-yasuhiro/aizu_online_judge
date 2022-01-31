"""
名前 namei と必要な処理時間 timei を持つ n 個のプロセスが順番に一列に並んでいます。
ラウンドロビンスケジューリングと呼ばれる処理方法では、CPU がプロセスを順番に処理します。
各プロセスは最大 q ms（これをクオンタムと呼びます）だけ処理が実行されます。
q ms だけ処理を行っても、まだそのプロセスが完了しなければ、そのプロセスは列の最後尾に移動し、CPU は次のプロセスに割り当てられます。
"""


def roundrobin():
    n, quanta = map(int, input().split())

    queue = []
    for _ in range(n):
        name, t = input().split()

        queue.append((name, int(t)))

    # start processing
    delta_t = 0
    results = [(name, 0) for _ in range(n)]
    while queue:
        name, t = queue.pop(0)
        if t > quanta:
            t = t - quanta
            queue.append((name, t))
            delta_t += quanta
        else:
            delta_t += t
            print(name, delta_t)
