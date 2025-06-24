import pandas
a=pandas.read_csv(r"C:\Users\HP\Downloads\archive (1).zip") #importing data from kaggle 
print(a)

b=a.sort_values("math score") #sorted in ascending order and store data in b variable 
print(b)

b=a.sort_values(["reading score"],ascending=[False]) #in descending order as ascending is set as false 
print(b)


b=a.sort_values(["math score","reading score","writing score"],ascending=[False,False,False])#Sorting in descending order 
print(b)


#exporting  file to csv
b.to_csv("Output of studensts score.csv")