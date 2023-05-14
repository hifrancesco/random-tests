### variables ###
full_name = "Erling Haaland"
height = 1.94
predicted_goals = 100
predicted_goals = 1000

print(full_name, height, predicted_goals, sep="\n")


### global vs local variable ###
global_var = "#100DaysOfCode"


def twitter():
    local_var = "CloudFrancesco"
    print("Follow me on Twitter @" + local_var)


twitter()

print(f"I am doing the {global_var} challenge.")


### assiging a variable to other variables ###
footballer = {
    "name": "Lionel Messi",
    "age": 35,
    "details": {
        "street": "Paris Street",
        "city": "Paris",
        "country": "France",
        "club": "PSG"
    },
    "phone_numbers": [
        {
            "type": "home",
            "number": "123456789"
        },
        {
            "type": "work",
            "number": "987654321"
        }
    ]
}

print(footballer["name"])  # Output: Lionel Messi
print(footballer["details"]["club"])  # Output: PSG
print(footballer["phone_numbers"][1]["number"])  # Output: 987654321