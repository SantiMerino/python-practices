# estrucuturas booleanas y repetitivas
# if, else, elif
is_raining = True
have_umbrella = False

if is_raining and not have_umbrella:
    print("You should stay inside.")
elif is_raining and have_umbrella:
    print("You can go outside, but take your umbrella!")
else:
    print("It's a nice day to go outside.")

is_weekend = True
is_holiday = False

if is_weekend or is_holiday:
    print("You can relax today.")
else:
    print("It's a workday.")

a = 10
b = 3
c = 1

if a > b and b > c:
    print("a is the largest number.")
