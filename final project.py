import random
jokes = [
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "I told my computer I needed a break, and it said 'No problem, I’ll go to sleep.",
    "Why was the JavaScript developer sad? Because they didn’t 'null' their feelings.",
    "Why do Python developers wear glasses? Because they can't C.",
    "I would tell you a joke about UDP, but you might not get it."
]

answer = input("Do you want a tech joke? Type yes or no: ")

if answer == "yes":
    joke = random.choice(jokes)
    print("Here is your joke:")
    print(joke)
elif answer == "no":
    print("Okay, no joke for now.")
else:
    print("Try again")    