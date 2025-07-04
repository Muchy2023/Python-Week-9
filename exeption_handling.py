
try:
    print(x)  # 'x' is not defined yet, triggers NameError
except NameError:
    print("Variable is not defined.")
except Exception:
    print("An exception has occurred.")
else:
    print("The 'try except' is finished.")

x = -1
if x < 0:
    raise Exception("Sorry, no number below zero")

    