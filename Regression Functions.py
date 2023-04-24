#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def linearplotter():
    import matplotlib.pyplot as plt # used for plotting
    ## Will plot in the form of y = mx + b
    m = float(input("What is the slope?: "))
    b = float(input("What is the y-intercept?: "))
    line = input("What is the x-point?: ")
    #Initializing the lists
    x = []
    y = []
    while line != "":
        xpoint = float(line)
        x.append(xpoint)
        ypoint = (m * xpoint) + b
        y.append(ypoint)
        line = input("What is the next x-point?(Leave blank to stop): ")
    plt.plot(x,y)
    plt.show()


# In[ ]:


def linearcorrelation(x: list,y:list):
    import math
    #counting amount of pairs
    n = len(x)
    #setting up summations
    sum_x = 0
    sum_xsquared = 0
    sum_y = 0
    sum_ysquared = 0
    sum_xy = 0
    for number in x:
        sum_x += number
        sum_xsquared += number ** 2
    for number in y:
        sum_y += number
        sum_ysquared += number ** 2
    for number1,number2 in zip(x,y):
        sum_xy += (number1 * number2)
    #solving for ss variables
    SS_xx = (sum_xsquared) - ((sum_x ** 2) / n)
    SS_xy = (sum_xy) - ((sum_x * sum_y) / n)
    SS_yy = (sum_ysquared) - ((sum_y ** 2) / n)
    #now solving for linear correlation coefficient
    r = SS_xy / (math.sqrt(SS_xx * SS_yy))
    return "%.2f" %r


# In[ ]:


def leastsquares_sse(x:list, y: list):
    import math
    import statistics as stat
    #counting amount of pairs
    n = len(x)
    #setting up variables
    x_avg = stat.mean(x)
    y_avg = stat.mean(y)
    sum_x = 0
    sum_xsquared = 0
    sum_y = 0
    sum_ysquared = 0
    sum_xy = 0
    #for statements to sum up summations
    for number in x:
        sum_x += number
        sum_xsquared += number ** 2
    for number in y:
        sum_y += number
        sum_ysquared += number ** 2
    for number1,number2 in zip(x,y):
        sum_xy += (number1 * number2)
    #solving for ss variables
    SS_xx = (sum_xsquared) - ((sum_x ** 2) / n)
    SS_xy = (sum_xy) - ((sum_x * sum_y) / n)
    SS_yy = (sum_ysquared) - ((sum_y ** 2) / n)
    #now solving for linear correlation coefficient
    r = SS_xy / (math.sqrt(SS_xx * SS_yy))
    print("This is the linear correlation coefficient: ","%.2f" %r)
    #solving for the least squares regression line
    slope = SS_xy / SS_xx
    y_int = y_avg - (slope * x_avg)
    print("The least squares regression equation is: ","y = ","%.2f" %slope,"x"," +","%.2f" %y_int)
    #calculating the goodness of fit / sum of the squared errors
    sse = SS_yy - (slope * SS_xy)
    print("The Sum of the Squared Errors / Goodness of Fit for this line: ","%.2f" %sse)


# In[ ]:


def Regression(x: list,y: list):
    import math # for square root function
    import statistics as stat # for mean function
    import scipy.stats # for z and t crtitical values
    import numpy as np # for the arange function
    from scipy.stats import norm # for the z critical value
    import matplotlib.pyplot as plt # for graphing
    #counting amount of pairs
    n = len(x)
    #setting up variables
    x_avg = stat.mean(x)
    y_avg = stat.mean(y)
    sum_x = 0
    sum_xsquared = 0
    sum_y = 0
    sum_ysquared = 0
    sum_xy = 0
#for statements to sum up summations
    for number in x:
        sum_x += number
        sum_xsquared += number ** 2
    for number in y:
        sum_y += number
        sum_ysquared += number ** 2
    for number1,number2 in zip(x,y):
        sum_xy += (number1 * number2)
#solving for ss variables
    SS_xx = (sum_xsquared) - ((sum_x ** 2) / n)
    SS_xy = (sum_xy) - ((sum_x * sum_y) / n)
    SS_yy = (sum_ysquared) - ((sum_y ** 2) / n)
    #now solving for linear correlation coefficient
    r = SS_xy / (math.sqrt(SS_xx * SS_yy))
    print("This is the linear correlation coefficient: ","%.2f" %r)
#solving for the least squares regression line

    slope = SS_xy / SS_xx
    y_int = y_avg - (slope * x_avg)
    print("The least squares regression equation is: ","y = ","%.2f" %slope,"x"," +","%.2f" %y_int)
    #calculating the goodness of fit / sum of the squared errors
    sse = SS_yy - (slope * SS_xy)
    print("The Sum of the Squared Errors / Goodness of Fit for this line: ","%.2f" %sse)
    
#Finding the coefficient of determination
    
    r_squared = slope * (SS_xy / SS_yy)
    if r_squared >= 0.5:
        print("The coefficient of determination is: ", r_squared,              "and is high in variablilty in y at ", "%.2f" %(r_squared *100),"%")
    else:
        print("The coefficient of determination is: ", r_squared,               "and is low in variability in y at ","%.2f" %(r_squared *100),"%")
        
#Finding the confidence interval for the slope
    line = input("Do you need a confidence interval?(Y/N): ")
    if line == "Y":
        confidence = (float(input("What is the level of confidence(in decimals)?: ")))
        alpha = 1 - confidence
        df = n - 2
        t = scipy.stats.t.ppf(q = (alpha / 2) , df = df)
        # finding the sample standard deviation of errors
        s_e = math.sqrt(sse/ df)
        sum = s_e / math.sqrt(SS_xx)
        interval = t * sum
        print("We are",confidence*100,"% confident that the true answer that lies within the confidence interval at",              "%.2f" %(100 * alpha),"%", "is","%.2f" %slope,"plus or minus","%.2f" %interval)
    
#Graphing the scatter with the line of fit
    line = input("Do you need a graph displayed?(Y/N): ")
    if line == "Y":
        xlabel = input(" What is the x-axis label?: ")
        ylabel = input("What is the y-axis label?: ")
        x_1 = x
        y_1 = y
        plt.scatter(x_1,y_1, label = "data set")
        x_2 = np.arange(min(x_1),max(x_1) + 1) 
        y_2 = (slope * x_2) + y_int
        plt.plot(x_2,y_2, label = "regression line of fit", color = "y")
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.legend()
        plt.show()
#The Hypothesis Test Concerning the Slope of the Population Regrression Line 
    line = input("Do you need a hypothesis test?(Y/N): ")
    if line =="Y":
        B_0 = float(input("What is the number deduced from the statement of the situation?: "))
        teststatistic = (slope - B_0) / sum  #same as the equation above   
        print("This is the test statistic: ", "%.2f" %teststatistic)
    #Doing the p-value test
        try:    
            tail = input("Enter which tailed test this is from right, left and two: ")
            if tail == "left":
                cnp = norm.cdf(teststatistic)
                print("The observed significance is: ", cnp)
                if cnp <= alpha:
                    return "The null hypothesis is rejected"
                else:
                    return "The null hypothesis is accepted"
            elif tail == "right":
                cnp = 1 - norm.cdf(teststatistic)
                print("The observed significance is: ", cnp)
                if cnp <= alpha:
                    return "The null hypothesis is rejected"
                else:
                    return "The null hypothesis is accepted"
            elif tail == "two":
                if teststatistic > 0: #if test statistic is postive for a two-tailed test
                    cnp = 2 * (1 - norm.cdf(teststatistic))
                    print("The observed significance is: ", cnp)
                    if cnp <= alpha:
                        return "The null hypothesis is rejected"
                    else:
                        return "The null hypothesis is accepted"
                else: #if test statistic is negative for a two-tailed test
                    cnp = 2 * (norm.cdf(teststatistic))
                    print("The observed significance is: ", cnp)
                    if cnp <= alpha:
                        return "The null hypothesis is rejected"
                    else:
                        return "The null hypothesis is accepted"
        except ValueError:
            print(" You either entered a blank or mispelled something")   


# In[ ]:


def Regression(x,y):
    import math # for square root function
    import statistics as stat # for mean function
    import scipy.stats # for z and t crtitical values
    import numpy as np # for the arange function
    from scipy.stats import norm # for the z critical value
    import matplotlib.pyplot as plt # for graphing
    #counting amount of pairs
    n = len(x)
    #setting up variables
    x_avg = stat.mean(x)
    y_avg = stat.mean(y)
    sum_x = 0
    sum_xsquared = 0
    sum_y = 0
    sum_ysquared = 0
    sum_xy = 0
#for statements to sum up summations
    for number in x:
        sum_x += number
        sum_xsquared += number ** 2
    for number in y:
        sum_y += number
        sum_ysquared += number ** 2
    for number1,number2 in zip(x,y):
        sum_xy += (number1 * number2)
#solving for ss variables
    SS_xx = (sum_xsquared) - ((sum_x ** 2) / n)
    SS_xy = (sum_xy) - ((sum_x * sum_y) / n)
    SS_yy = (sum_ysquared) - ((sum_y ** 2) / n)
    #now solving for linear correlation coefficient
    r = SS_xy / (math.sqrt(SS_xx * SS_yy))
    print("This is the linear correlation coefficient: ","%.2f" %r)
#solving for the least squares regression line

    slope = SS_xy / SS_xx
    y_int = y_avg - (slope * x_avg)
    print("The least squares regression equation is: ","y = ","%.2f" %slope,"x"," +","%.2f" %y_int)
    #calculating the goodness of fit / sum of the squared errors
    sse = SS_yy - (slope * SS_xy)
    print("The Sum of the Squared Errors / Goodness of Fit for this line: ","%.2f" %sse)
    #adding this here so hypothesis test still has these variables assigned
    df = n - 2
    s_e = math.sqrt(sse / df)
#Finding the coefficient of determination
    
    r_squared = slope * (SS_xy / SS_yy)
    if r_squared >= 0.5:
        print("The coefficient of determination is: ", r_squared,              "and is high in variablilty in y at ", "%.2f" %(r_squared *100),"%")
    else:
        print("The coefficient of determination is: ", r_squared,               "and is low in variability in y at ","%.2f" %(r_squared *100),"%")
        
#Finding the confidence interval for the slope
    line = input("Do you need a confidence interval for the slope?(Y/N): ")
    if line == "Y":
        confidence = (float(input("What is the level of confidence(in decimals)?: ")))
        alpha = 1 - confidence
        df = n - 2
        t = scipy.stats.t.ppf(q = (alpha / 2) , df = df)
        # finding the sample standard deviation of errors
        s_e = math.sqrt(sse / df)
        sum = s_e / math.sqrt(SS_xx)
        interval = t * sum
        print("We are",confidence*100,"% confident that the true answer that lies within the confidence interval at",              "%.2f" %(100 * alpha),"%", "is","%.2f" %slope,"plus or minus","%.2f" %interval)
 
 #Finding the confidence interval for the mean value of y at x = x_p
    yline = input("Do you need a confidence interval for the mean value of y at a certain x?(Y/N): ")
    if yline == "Y":
        confidence = (float(input("What is the level of confidence(in decimals)?: ")))
        alpha = 1 - confidence
        df = n - 2
        t = scipy.stats.t.ppf(q = (alpha / 2) , df = df)
        s_e = math.sqrt(sse/ df)     
        x_p = float(input("What particular value of x is of interest?: "))
        x_ = float(input("What is the closest x value in the range of data rounded up?: "))
        y_2 = (slope * x_p) + y_int
        sum = math.sqrt(( 1 / n ) + ((x_p - x_) ** 2) / SS_xx)
        interval = t * s_e * sum
        print("We are",confidence*100,"% confident that the true answer that lies within the confidence interval at",              "%.2f" %(100 * alpha),"%", "is","%.2f" %y_2,"plus or minus","%.2f" %interval)
        
 #Finding the prediction interval for an individual new value of y at x = x_p
    line = input("Do you need a prediction interval for an individual new value of y at a certain x?(Y/N): ")
    if line == "Y" and yline == "Y":
        sum = math.sqrt(1 + ( 1 / n ) + ((x_p - x_) ** 2) / SS_xx)
        interval = t * s_e * sum
        print("We are",confidence*100,"% confident that the true answer that lies within the prediction interval at",              "%.2f" %(100 * alpha),"%", "is","%.2f" %y_2,"plus or minus","%.2f" %interval)
    if line == "Y" and yline == "N":
        confidence = (float(input("What is the level of confidence(in decimals)?: ")))
        alpha = 1 - confidence
        df = n - 2
        t = scipy.stats.t.ppf(q = (alpha / 2) , df = df)
        s_e = math.sqrt(sse/ df)
        x_p = float(input("What particular value of x is of interest?: "))
        x_ = float(input("What is the closest x value in the range of data rounded up?: "))
        y_2 = (slope * x_p) + y_int
        sum = math.sqrt(1 + ( 1 / n ) + ((x_p - x_) ** 2) / SS_xx)
        interval = t * s_e * sum
        print("We are",confidence*100,"% confident that the true answer that lies within the prediction interval at",              "%.2f" %(100 * alpha),"%", "is","%.2f" %y_2,"plus or minus","%.2f" %interval)
        
#Graphing the scatter with the line of fit
    line = input("Do you need a graph displayed?(Y/N): ")
    if line == "Y":
        xlabel = input(" What is the x-axis label?: ")
        ylabel = input("What is the y-axis label?: ")
        x_1 = x
        y_1 = y
        plt.scatter(x_1,y_1, label = "data set")
        x_2 = np.arange(min(x_1),max(x_1) + 1) 
        y_2 = (slope * x_2) + y_int
        plt.plot(x_2,y_2, label = "regression line of fit", color = "y")
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.legend()
        plt.show()
        
#The Hypothesis Test Concerning the Slope of the Population Regrression Line 
    line = input("Do you need a hypothesis test?(Y/N): ")
    if line =="Y":
        B_0 = float(input("What is the number deduced from the statement of the situation?: "))
        sum = s_e / math.sqrt(SS_xx)
        teststatistic = (slope - B_0) / sum  #same as the equation above   
        print("This is the test statistic: ", "%.2f" %teststatistic)
    #Doing the p-value test
        try:
            alpha = (float(input("What is the level of significance(in decimals)?: ")))
            tail = input("Enter which tailed test this is from right, left and two: ")
            if tail == "left":
                cnp = norm.cdf(teststatistic)
                print("The observed significance is: ", cnp)
                if cnp <= alpha:
                    return "The null hypothesis is rejected"
                else:
                    return "The null hypothesis is accepted"
            elif tail == "right":
                cnp = 1 - norm.cdf(teststatistic)
                print("The observed significance is: ", cnp)
                if cnp <= alpha:
                    return "The null hypothesis is rejected"
                else:
                    return "The null hypothesis is accepted"
            elif tail == "two":
                if teststatistic > 0: #if test statistic is postive for a two-tailed test
                    cnp = 2 * (1 - norm.cdf(teststatistic))
                    print("The observed significance is: ", cnp)
                    if cnp <= alpha:
                        return "The null hypothesis is rejected"
                    else:
                        return "The null hypothesis is accepted"
                else: #if test statistic is negative for a two-tailed test
                    cnp = 2 * (norm.cdf(teststatistic))
                    print("The observed significance is: ", cnp)
                    if cnp <= alpha:
                        return "The null hypothesis is rejected"
                    else:
                        return "The null hypothesis is accepted"
        except ValueError:
            print(" You either entered a blank or mispelled something")   

