import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.dates as mdates

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
	fig = plt.figure(figsize=(10, 4))

	ax = fig.add_subplot()
	ax.plot(df["x"], df["y"])
	ax.plot(df3["x"], df3["y"])
	
	#ax.set_xticks(df3["x"])
	ax.set_xticklabels(df3["x"],rotation=45, ha='right')

	
	#ax.xaxis.set_major_locator( mdates.AutoDateLocator(minticks=4,maxticks=6) )
	ax.set_xlim(pd.to_datetime(["2023/12/23 00:00:00", "2023/12/23 00:10:00"]))
	
	formatter = mdates.DateFormatter("%H:%M:%S")
	ax.xaxis.set_major_formatter(formatter)

	ax.set(
		title='日経平均株価',
		ylabel='株価(円)'
	)
	labels = ["A社"]
	ax.legend(labels,title='凡例')

	plt.show()

#https://www.yutaka-note.com/entry/matplotlib_time_axis
if __name__=='__main__':
	intro()


