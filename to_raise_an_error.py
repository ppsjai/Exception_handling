# To raise our own exception

heigth = float(input("Enter your height: "))
weight = int(input("Enter your weight: "))

if heigth > 10:
    raise ValueError("Human height is not more han 10feet")

bmi = weight / heigth ** 2
print(bmi)
