try:
    import ask_ai
    from nltk.chat.util import Chat, reflections

    pairs = [['my name is (.*)', ["Hello %1, I'm Chatox"]],
             ['(hi|hello|hey)', ['Hello!']],
             ['what is your name?', ['My name is Chatox.']],
             ['how are you?', ['I am doing well, how about you?']],
             ['(.*) your name(.*)', ['My name is Chatox.']],
             ['goodbye|bye|Quit|q|Q', ['Goodbye!', 'See you later.']],
             ['how old are you', ['I am 1 year old']], ['(.*)okay(.*)', ['...']],
             ['okay', ['...']], ["I am(.*)", ["Okay"]], ["I'm(.*)", ["Okay"]],
             ["(.*)", ["Sorry, I dont understand"]],
             ['What are your hobbies', ['Chatting and Talking']]]
    chatox = Chat(pairs, reflections)
    print("Hi! I'm Chatox.")
    while True:
        user_input = input("")
        response = chatox.respond(user_input.lower())
        print(response)
        if "how are you" in user_input.lower():
            user_feeling = input("")
            mood = ask_ai.get_prediction(user_feeling)
            if mood == "happy":
                print("I'm glad you feel that way!")
            elif mood == "sad":
                print("I'm so sorry you feel that way")
                print("You could do something that you like to do to cheer you up!!")
            else:
                print("Sorry, I dont understand")
except:
    pass
