# calculate avg score and student rank
literature_score = float(input("Enter the literature score: "))
math_score = float(input("Enter the math score: "))
english_score = float(input("Enter the english score: "))

avg_score = (literature_score + math_score + english_score) / 3

if (avg_score >= 8 and (math_score >= 8 or literature_score >= 8)
        and all(val >= 6.5 for val in [math_score, literature_score, english_score])):
    print("The student is ranked as Excellent")
elif (avg_score >= 6.5 and (math_score >= 6.5 or literature_score >= 6.5)
        and all(val >= 5 for val in [math_score, literature_score, english_score])):
    print("The student is ranked as Good")
elif (avg_score >= 5 and (math_score >= 5 or literature_score >= 5)
        and all(val >= 3.5 for val in [math_score, literature_score, english_score])):
    print("The student is ranked as Average")
else:
    print("The student is ranked as Poor")