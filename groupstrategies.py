# YOU ONLY HAVE TO SUBMIT FUNCTIONS FOR WHICH
# YOU ARE THE DRIVER IN PAIR PROGRAMMING

import random

# Here are some history variables to test your code on. Feel free to create your own.
hist1 = []
hist2 = [("split","steal")]
hist3 = [("split","split"),("steal","split"),("split","steal"),("split","split"),("steal","split")]
hist4 = [("split","steal"),("steal","steal"),("split","steal"),("steal","split"),("split","split"),("steal","split")]

# Your team's 1st strategy (leave blank if you are not the driver)
# Explanation of Strategy:
# 


# Your team's 2nd strategy (leave blank if you are not the driver)
# Explanation of Strategy: Take advatage if they consistitly split, split most of the time if not.
# 
def USC2(history):
    if len(history) >= 2:
        if history[-1][1] == "split" and history[-2][1] == "split":
            return "steal"
        else:
            return random.choice(['split', 'steal', 'split', 'split', 'split'])
    else:
        return random.choice(['split', 'steal', 'split', 'split', 'split'])
    
for i in range(0,10):
    print(USC2(hist4))

# Your team's 3rd strategy (leave blank if you are not the driver)
# Explanation of Strategy:
# 
