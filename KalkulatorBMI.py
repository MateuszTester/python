masa = int(input("Podaj swoją wagę w kg: "))
wzrost = float(input("Podaj swój wzrost w m: "))

BMI = round(masa/(wzrost**2), 2)
print("Twoje BMI wynosi: " + str(BMI))

if BMI < 16:
    print("Jesteś wygłodzony")
elif BMI >= 16 and BMI <= 16.99:
    print("Jesteś wychudzony")
elif BMI >= 17 and BMI <= 18.49:
    print("Masz niedowagę")
elif BMI >= 18.5 and BMI <= 24.99:
    print("Wartość prawidłowa")
elif BMI >= 25 and BMI <= 29.99:
    print("Masz nadwagę")
elif BMI >= 30 and BMI <= 34.99:
    print("Masz I stopień otyłości")
elif BMI >= 35 and BMI <= 39.99:
    print("Masz II stopień otyłości")
else:
    print("Masz otyłość skrajną")