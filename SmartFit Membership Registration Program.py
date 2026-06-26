### SmartFit Membership Registration Program

print("Welcome to SmartFit! Kindly fill out the form below to choose your membership plan.")

# User input
name = input("Enter your name: ")
age = int(input("Enter your age: "))

# Age-based eligibility check and program recommendation
if age < 18:
    print("You are eligible for the Teen Fitness Program.") 
elif age >= 18 and age <= 40:
    print("You are eligible for the Regular Fitness Program.")
else:
    print("You are eligible for the Senior Wellness Program.")

# Medical condition check
medical_condition = input( "Do you have any pre-existing medical conditions? 'yes' or 'no': ").lower( )
while medical_condition != 'yes' and medical_condition != 'no':
    print("Invalid input. Please enter 'yes' or 'no'.")
    medical_condition = input( "Do you have any pre-existing medical conditions? 'yes' or 'no': ").lower( )
if medical_condition == 'yes' and age >= 40:
    print("Medical clearance is required before joining")
    clearance = input("Do you have medical clearance? 'yes' or 'no': ").lower( )
    while clearance != 'yes' and clearance != 'no':
        print("Invalid input. Please enter 'yes' or 'no'.")
        clearance = input("Do you have medical clearance? 'yes' or 'no': ").lower( )
    if clearance == 'no':
     print("Please try again after getting medical clearance. Thank you for your interest in SmartFit! We hope to see you soon. Have a lovely SmartFit day!")
     exit()
    elif clearance == 'yes':
        print("Provide your medical clearance document to the front desk for verification. You can proceed with the registration.")
elif medical_condition == 'no': 
        print(" You can proceed with the registration.")
elif medical_condition == 'yes' and age < 40:
    print("You can proceed with the registration but please note that you may need to undergo a health screening. If you have a medical clearance document, please submit it at the front desk for verification. You can proceed with the registration.")

## Membership plan

# Dictionary to store membership plans and their prices
membership_plans = {
    "Basic":30.00,
    "Premium": 60.00
}
# Membership plan selection
print("SmartFit offers two membership plans: Basic and Premium")
membership_plan = input("Choose your membership plan: 'Basic', 'Premium' ")
if membership_plan in membership_plans:
    print(f"You have selected the {membership_plan} plan.")
else:
    while membership_plan not in membership_plans:
        print("Invalid membership plan. Please choose 'Basic' or 'Premium'.")
        membership_plan = input("Choose your membership plan: 'Basic', 'Premium' ")
        print(f"You have selected the {membership_plan} plan.")
if membership_plan == 'Basic':
    training = input("Do you want personal training? 'yes' or 'no': ").lower( )
    while training != 'yes' and training != 'no':
        print("Invalid input. Please enter 'yes' or 'no'.")
        training = input("Do you want personal training? 'yes' or 'no': ").lower( )
    if training == 'yes':
        cost = membership_plans[membership_plan] + 15.00
        print(f"{membership_plan} plan with personal training: ${cost:.2f}per month.")
    elif training == 'no':
        print(f"{membership_plan} plan: ${membership_plans[membership_plan]:.2f}per month.")
    
elif membership_plan == 'Premium':
    print(f"{membership_plan} plan: ${membership_plans[membership_plan]:.2f}per month.")

if membership_plan == 'Premium' and age < 30:
    print("You qualify for a youth discount! 10% off your plan.")

if membership_plan == 'Basic' and training == 'no':
    print("Consider upgrading to the Premium plan for more benefits!")

if membership_plan == 'Premium' and medical_condition == 'yes':
    print("We recommend a free consultation before starting.")


## Final confirmation
confirmation = input(f"Thank you {name} for registering with SmartFit! You have selected the {membership_plan} plan. Do you want to confirm your registration? 'yes' or 'no': ").lower( )
if confirmation == 'yes':
    print("Your registration is confirmed! Welcome to SmartFit! Quality fitness and wellness awaits you! Enjoy your journey to a healthier lifestyle! We are excited to have you on board and look forward to helping you achieve your fitness goals. Thank you for choosing SmartFit! Have a SmartFit day!")
else:
 print("Your registration is not confirmed. Please visit us again when you are ready to join SmartFit or re-register. We hope to see you soon! Have a SmartFit day!")