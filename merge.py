def merge_interval(intervals_list):
    """
    This Function merges the overlapping intervals. First the input interval list is flattened to specific bound
    and connected them with integer that identifies if the bound is upper or lower. Sorting operation is performed
    on this list. Items are pushed into stack if they are lower bound and are popped out when upper bound item arrives.
    When the stack is empty merged interval is obtained.

    :param intervals_list: Intervals list whose overlapping intervals has to be merged
    :return: Merged intervals that are overlapping
    """
    if not intervals_list:
        return []
    # list to store items with their bounds
    flat_intervals_list = []
    for interval in intervals_list:
        flat_intervals_list.append((interval[0], 0))
        flat_intervals_list.append((interval[1], 1))
    flat_intervals_list.sort()

    merged_intervals = []
    stack = [flat_intervals_list[0]]
    for i in range(1, len(flat_intervals_list)):
        temp = flat_intervals_list[i]
        if temp[1] == 0:
            # push this to stack as it is lower bound
            stack.append(temp)
        elif temp[1] == 1:
            if stack:
                start_element = stack.pop()
            if len(stack) == 0:
                # merged interval is obtained
                merged_intervals.append([start_element[0], temp[0]])
    return merged_intervals


if __name__ == '__main__':
    interval_list_1 = [[1, 4], [4, 5]]
    interval_list_2 = [[25, 30], [2, 19], [14, 23], [4, 8]]
    # calling function on example 1
    test_1 = merge_interval(interval_list_1)
    # calling function on example 2
    test_2 = merge_interval(interval_list_2)
    print('Merged intervals of {} --->   {} \nMerged intervals of {} --->   {}'.format(interval_list_1,
                                                                                       test_1,
                                                                                       interval_list_2,
                                                                                       test_2))
