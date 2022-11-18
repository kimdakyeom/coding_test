def solution(bridge_length, weight, truck_weights):
    answer = 0
    queue = [0] * bridge_length
    truck_weights_queue = truck_weights
    while len(queue) != 0:
        answer += 1
        queue.pop(0)
        if truck_weights_queue:
            if sum(queue) + truck_weights_queue[0] <= weight:
                new_truck = truck_weights_queue.pop(0)
                queue.append(new_truck)
            else:
                queue.append(0)
    return answer