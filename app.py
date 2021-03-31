import itertools

list1=[[1,2,3], ["a"], ["a","b","c"], ["pyhton"]]

merged = list(itertools.chain(*list1))

print(merged)