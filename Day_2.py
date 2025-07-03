name = "Dev" 
age = 20

def Authenticity(age):
	if age == 20:
		return "authentic"
	else: 
		return "unauthentic"

for i in range(1,4):
	print(f"Check {i}: {Authenticity(age)}")

