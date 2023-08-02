from collections import deque

def solution(cacheSize, cities):
    answer = 0
    cache = deque()
    cities = [x.lower() for x in cities]
 
    for x in cities:
        if cacheSize == 0: # 캐시 사이즈가 0인 경우
            return len(cities) * 5

        if len(cache) == 0: # 캐시가 비어있는 경우
            cache.append(x)
            answer += 5

        else: # 캐시가 비어있지 않은 경우
            if x in cache: # 이미 캐시안에 있을 경우
                answer += 1
                if cache[-1] != x: # 접근한 원소를 제일 최근 원소로
                    del cache[cache.index(x)]
                    cache.append(x)


            else: # 캐시안에 없을 경우           
                if len(cache) < cacheSize: # 캐시가 꽉 차지 않았을 경우
                    cache.append(x)
                else: # 캐시가 꽉 찬 경우
                    cache.popleft() 
                    cache.append(x)
                answer += 5

    return answer
