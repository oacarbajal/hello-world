#These first lines are creating products and price for 4 items

product1_name, product1_price, units = "Coffee", 5.00, 5 
product2_name, product2_price, units2 = "Muffin", 4.00, 4
product3_name, product3_price, units3 = "Doubleshot", 3.00, 3
product4_name, product4_price, units4 = "Water", 2.00, 2 
x = "1"
y = "2"
#tax formula
tax = ((product1_price + 2 * product2_price) *.06)

#calculation for each line
ln1 =(f"{x} {product1_name} at ${units} each: ${product1_price}")
ln2 =(f"{y} {product2_name} at ${units2} each: ${product2_price}")

#Create business name
business_name = "My Coffee and Muffin Shop"

#create top border
print("*"*30) 

#print business info first
print(business_name)

#this will be to input how many items were purchased
string = 'Number of coffees bought?'
print(string)
print(x)
string2 = 'Number of muffins bought?'
print(string2)
print(y)

#print out line between sections
print("*"*30)
print()
#print out line between sections
print("*"*30)

#breakdown of receipt
receipt = "My Coffee and Muffin Shop Receipt"
print(receipt)

#qty and price of products purchased
print(ln1) 
print(ln2)

#this line is to print the total tax
print(f"6% Tax: ${tax}")

#print out line between sections
print("_ "*7)

#total price
total = tax + ((product1_price) + (2 * product2_price))

print(f"Total: ${total}")

#create bottom border
print("*"*30) 

