'''
Created on May 24, 2019

@author: Srinivasulu
'''

from datetime import datetime
import matplotlib.pyplot as plt
from datetime import date
import xlrd

def calculateBothAxes(ws):
    totalRows=ws.nrows
    x=[]
    y1=[]
    y2=[]
    for rowNum in range(1,totalRows):
        y1.append(ws.cell(rowNum, 1).value)
    
    for rowNum in range(1,totalRows):
        x.append(rowNum)

    #for rowNum in range(1,totalRows):
    #    x.append(ws.cell(rowNum, 0).value)
    
    for i in range(int(len(y1))):
        y2.append(datetime.strptime(str(y1[i]), '%H:%M:%S.%f').time())
    
    myDay = datetime.strptime((date.today().strftime('%d-%m-%Y')),'%d-%m-%Y').date()
        
    y = [ datetime.combine(myDay, t) for t in y2 ]
        
    return(x,y)

def plotGraph(x,y,legendLabel):
    #plotting the points 
    #plt.plot(x,y, color='green', linestyle='dashed', linewidth = 3, marker='o', markerfacecolor='blue', markersize=12,label=legendLabel)
    plt.plot(x,y,marker='o',linewidth = 0,label=legendLabel)
    #naming the x axis 
    plt.xlabel('Test Cases') 
    #naming the y axis 
    plt.ylabel('Time Taken')
    #giving a title to my graph 
    plt.title('Test Case Time Elapsed') 
    plt.xticks(range(min(x), max(x)+1, 1))
    #function to show the plot
    plt.legend()
    #plt.show() 

def sourceFile(fileName,sheetName):
    wb = xlrd.open_workbook('D:\\ECLIPSE PROJECTS\\TestRepoOne\\PythonExamples\\'+fileName+'.xlsx')
    #ws = wb.sheet_by_index(0)
    ws=wb.sheet_by_name(sheetName)
    x,y=calculateBothAxes(ws)
    #legendLabel=sheetName
    legendLabel=fileName + " - " + sheetName
    plotGraph(x,y,legendLabel)
    
sourceFile("hello","Alpha")

sourceFile("hello","Beta")

sourceFile("hello","Gamma")

plt.show()
