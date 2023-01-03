def solution(genres, plays):
    answer = []
    albums = {}
    rank = {}
    for i in range(len(genres)):
        if genres[i] not in albums:
            albums[genres[i]] = [(plays[i], i)]
            rank[genres[i]] = plays[i]
        else:
            albums[genres[i]].append((plays[i], i))
            rank[genres[i]] += plays[i]
    rank = sorted(rank, key=lambda x:rank[x], reverse=True)
    for item in rank:
        tmp = sorted(albums[item], key=lambda x:(x[0],-x[1]), reverse=True)
        for i in range(2):
            answer.append(tmp[i][1])
            if len(albums[item]) < 2:
                break
    return answer