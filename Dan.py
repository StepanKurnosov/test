import numpy as np
import matplotlib.pyplot as plt
import textwrap

#Прочтение .txt файлов 
data = np.genfromtxt("data.txt",comments="\n")
settings = np.genfromtxt("settings.txt",comments="\n")

#Добавление времени
times = np.linspace(0, settings, len(data))

#Добавление figure
fig = plt.figure()
ax = fig.add_subplot(111)

#Добавление осей
ax.set_xlim([min(times), 1.1*max(times)])
ax.set_ylim([min(data), 1.05*max(data)])

# init title
location = ['center', 'left', 'right']
myTitle = "Анализ данных (Зарядка и разрядка конденсатора)"
ax.set_title("\n".join(textwrap.wrap(myTitle, 80)), loc =location[0])
ax.set_xlabel('Время, с')
ax.set_ylabel('Напряжение, В')

# Построение графиков данных: (стиль линии, ширина линии, цвет) 
plt.plot(times, data,
        linestyle = '-',
        linewidth = 1,
        color = 'red',
        marker='.',
        mew = 2,
        markevery = 10,
        label = 'Напряжение(t)')
plt.legend()

# Добавление сетки  
plt.minorticks_on()      
plt.grid(which='major', color='lightblue', linestyle='-', linewidth=1)
plt.grid(which='minor', color='lightblue', linestyle='--', linewidth=0.5) 

# add a text
plt.text(76, 2.5,"Время зарядки = {: .2f}".format(times[np.argmax(data)]))
plt.text(76, 2,"Время разрядки= {: .2f}".format(settings - times[np.argmax(data)]))

# save plot
plt.savefig('plotted_data.png')
plt.show()