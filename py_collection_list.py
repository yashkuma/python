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
mylist.insert(4,"CA")
print("------Insert------")
print(mylist)
print("------Done!-------\n")

#Delete last item from IN LIST
mylist.pop()
print("------Last item------")
print(mylist)
print("------Deleted!-------\n")


#SWAP items in LIST let take first and last value
#method 1
mylist.append("Temp")
mylist[4]=mylist[0]
mylist[0]=mylist[3]
mylist[3]=mylist[4]
mylist.pop()
print("------Method 1 SWAPING------")
print(mylist)
print("------Done------\n")

#method 2
temp=mylist[0]
mylist[0]=mylist[3]
mylist[3]=temp
print("------Method 2 SWAPING------")
print(mylist)
print("------Done------\n")

#method 3
mylist[0],mylist[3]=mylist[3],mylist[0]
print("------Method 3 SWAPING------")
print(mylist)
print("------Done------\n")

#CLEAR ITEM IN LIST
mylist.clear()
print(mylist)
print("---Cleared the list---\n")

#print list using range function
print(list(range(1,100)))

#print even number
even=0
for i in range(1,100):
    if i%2==0:
        print(i)
print("even number")
        

#-------------------------------LIST END-------------------------------#

#-------------------------------TOUPLE START-------------------------------#
mylist=("Y","K","S")
print("\n-----Just print touble----")
print(mylist)
print("----END---\n")
