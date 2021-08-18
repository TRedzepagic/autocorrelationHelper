#!/usr/bin/env python3

print("Python helper program for autocorrelation calculation")

# Two methods of getting timeseries data are provided. Comment the one that you do not need or want to use.

# Method 1: Reading from .xlsx (Excel) file where the timeseries is the 'Sales' column

# import pandas as pd 
# DataF=pd.read_excel("timeseries.xlsx",sheet_name='Sheet1')
# print("Timeseries data: ")
# print("Column headings:")
# print(DataF.columns)
# data = DataF['Sales'].to_numpy().tolist()
# print(data)

# Method 2: Reading from plain text file
data = []
# Open timeseries file and append values to timeseries list, cast lines to float
with open("timeseries.txt") as timeseriesFile:
    for line in timeseriesFile:
        data.append(float(line))
print("Timeseries data:")
print(data)

# Both should result in the same data list.
# First step: Calculate arithmetic mean (average)
average = sum(data) / len(data)
print("Arithmetic mean (average) = " + str(average))
print("----------------------------------------------")

numerator = 0
secondOrderNumerator = 0
denominator = 0
for t in range(len(data)):
    # Formulae start from 1, while program calculates indexing from 0
    print("----------------------------------------------")
    print("Iteration ==> " + str(t+1))
    print("Time series element ==> " + str(data[t]))
    print("----------------------------------------------")

    if t == 0:
        # In the first iteration, we only calculate the denominator
        print("Only calculating initial denominator...")
        denominator = (data[t] - average) ** 2
        print(denominator)

    else:
        print("First order calculation step: " + "(" + str(data[t]) + " - " + str(average) + ") * (" + str(
            data[t - 1]) + " - " + str(average) + ")")

        # Calculating first order numerator for this iteration, then adding it to the total numerator
        numeratorIteration = (data[t] - average) * (data[t - 1] - average)
        numerator += numeratorIteration

        # Calculating denominator iteration for both orders (same formula), then adding it to the total denominator
        denominatorIteration = (data[t] - average) ** 2
        denominator += denominatorIteration

        # For the second order autocorrelation numerator we skip t = 1 (second iteration),
        # since it starts from t = 2 (third iteration).
        if t != 1:
            print("Second order calculation step: " + "(" + str(data[t]) + " - " + str(average) + ") * (" + str(
                data[t - 2]) + " - " + str(average) + ")")
            secondOrderNumeratorIteration = (data[t] - average) * (data[t - 2] - average)
            secondOrderNumerator += secondOrderNumeratorIteration

# Calculating first and second order autocorrelation coefficients
firstOrderAutoCorrelation = numerator / denominator
secondOrderAutoCorrelation = secondOrderNumerator / denominator

print("----------------------------------------------")
print("First order autocorrelation coefficient = " + str(firstOrderAutoCorrelation))
print("Second order autocorrelation coefficient = " + str(secondOrderAutoCorrelation))
