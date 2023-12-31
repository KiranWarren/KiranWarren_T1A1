# Coding Score Calculator

# Initialise objects to be used.
coding_skills_dict = {
    "Python": 1,
    "Ruby": 2,
    "Bash": 4,
    "Git": 8,
    "HTML": 16,
    "TDD": 32,
    "CSS": 64,
    "JavaScript": 128
}
skill_check = "" # String variable to take 'y' or 'n' input from user for each skill.
user_skills = [] # List containing booleans corresponding to each coding skill.
total_score = 0 # Total score of all their skills added together.

# Welcoming splash printed to console.
print("")
print("------------------------------")
print("-----WELCOME TO ACME CORP-----")
print("------------------------------")
print("")
print("Coding Skill Calculator")
print("")

# Iterate over all keys in the coding_skills_dict and get user input for each.
for k in coding_skills_dict.keys():
    # Use a while loop in case the user enters an invalid input. It will just ask the question again.
    while skill_check != "y" and skill_check != "n":
        skill_check = input(f"Are you competent with {k}? Enter 'y' or 'n': ")
    # Add skill to the user_skills list as a boolean.
    if skill_check == "y":
        user_skills.append(True)
    else:
        user_skills.append(False)
    # Reset skill_check variable.
    skill_check = ""

# Calculate total skill score. All scores are powers of 2, so we can just use 2^i.
for i in range(len(user_skills)):
    total_score += user_skills[i] * (2 ** i)

# Provide feedback to the user showing their score and potential improvements.
print("")
print(f"Thank you for your input! Your total coding score is {total_score} out of a possible 255.")
print("")

# Offer a list of compentencies based on the users previous inputs.
if total_score < 255:
    print("To improve your score, you could learn the following skills:")
    i = 0
    for k in coding_skills_dict.keys():
        if not user_skills[i]:
            print(f"- {k} would improve your score by {coding_skills_dict[k]}.")
        i += 1

# If the user has already achieved a perfect score, congratulate them and offer no improvements
else:
    print("You have a perfect score. There are no other competencies that would improve your score! Bravo!")

# Let the user know the application has been closed.
print("")
print("Application Closed")