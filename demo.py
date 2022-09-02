from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

def plot():
    
	# the figure that will contain the plot
	fig = Figure(figsize=(5, 5), dpi=100)

	# list of squares
	y = [i**2 for i in range(101)]

	# adding the subplot
	plot1 = fig.add_subplot(111)

	# plotting the graph
	plot1.plot(y)

	# creating the Tkinter canvas
	# containing the Matplotlib figure
	canvas = FigureCanvasTkAgg(fig, master=f1)
	canvas.draw()

	# placing the canvas on the Tkinter window
	canvas.get_tk_widget().pack()

	# creating the Matplotlib toolbar
	toolbar = NavigationToolbar2Tk(canvas, window)
	toolbar.update()

	# placing the toolbar on the Tkinter window
	canvas.get_tk_widget().pack()

window = Tk()
window.title('Plotting in Tkinter')
window.geometry("500x500")

Button(master=window, command=plot, height=2, width=10, text="Plot").pack()

f1 = Frame(window)
f1.pack()

window.mainloop()