d={"a":1, "b":2, "c":3,"d":4}
print d

# for k in d:
# 	print k
# 	print d[k]

d.update({"e":13})
print d

if d.has_key("c"):
	del d["c"]
	print d

d.update({"c":3})
print d

#print d.clear()
print d.items()

f= open("calc.py", 'rU')
for line in f:
	print line

