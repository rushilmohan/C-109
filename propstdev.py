import csv
from os import stat
import pandas as pd
import statistics
import plotly.figure_factory as ff
import plotly.express as px

df = pd.read_csv("StudentsPerformance.csv")

mathlist = df["math score"].tolist()
readinglist = df["reading score"].tolist()

mathmean = statistics.mean(mathlist)
readingmean = statistics.mean(readinglist)

mathmode = statistics.mode(mathlist)
radingmode = statistics.mode(readinglist)

mathmedian = statistics.median(mathlist)
readingmedian = statistics.median(readinglist)

mathx = statistics.stdev(mathlist)
readingx = statistics.stdev(readinglist)


math = ff.create_distplot([mathlist],["Math Score"])
math.show()

math1dstart,math1dend = mathmean - mathx, mathmean + mathx
math2dstart,math2dend = mathmean - 2*mathx, mathmean + 2*mathx
math3dstart,math3dend = mathmean - 3*mathx, mathmean + 3*mathx

input1d = [result for result in mathlist if result > math1dstart and result < math1dend ]
input2d = [result for result in mathlist if result > math2dstart and result < math2dend ]
input3d = [result for result in mathlist if result > math3dstart and result < math3dend ]

print((len(input1d)/(len(mathlist)))*100)
print((len(input2d)/(len(mathlist)))*100)
print((len(input3d)/(len(mathlist)))*100)
