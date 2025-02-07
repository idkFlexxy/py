##import pandas as pd
#import matplotlib.pyplot as plt
#data=pd.read_csv("D:\data.csv")

#plt.plot(data["Months"], data["Total profit"], linestyle="dotted", marker = "o", color="blue", linewidth=4, label="Total Profit")
#plt.xlabel("Months")
#plt.ylabel("Total Profit")
#plt.legend(loc="lower right")
#plt.title("Total Profit per Month")
#plt.grid(True)
#plt.show()
import pandas as pd # type: ignore
import matplotlib.pyplot as plt # type: ignore

# Load the data into a pandas DataFrame (CSV format assumed)
data = {
    "Months": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    "Pen": [2500, 2630, 2140, 3400, 3600, 2760, 2980, 3700, 3540, 1990, 2340, 2900],
    "Book": [1500, 1200, 1340, 1130, 1740, 1555, 1120, 1400, 1780, 1890, 2100, 1760],
    "Marker": [5200, 5100, 4550, 5870, 4560, 4890, 4780, 5860, 6100, 8300, 7300, 7400],
    "Chair": [9200, 6100, 9550, 8870, 7760, 7490, 8980, 9960, 8100, 10300, 13300, 14400],
    "Table": [1200, 2100, 3550, 1870, 1560, 1890, 1780, 2860, 2100, 2300, 2400, 1800],
    "Pen stand": [1500, 1200, 1340, 1130, 1740, 1555, 1120, 1400, 1780, 1890, 2100, 1760],
    "Total units": [21100, 18330, 22470, 22270, 20960, 20140, 29550, 36140, 23400, 26670, 41280, 30020],
    "Total profit": [211000, 183300, 224700, 222700, 209600, 201400, 295500, 361400, 234000, 266700, 412800, 300200],
}

# OR 
# data = pd.read_csv('path/to/your/csvfile.csv')

df = pd.DataFrame(data)

# a. Total profit line plot line graph
plt.figure(figsize=(10, 6))
plt.plot(df["Months"], df["Total profit"], linestyle="dotted", marker = "o", color="blue", linewidth=4, label="Total Profit")
plt.xlabel("Months")
plt.ylabel("Total Profit")
plt.legend(loc="lower right")
plt.title("Total Profit per Month")
plt.grid(True)
plt.show()
