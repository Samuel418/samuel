# module mane: main
import read
import purchase
import write

again = "Y"
while again.upper() == "Y":
    a = read.read_file()
    b = purchase.purchase(a)
    write.over_write(a, b)
    again = input("\nAre there any new customers waiting to buy product? ")
print("\nThank you for orders from our company!!")
print("Please check your invoice for your orders details, \nWhich we have created in .txt file format.")
