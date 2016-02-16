

dice={"roy":32 , "wiliam":57 , "sam":86}
print dice

del dice["roy"]
print dice

dice.update({"roy":35})
print dice


#has_key and in
if dice.has_key("roy"):
	del dice["roy"]
print dice

#clear list
dice.clear()

if "sam" in dice:
	del dice["sam"]
print dice	

#update values in dictionary
dice.update({"roy":10 ,"sam":20})
print dice


# get value

print dice.get("sam")
print dice["roy"]


 # key and value()

for key in dice:
	print key

for key in dice.keys():
	print key

for v in dice.values():
	print v

for k in dice:
	print k ,":" ,dice[k]


#  items()

for k,v in dice.items():
	print k, ";", v

	