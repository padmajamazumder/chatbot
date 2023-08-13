import random
from PyDictionary import PyDictionary
import sgpa
def calculator():

    
    def calculate(expression):
        try:
            result = eval(expression)
            return result
        except:
            return "Error: Invalid input"

    print("Welcome to the Calculator!")

    while True:
        equation = input("Enter an equation (or 'exit' to quit): ")

        if equation.lower() == "exit":
            print("Goodbye!")
            break

        result = calculate(equation)
        print("Result:", result)
        print()
def dictt():
    dictionary = PyDictionary()
    user_input = input("Enter a word: ")
    meaning = dictionary.meaning(user_input)
    if meaning:
        for key, value in meaning.items():
            ans = (f"{key}: {', '.join(value)}")
    else:
        ans = ("No meaning found for the given word.")
    return ans
def ans1():
    ans1 = ["I'm fine ","I am good what about you",'Good',"doing good"]
    return random.choice(ans1)
def greet():
    greetings = ['hello', 'hi', 'hey', 'greetings', 'hola']
    return random.choice(greetings)
def farewell():
    farewells = ['goodbye', 'bye', 'see you', 'take care']
    return random.choice(farewells)
def ans2():
    return "\n\t 1. I can do simple calculations \n\t 2. I can find your marks and percentage of your IA's  \n\t 3. I can calculate your SGPA \n\t 4. I can find the meaning of the word \n\t 5. I can perform simple calculations"
def chatbot_response(user_input):
    user_input = user_input.lower()

    if user_input in ['hello', 'hi', 'hey']:
        return greet()
    elif user_input in ['goodbye', 'bye']:
        return farewell()
    elif user_input in ['How you doing','how are you','fine']:
        return ans1()
    elif user_input in ['what can you do','services','help','list']:
        return ans2()
    elif user_input in ["find the meaning of the word","4","meaning of the word"]:
        return dictt()
    # elif user_input in ["find my sgpa","find my SGPA","3","i need my sgpa","calculate my sgpa"]:
    #     print("Sure, continue with the following steps : \n ")
    #     return  sgpaa() 
    elif user_input in ["calculator","calculate","5","maths","simple calculations"]:
        return calculator()
    else:
        return "I'm sorry, I can't understand your message."
while True:
    user_input = input("You: ")
    response = chatbot_response(user_input)
    print("ChatBot:", response)

    if user_input.lower() == 'bye':
        break




