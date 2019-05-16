import matplotlib.pyplot as plt 
  
# x-coordinates of left sides of bars  
  
# heights of bars 
height = [10, 24, 36, 40, 5] 
  
# labels for bars 
tick_label = ['one', 'two', 'three', 'four', 'five'] 
  
# plotting a bar chart 
plt.bar(range(len(tick_label)), height, color = ['red', 'green']) 

plt.xticks(range(len(tick_label)), tick_label, rotation = 90)
# naming the x-axis 
plt.xlabel('x - axis') 
# naming the y-axis 
plt.ylabel('y - axis') 
# plot title 
plt.title('My bar chart!') 
  
# function to show the plot 
plt.show() 
