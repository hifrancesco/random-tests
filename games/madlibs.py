import os

def main():
    os.system("clear")
    # Part 1
    print("=" * 50)
    adj1 = input("Adjective: ").lower().strip()
    noun1 = input("Noun: ").lower().strip()
    verb1 = input("Verb: ").lower().strip()
    animal1 = input("Animal (plural): ").lower().strip()
    food1 = input("Favourite food: ").lower().strip()
    celebrity1 = input("Celebrity's name: ").title().strip()
    country1 = input("Country you do not want to visit: ").title().strip()
    body_part1 = input("Most favourite body part: ").lower().strip()
    # Part 2
    print("=" * 50)
    adj2 = input("Adjective: ").lower().strip()
    noun2 = input("Noun: ").lower().strip()
    verb2 = input("Verb: ").lower().strip()
    animal2 = input("Animal (singular): ").lower().strip()
    food2 = input("Favourite fruit: ").lower().strip()
    celebrity2 = input("Celebrity's name: ").title().strip()
    country2 = input("Country you want to visit: ").title().strip()
    body_part2 = input("Least favourite body part: ").lower().strip()
    madlib1 = f"""
Today, I went to my favourite place called the '{adj1} {noun1}'.
Unlike other places, {celebrity1} delivers your {food1} from {country1} with his {body_part1}. 
They eat and {verb1} like {animal1} and the best thing is a {adj2} computer inside your {body_part2}.
You love to chew a {noun2} with {food2} while you {verb2} in the grass with {celebrity2} and eat a raw {animal2} in {country2}. 
"""
    madlib2 = f"""
On the news, {celebrity1}, while on vacation in {country1} took a selfie of {celebrity2}'s {body_part1}.
At the same time, they {verb1} like lovers inside a {noun1} with a big {food1} chasing them. 
The {adj1} {animal1} in {country2} couldn't help but attack your {adj2} face because you {verb2} their {body_part2}
Why do you love a {noun2} so much to the point you eat the {animal2}'s homemade {food2}?
"""
    print(madlib1)
    print(madlib2)

if __name__ == "__main__":
    main()
