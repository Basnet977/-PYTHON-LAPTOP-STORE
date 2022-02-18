print("1.Dell (Rs 20,000)  2.Toshiba (Rs 30,00)  3.Mac(Rs 50,000)")
option= int(input("Select any one : "))

dell_price=0
toshiba_price=0
mac_price=0
delivery_price=0
plastic_price=0
bag_price=0
gift_price=0
tax_amt=0
total_qt=0

if option==1:
    qt=int(input("Enter qt : "))
    dell_price+=20000*qt
    total_qt+=qt
elif option==2:
    qt=int(input("Enter qt : "))
    toshiba_price+=30000*qt
    total_qt+=qt
elif option==3:
    qt=int(input("Enter qt : "))
    mac_price+=50000*qt
    total_qt+=qt
else:
    print("invalid option")
    exit()

print("Delivery option: 1.Home(Rs 1,000) 2.Pickup(free)")

dop=int(input("Enter any option: "))

if dop==1:
    delivery_price+=1000

print("1.Plastic(Rs 1,000)  2.Bag(Rs 2,000) 3.Gift box(Rs 5,000)")

pop=int(input("Select any option: "))
if pop==1:
    plastic_price+=1000
elif pop==2:
    bag_price+=2000
elif pop==3:
    gift_price+=5000
else:
    print("invalid option")

print("1.KTM(13%)  2.LTP(free)  3.BKT(free)")

lop= int(input("Enter any option"))
if lop==1:
    tax_amt+=(mac_price+dell_price+toshiba_price)*0.13
total= mac_price+dell_price+toshiba_price
gt_price= total+delivery_price+plastic_price+bag_price+gift_price+tax_amt
print("================bill=============")
print(f"total qt : {total_qt}")
print(f"tax amt : {tax_amt}")
print(f"gt : {gt_price}")

