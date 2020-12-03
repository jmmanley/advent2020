def prod(x,curr=1):
	if not x: return 1
	else: return x[0] * prod(x[1:])
