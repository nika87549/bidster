# 1
# user = ("hello world")
# print (user)

# 2
# user = input("ra gqvia?")
# user2 = (f"gamarjoba {user} sasiamovnoa sheni gacnoba")
# print (user2)

# 3
# user = input("dawere winadadeba:")
# user2 = len(user)
# print (user2)

# 4
# user = int(input("pirveli ricxvi:"))
# user2 = int(input("meore ricxvi:"))
# u3= user + user2
# u4= user - user2
# u5= user * user2
# u6= user // user2
# print(f"{user}+{user2}={u3}\n"
#       f"{user}-{user2}={u4}\n"
#       f"{user}*{user2}={u5}\n"
#       f"{user}/{user2}={u6}")

# 5
# user = input("dawere citata: ")
# user2 = input("vin aris am citatis avtori? ")
# print(f"{user2} ambobda '{user}'")

# 6
# user = input("mitxari sheni sayvareli gamonatqvami: ").lower()
# print(user)

# 7
# user =input("dawere teqsti: ").replace(" ","...")
# print (user)

# 8
# user = input("dawer rac ginda:").replace(":)","🙂").replace(":(","🙁")
# print(user)


# 9
# def main():
#     c = 300_000_000  # სინათლის სიჩქარე მეტრ/წმ-ში
#     m = float(input("შეიყვანეთ მასა კილოგრამებში: "))
#     E = m * c**2
#     print(f"გამოთვლილი ენერგია E = {E:.2e} ჯოული")
# main()


# 10
# c= int(input("dawere gradusi celsiusi: "))
# user=(c * 9/5 + 32)
# print(f"{c} gradusi celsiusi aris {user} farengeiti")

# 13
# user = int(input("mitxari sheni asaki: "))
# user2= int(input("mitxari sapensio asaki: "))
# user3= user - user2
# print(f"shen pensiaze gaxval {user3} weliwadshi")

# 14
# user = int(input("mitxari ramdenia sigrdze futebshi: "))
# user2 = int(input("mitxari ramdenia sigane futebshi: "))
# u1 = user * 0.09290304
# u2 = user2 * 0.09290304
# u3 = user * user2
# u4 = u1 * u2
# print(f"otaxis fartobi futebshi aris:{u3}\n"
#       f"otaxis fartobi metrkvadratshi aris:{u4}")


# 15
# u1 = int(input("mitxari adamianebis raodenoba: "))
# u2 = int(input("mitxari ramdeni pizza gaqvs: "))
# u3 = int (input("mitxari tito pizza ramdeni navheria: "))
# u4 = u3 * u2
# u5 = u4 // u1
# u6 = u4 % u1
# print(f"tqven gaqvt {u4} nacheri pizza\n"
#       f"tito adamians ergeba {u5} nacheri\n"
#       f"darchenili nachrebis raodenoba aris {u6}")


# 21
# def main():
#     dollars = dollars_to_float(input("How much was the meal? "))
#     percent = percent_to_float(input("What percentage would you like to tip? "))
#     tip = dollars * percent
#     print(f"Leave ${tip:.2f}")

# def dollars_to_float(d):
#     return float(d.replace("$", ""))

# def percent_to_float(p):
#     return float(p.replace("%", "")) / 100
# main()