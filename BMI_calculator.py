#The welcome message
print("\t\tHello, Welcome ! \n\t\tCalculate your BMI ")

#Weight
weight = float(input("\nEnter your weight(Kg):"))
#Height
height = float(input("Enter your height(m):"))


#Calculate BMI
height_n = height * height
bmi = weight / height_n

# BMI rounded to 2 decimals.
limited_bmi = round(bmi, 2)
print(f'\nYour BMI is {limited_bmi}kg/m²')

# Weight status and dietary advice
if limited_bmi < 18.5:
    print("\nWeight Status: Underweight")
    print("""
    DIETARY ADVICE:
    * Increase your calorie intake
       - add butter or margarine to your food
       - fry foods such as roast potatoes and chips
       - choose whole milk instead of skimmed or semi-skimmed milk
       """)

elif 18.5 <= limited_bmi <= 24.9:
    print("\nWeight Status: Healthy weight")
    print("""\
        DIETARY ADVICE:
        * Base your meals on higher fiber starchy carbohydrates
        * Eat lots of fruit and vegetables
        * Cut down on saturated fat and sugar
           """)

elif 25 <= limited_bmi <= 29.9:
    print("\nWeight Status: Overweight")
    print("""
        DIETARY ADVICE:
        * Choose minimally processed, whole foods
        * Whole grains (Whole wheat, steel-cut oats, brown rice)
        * Vegetables (a colorful variety - not potatoes)
        * Whole fruits
        * Healthful sources of protein
           """)

else:
    print("\nWeight Status: Obesity")
    print("""
            DIETARY ADVICE:
            * Choose minimally processed, whole foods
            * Whole grains (Whole wheat, steel-cut oats, brown rice)
            * Vegetables (a colorful variety - not potatoes)
            * Whole fruits
            * Healthful sources of protein
               """)

#Calculate the minimum weight for the given height to maintain a healthy BMI.
min_weight = height_n * 18.5
limited_min_weight = round(min_weight, 2)

#Calculate the maximum weight for the given height to maintain a healthy BMI.
max_weight = height_n * 24.9
limited_max_weight = round(max_weight, 2)


print(f"\nThe minimum weight you should have: {limited_min_weight}kg")
print(f"The maximum weight you should have: {limited_max_weight}kg")

print("\n\t\tKeep your BMI between 18.5 and 24.9  \n\t\tHave a nice day!")

# Run the application
