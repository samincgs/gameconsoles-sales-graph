import matplotlib.pyplot as plt

phases = ['Mid 1990s', 'Early 2k', 'Mid 2k', 'Mid 2010s']

# estimated values (not fully accurate)
playstation_sales = [45, 155, 350, 110]
xbox_sales = [25, 80, 85, 50]
nintendo_sales = [150, 190, 255, 320]
pc_sales = [90, 182, 300, 479]

width = 0.2
x_playstation = [ x - width for x in range(len(playstation_sales))]
x_xbox = [ x for x in range(len(xbox_sales))]
x_nintendo = [ x + width for x in range(len(nintendo_sales))]

fig, ax = plt.subplots()

#title
ax.set_title('Game consoles over the years')

# fix y labels
ax.set_ylabel('Total sales (in millions)')



#bar chart
ax.bar(x_playstation, playstation_sales, width, label= 'Playstation', color = 'slateblue') 
ax.bar(x_xbox, xbox_sales, width, label = 'Xbox', color = 'springgreen')
ax.bar(x_nintendo, nintendo_sales, width, label= 'Nintendo', color = 'hotpink')

#plot graph
ax.plot(phases, pc_sales, label = 'PC Sales', color = 'aquamarine')

#add a legend
ax.legend()

plt.show()