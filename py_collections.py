#List is a collection which is ordered and changeable. Allows duplicate members.
#Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
#Set is a collection which is unordered and unindexed. No duplicate members.
#Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

#-------------------------------LIST START-------------------------------#
#CHANGE IN LIST
mylist=["y","K","S"]
mylist[1]="kumar"
mylist[0]="Yash"
mylist[2]="Srivastava"

print("\n------------Change List Start-----------------")
print(mylist)
print("-------------Change List Start---------------\n")


#LOOP
print("----------Loop Start----------")
for x in mylist:
    print(x)
print("----------Loop End------------\n") # to keep print also in for loop, put print in same indent


 
#ADD IN LIST
mylist.append("India")
print("-----Item Added-----")
print(mylist)
print("-----Done!------\n")



#INSERT at given position IN LIST
mylist.insert(1,"CA")
print("------Insert------")
print(mylist)
print("------Done!-------\n")

#CLEAR ITEM IN LIST
mylist.clear()
print(mylist)
print("---Cleared the list---\n")

#-------------------------------LIST END-------------------------------#

#-------------------------------TOUPLE START-------------------------------#
mylist=("Yash","Kumar","Srivastava")
print("\n-----Just printed touble----")
print(mylist)
print(mylist[1]) #second
print("----END---\n")

#Change item in Touple is not supported, hence below will throw error: TypeError: 'tuple' object does not support item assignment
#mylist[1]="CA"
#print(mylist) # Cannot change value
#print("Errord out, Please ignore this")

#FOR LOOP
print("----------Loop Start----------")
for x in mylist:
    print(x)
print("----------Loop END----------")