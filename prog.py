
while True:
	var=input("enter number:")
	is_prime= True

	for fac in range(2,var):
		if var % fac == 0:
			is_prime = False

	if is_prime == True:
		print "%d is prime number" % var
	else:
		print "not "

