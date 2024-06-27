import sys
import heapq

white = []
black = []
same = []


def change():
    while True:
        if len(black) > 15:
            y, x = heapq.heappop(black)
            if not white:
                heapq.heappush(white, (-x, -y))
            elif -x > white[0][0]:
                heapq.heappush(white, (-x, -y))
            continue
        if len(white) > 15:
            x, y = heapq.heappop(white)
            if not black:
                heapq.heappush(black, (-y, -x))
            elif -y > black[0][1]:
                heapq.heappush(black, (-y, -x))
            continue

        break


while True:
    try:
        x, y = map(int, sys.stdin.readline().split())
        if y > x:
            heapq.heappush(black, (y, -x))
        elif x > y:
            heapq.heappush(white, (x, -y))
        else:
            heapq.heappush(same, (x, y))
    except:
        break
change()
while same:
    x, y = heapq.heappop(same)
    if len(black) < 15:
        heapq.heappush(black, (y, -x))
    elif len(white) < 15:
        heapq.heappush(white, (x, -y))
    else:
        if black[0][0] < white[0][0]:
            heapq.heappush(black, (y, -x))
        else:
            heapq.heappush(white, (x, -y))
    change()
ans = 0
for i in range(15):
    ans += black[i][0]
    ans += white[i][0]
print(ans)
