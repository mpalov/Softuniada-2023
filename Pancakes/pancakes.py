def find_best_stuffing(line):
    max_sum = float('-inf')
    curr_sum = 0
    start_idx = 0
    end_idx = 0
    max_start = 0
    max_end = 0

    for i in range(len(line)):
        if curr_sum < 0:
            start_idx = i
            end_idx = i
            curr_sum = 0

        curr_sum += line[i]
        end_idx = i

        if curr_sum > max_sum:
            max_start = start_idx
            max_end = end_idx
            max_sum = curr_sum
        elif curr_sum == max_sum and (end_idx - start_idx) > (max_end - max_start):
            max_start = start_idx
            max_end = end_idx

    return max_sum, max_start, max_end


elements = [int(x) for x in input().split()]
max_sum, max_start, max_end = find_best_stuffing(elements)
print(max_sum, max_start, max_end)
