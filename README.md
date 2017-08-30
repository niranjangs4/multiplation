# multiplation.py
python multiplation module
def mul_table(n):
	for i in range(1,11):
		print("{0}x{1}={2}".format(n,i,n*i))
if __name__ == "__main__":
	while True:
		a=float(input("enter number: "))
		mul_table(a)
		b=input('Do you want to continue (y) for yes or (n) for no: ')
		if b=='n':
			print('-----------Thank You-----------')
			break
