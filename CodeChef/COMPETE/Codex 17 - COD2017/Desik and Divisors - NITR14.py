def s(n, prime, primesquare, a):
	for i in range(2, n):
		prime[i] = True
	prime[1] = False
	for i in range(n * n + 1):
		primesquare = False
	p = 2
	while p * p <= n:
		if prime[p]:
			for i in range(2*p, n, p):
				prime[i] = False


def main():
	from sys import stdin, stdout
	rl = stdin.readline()
	int1 = int
	T = int1(rl())

	for i in range(T):
		pass


main()
