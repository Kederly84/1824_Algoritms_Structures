# Параллельная обработка

def processors(processor: list, tasks: list):
    proc = {}
    for i in range(processor[0]):
        proc[i] = [0, 0]

    def finder(avail: dict):
        free = proc[0][1]
        free_idx = 0
        for i in range(1, len(avail)):
            if avail[i][1] < free:
                free = avail[i][1]
                free_idx = i
        return free_idx

    for task in tasks:
        worker = finder(proc)
        print(f'{worker} {proc[worker][0]}')

        proc[worker][0] += task
        proc[worker][1] += task


processor = [2, 5]
tasks = [1, 2, 3, 4, 5]
processors(processor, tasks)
print('End Task')
processor_1 = [4, 20]
tasks_1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
processors(processor_1, tasks_1)
print('End Task')
processor_2 = [1, 20]
tasks_2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
processors(processor_2, tasks_2)