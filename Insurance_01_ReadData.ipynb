
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns
sns.set()




pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)



TARGET_F = "TARGET_CLM_FLAG"
TARGET_A = "TARGET_CLM_AMT"




INFILE = "C:\\NWU422\\DATA\\Insurance.csv"

df = pd.read_csv( INFILE )




'''
Print a transpose of the data so that it will fit on the screen
'''
#print( df.head() )
#print( df.head(3).T )



'''
print the data types and if we wish to change some, this is how to do it.
'''
#print( df.dtypes )
#df["HOMEKIDS"] = df["HOMEKIDS"].astype(float)
#df["TIF"] = df["TIF"].astype(float)
#df.TIF = df.TIF.astype(float)
#print( df.dtypes )







'''
Statistical description of data transposed so that it fits on the screen.
'''
##print( df.describe() )
##print("\n\n\n")
##print( df.describe().T )
##print("\n\n\n")
##x = df.describe().T
##print( x )
##print("\n\n\n")








'''
Find the variables that are objects (strings), integers, and floats. Put their in a list.
'''

#print( df.dtypes )
dt = df.dtypes
#print( dt )

objList = []
intList = []
floatList = []

for i in dt.index :
    #print(" here is i .....", i , " ..... and here is the type", dt[i] )
    if i in ( [ TARGET_F, TARGET_A ] ) : continue
    if dt[i] in (["object"]) : objList.append( i )
    if dt[i] in (["float64"]) : floatList.append( i )
    if dt[i] in (["int64"]) : intList.append( i )


##
##print(" OBJECTS ")
##print(" ------- ")
##for i in objList :
##    print(i)
##
##print(" INTEGER ")
##print(" ------- ")
##for i in intList :
##    print(i)
##
##print(" FLOAT ")
##print(" ----- ")
##for i in floatList :
##    print(i)
##


'''
EXPLORE THE CATEGORICAL / OBJECT VARIABLES
'''


##for i in objList :
##    print(" Class = ", i )
##    g = df.groupby( i )
##    #print( g[i].count() )
##    x = g[ TARGET_F ].mean()
##    print( "Crash Prob", x )
##    print( " ................. ")
##    x = g[ TARGET_A ].mean()
##    print( "Damage Amount", x )
##    print(" ===============\n\n\n ")





##'''
##EXPLORE THE CONTINUOUS VARIABLES
##'''
##print("\n\n")
##print("INTEGER VARIABLES" )
##print("\n")
##for i in intList :
##    print("Variable=",i )
##    g = df.groupby( TARGET_F )
##    x = g[ i ].mean()
##    print( "Crash Prob", x )
##    c = df[i].corr( df[ TARGET_A ] )
##    c = round( 100*c, 1 )
##    print( "Damage Correlation = ", c, "%" )
##    print(" ===============\n\n\n ")




##
##
##print("\n\n")
##print("FLOAT VARIABLES" )
##print("\n")
##for i in floatList :
##    print("Variable=",i )
##    g = df.groupby( TARGET_F )
##    x = g[ i ].mean()
##    print( "Crash Prob", x )
##    c = df[i].corr( df[ TARGET_A ] )
##    c = round( 100*c, 1 )
##    print( "Damage Correlation = ", c, "%" )
##    print(" ===============\n\n\n ")







'''
PIE CHARTS
'''

##for i in objList :
##    print(i)
##    x = df[ i ].value_counts(dropna=False)
##    #print( x )
##    theLabels = x.axes[0].tolist()
##    print( theLabels )
##    theSlices = list(x)
##    print( theSlices ) 
##    plt.pie( theSlices,
##             labels=theLabels,
##             startangle = 90,
##             shadow=True,
##             autopct="%1.1f%%")
##    plt.title("Pie Chart: " + i)
##    plt.show()
##    print("=====\n\n")


x = df["EDUCATION"].value_counts(dropna=False)
theLabels = x.axes[0].tolist()
theSlices = list(x)
explodeList = [ 0 for i in theSlices ]
explodeList[2] = 0.3
print( theLabels )
print( theSlices )
print( explodeList )
plt.pie( theSlices,
         labels=theLabels,
         startangle = 90,
         explode=explodeList,
         shadow=True,
         autopct="%1.1f%%")
plt.title("Pie Chart: " + i)
plt.show()




##for i in intList :
##    plt.hist( df[ i ] )
##    plt.xlabel( i )
##    plt.show()

for i in floatList :
    plt.hist( df[ i ] )
    plt.xlabel( i )
    plt.show()
    
##plt.hist( df[ TARGET_A ] )
##plt.xlabel( "Damages" )
##plt.show()













    











