def solution(order):
    container = []
    idx = 1
    order_idx = 0

    while idx < len(order) + 1:
        container.append(idx)
        while container and container[-1] == order[order_idx]:
            container.pop()
            order_idx += 1
        idx += 1

    return order_idx

