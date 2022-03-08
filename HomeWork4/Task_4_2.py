def package_worker(info: list) -> list:
    buffer_size = info[0][0]
    buffer = []
    result = []

    for i in range(1, len(info)):
        if len(buffer) < buffer_size and len(buffer) != 0:
            result.append(max(buffer[-1], info[i][0]))
            buffer.append(max(buffer[-1], info[i][0]) + info[i][1])
        elif len(buffer) == 0:
            buffer.append(info[i][0] + info[i][1])
            result.append(info[i][0])
        else:
            j = 0
            while j < buffer_size:
                if buffer[0] <= info[i][0]:
                    buffer.pop(0)
                j += 1
            if len(buffer) < buffer_size:
                result.append(max(buffer[-1], info[i][0]))
                buffer.append(max(buffer[-1], info[i][0]) + info[i][1])
            else:
                result.append(-1)

    return result






print(package_worker([[3, 1], [1, 1], [1, 1], [10, 1], [10, 1], [10, 1]]))
