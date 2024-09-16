#Return from the Centre for a single rupee for the South States
from matplotlib import pyplot as plt
States = ["Karnataka", "Tamil Nadu", "Telangana", "Andhra Pradesh", "Kerala", "Rajasthan", "Uttar Pradesh", "Bihar"]
Returns = [0.15, 0.29, 0.43, 0.49, 0.57, 1.33, 2.73, 7.06]
plt.bar(States, Returns, label="Returns from Centre", color="c")
plt.legend()
plt.title("Returns from Centre")
plt.ylabel("Returns")
plt.xlabel("States")
plt.show()
