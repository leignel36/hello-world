def test_to_roman():
	if to_roman(1)!="I":
		return(False)
	elif to_roman(4)!="IV":
		return(False)
	elif to_roman(10)!="X":
		return(False)
	elif to_roman(50)!="L":
		return(False)
	elif to_roman(100)!="C":
		return(False)
	elif to_roman(500)!="D":
		return(False)
	elif to_roman(1000)!="M":
		return(False)
	
	elif to_roman(0) != "n est hors de l'intervalle discret [1;3999]":
		return(False)
	
	elif to_roman(-5)!="n est hors de l'intervalle discret [1;3999]":
		return(False)
	
	
	else:
		return(True)

class BadArgument(Exception):
	pass

def to_roman(n):
	if n <=0 or n> 3999:
		raise BadArgument("n est hors de l'intervalle discret [1;3999]")

	result =''

	if n//1000 !=0:
		for k in range (1,4):
			if n//1000==k:
				for i in range (1,k+1):
					result += 'M'
	new=n-1000 * (n//1000)

	if new//100 !=0 :
		if new//100==9:
			result += 'CM'
		for k in range (6,9):
			if new//100 == k:
				result += 'D'
				for i in range (1,k-5+1):
					result += 'C'

		if new//100==5:
			result += 'D'
		if new//100==4:
			result += 'CD'
		for k in range (1,4):
			if new//100 == k:
				for i in range (1,k+1):
					result += 'C'
	new=new-100 * (new//100)
	if new//10 !=0:	
		if new//10 ==9:
			result += 'XC'
		for k in range (6,9):
			if new//10 == k:
				result += 'L'
				for i in range (1,k-5+1):
					result += 'X'
		if  new//10==5:
			result += 'L'
		for k in range (1,4):
			if new//100 == k:
				for i in range (1,k+1):
					result += 'X'

	
	if new % 10 !=0:
		if new % 10 ==9:
			result += 'IX'
		for k in range (6,9):
			if new % 10 ==k:
				result += 'V'
				for i in range (1,k-5+1):
					result += 'I'
		if new % 10 ==5:
			result += 'V'
		for k in range (1,4):
			if new % 10 ==k:
				for i in range (1,k+1):
					result += 'I'
	return (result)



print(to_roman(45))
	
