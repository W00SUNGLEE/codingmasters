import sys
import heapq

n, m = map(int, sys.stdin.readline().split())

customer = list()
out = list()

for _ in range(m):
    in_time_string, out_time_string = sys.stdin.readline().split()
    in_time_list = list(map(int, in_time_string.split(":")))
    out_time_list = list(map(int, out_time_string.split(":")))

    in_time = in_time_list[0]  * 60 * 60 + in_time_list[1]  * 60 + in_time_list[2]
    out_time = out_time_list[0] * 60 * 60 + out_time_list[1] * 60 + out_time_list[2]

    heapq.heappush(customer, [in_time, out_time])

in_time, out_time = heapq.heappop(customer)
heapq.heappush(out, out_time)

answer = 1
count = 1

for _ in range(1, m):
    in_time, out_time = heapq.heappop(customer)

    if len(out) == 0:
        heapq.heappush(out, out_time)
        answer += 1
        count += 1

    else:
        if in_time < out[0]:
            if count < n:
                heapq.heappush(out, out_time)
                answer += 1
                count += 1
            else:
                continue

        else:
            while in_time >= out[0]:
                heapq.heappop(out)
                count -= 1

                if len(out) == 0:
                    break

            heapq.heappush(out, out_time)
            answer += 1
            count += 1

print(answer)