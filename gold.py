def helper():
	M = 1000000007
	n = int(input())
	b, h = map(int, input().split())
	l = list(map(int, input().split()))
	pro = (b * h) % M
	stack = [-1]
	maxArea = 0
	i = 0
	totalVolume = (sum(l) * pro) % M
	while i < len(l):
		if stack[-1] == -1 or l[stack[-1]] <= l[i]:
			stack.append(i)
			i += 1

		else:
			curMax = stack.pop()
			temp = i - stack[-1] - 1

			area = (l[curMax] * temp) % M
			maxArea = max(area, maxArea)

	while stack[-1] != -1:
		curMax = stack.pop()
		temp = n - stack[-1] - 1
		area = (l[curMax] * temp) % M
		maxArea = max(area, maxArea)

	# print(totalVolume, maxArea)

	volumeOfLargest = (maxArea * pro) % M
	answer = totalVolume - volumeOfLargest
	print(answer)


helper()
