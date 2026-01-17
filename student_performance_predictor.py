print("Student Performance Predictor (AI Project)")

marks = int(input("Enter student marks (0-100): "))

if marks >= 85:
    print("Predicted Performance: Excellent")
elif marks >= 70:
    print("Predicted Performance: Very Good")
elif marks >= 50:
    print("Predicted Performance: Good")
elif marks >= 35:
    print("Predicted Performance: Average")
else:
    print("Predicted Performance: Needs Improvement")

print("Prediction completed successfully.")
