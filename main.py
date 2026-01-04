age = 25
salary = 45000.5
is_active = True
tenure = 10
def churn_risk(tenure):
    if tenure < 12:
        return "High risk"
    else:
        return "Low risk"
print(age, salary, is_active ,churn_risk(tenure))
