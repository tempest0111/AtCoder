import itertools
s, k = input().split()
s = sorted(s)
k = int(k)

p_list = sorted(list(set(itertools.permutations(list(s)))))
print("".join(p_list[k-1]))