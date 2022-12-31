def solution(cards):
    answer = 0
    ans_len = []
    boxes = {}
    for index, card in enumerate(cards):
        boxes[index+1] = card
    while boxes:
        pos = list(boxes.keys())[0]
        visited = set()
        while pos not in visited:
            visited.add(pos)
            tmp = boxes[pos]
            del boxes[pos]
            pos = tmp
        ans_len.append(len(visited))
    ans_len.sort(reverse=True)
    return ans_len[0] * ans_len[1] if len(ans_len) > 1 else 0