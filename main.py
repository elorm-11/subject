print("enter mark obtained in 4 subjects: ")
math = int(input("math :"))
english = int(input("english :"))
science = int(input("science :"))
hindi = int(input("hindi :"))

sum = math+english+science+hindi
print("sum of math,english, and hindi")

perc = (sum/400)*100

print(end="percentage mark = ")
print(perc)