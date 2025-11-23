print("health habit tracker")
sleep_hours=int(input("Hours you slept:"))
water=int(input("liters of water you drank today:"))
protein=int(input("grams of protein you had:"))
screen_time=int(input("Hours you used your phone:"))
walk=int(input("number of steps you walked today:"))
number_of_meals=int(input("number of meals you had in a day:"))
score=0
if sleep_hours>=7:
    score+=30
if water>=8:
    score+=30
if protein>=50:
    score+=30
if screen_time<=3:
    score+=30
if walk>=8000:
    score+=30
if number_of_meals>=3:
    score+=30
print("/nToday's health report")
print("Sleep hours:",sleep_hours,"hours")
print("Water:",water,"liters")
print("Protein:",protein,"grams")
print("Screen time:",screen_time,"hours")
print("Walk:",walk,"steps")
print("Number of meals:",number_of_meals)
print("Health score:",score,"/180")
if score>=120:
    print("excillent")
elif score>=90:
    print("good")
else:
    print("bad")
    