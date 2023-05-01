from time import time


def typing_errors(prompt):
    global input_words
    words = prompt.split()
    error = 0
    for i in range(len(input_words)):
        if i in (0, len(input_words)-1):
            if input_words[i] == words[i]:
                continue
            else:
                error += 1
        else:
            if input_words[i] == words[i]:
                if (input_words[i+1] == words[i+1]) & (input_words[i-1] == words[i-1]):
                    continue
                else:
                    error += 1
            else:
                error += 1
    return error


def typing_speed(prompter):
    global time
    global input_words
    input_words = prompter.split()
    total_words = len(input_words)
    user_speed = (total_words / time)*60
    return user_speed


def time_elapsed(starting_time, ending_time):
    duration = ending_time - starting_time
    return duration


prompt = "Hi, my name is ninetysix, I am a coder."
print("Type this:- '", prompt, "'")
input("press ENTER when you are ready!")

stime = time()
i_prompt = input()
etime = time()

time = round(time_elapsed(stime, etime), 2)
speed = typing_speed(i_prompt)
formatted_speed = "{:.2f}".format(speed)
errors = typing_errors(prompt)

print("Total time elapsed : ", time, "s")
print("Your average typing speed was : ", formatted_speed, "words / minute")
print("With a total of : ", errors, "errors")
