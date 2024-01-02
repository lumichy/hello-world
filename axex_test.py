import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.dates as mdates
from matplotlib.backends.backend_pdf import PdfPages

mpl.rc('font', family="MS Gothic")

def intro():
	
	stock1 = pd.read_csv('nikkei2-1.csv', header=None, delimiter=',')
	np_data1 = np.array(stock1)
	x1 = np_data1[:, 0]
	y1 = np_data1[:, 1]

	stock3 = pd.read_csv('nikkei2-3.csv', header=None, delimiter=',')
	np_data3 = np.array(stock3)
	x3 = np_data3[:, 0]
	y3 = np_data3[:, 1]
	
	df = pd.DataFrame({'x':pd.to_datetime(x1, format="%Y/%m/%d %H:%M:%S", errors='coerce'),'y':y1}) 
	df3 = pd.DataFrame({'x':pd.to_datetime(x3, format="%Y/%m/%d %H:%M:%S", errors='coerce'),'y':y3}) 
	print(df)
	print(df3)


	graphCount=2
	graphWidth=10
	graphHigth = 5

	

	for i in range(graphCount):
		fig = plt.figure(figsize=(graphWidth, graphHigth))
		#ax = fig.add_subplot(graphCount,1,i+1)
		ax = fig.add_subplot()
		ax.plot(df["x"], df["y"])
		ax.plot(df3["x"], df3["y"])
		
		#ax.set_xticks(df3["x"])
		#ax.set_xticklabels(df3["x"],rotation=45, ha='right')

		
		#ax.xaxis.set_major_locator( mdates.AutoDateLocator(minticks=4,maxticks=6) )
		ax.set_xlim(pd.to_datetime(["2023/12/23 00:00:00", "2023/12/23 00:10:00"]))
		ax.set_ylim([10000,40000])

		ax.grid()
		ax.minorticks_on()
		
		formatter = mdates.DateFormatter("%H:%M:%S")
		ax.xaxis.set_major_formatter(formatter)

		ax.set(
			title=i,
			ylabel='株価(円)'
		)
		labels = ["A社","B社"]
		ax.legend(labels,title='凡例')

	plt.show()



def intro2():
	from matplotlib.backends.backend_pdf import PdfPages

	x = np.linspace(0,100,1000)
	y = np.sin(x)

	nr = 10
	nc = 1

	for i in range(nr):    
		plt.subplot(nr, nc, i + 1)
		plt.plot(x, y)    

	pdf = PdfPages('longplot.pdf')
	pdf.savefig()

	pdf.close()

#https://www.yutaka-note.com/entry/matplotlib_time_axis
if __name__=='__main__':
	intro()
	


