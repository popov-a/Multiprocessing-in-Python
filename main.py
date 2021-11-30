#https://docs-python.ru/tutorial/mnogopotochnost-python/

#n_proc = multiprocessing.cpu_count()
import multiprocessing as mp
import time

my_p = list()

def my_func_2(i, j):
    global my_p
    my_p.append((i, j))

def my_func(j, n):
    time_start = time.time()
    print(f'Процесс {n} стартанул ...')
    sum = 0
    for i in range(30000000):
        sum += i
    my_func_2(j, n)
    print(f'Процесс {n} закончил. Время работы {time.time() - time_start}')

if __name__ == '__main__':
    # узнаем количество ядер у процессора
    n_proc = mp.cpu_count()
    print(f'Всего {n_proc} ядер')
    for j in range(1, n_proc + 2):
        print(f'\nЗапускаем {j} процессов:')
        p = list()
        for i in range(j):
            p.append(mp.Process(target=my_func, args=(j, i)))
            p[i].start()
        for i in range(j):
            p[i].join()

    print(f'\nДоступ к глобальным переменным {my_p}')