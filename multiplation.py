# Developed By : NIRANJAN KUMAR G S 
# From : INDIA
# Email : niranjan4@outlook.in
# Updated date : 12/sec/2017

def mul_table(n):
	for i in range(1,11):
		print("{0}x{1}={2}".format(n,i,n*i))
if __name__ == "__main__":
	while True:
		#a=float(input("enter number: ")) 		#python3
		a=float(raw_input("enter number: ")) 		#python2
		mul_table(a)
		#b=input('Do you want to continue (y) for yes or (n) for no: ')#python3
		b=raw_input('Do you want to continue (y) for yes or (n) for no: ')#python2
		if b=='n':
			print('-----------Thank You-----------')
			break



