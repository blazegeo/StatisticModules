#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def chisquaredhypothesis(row0: list, row1:list):
    from scipy.stats import norm
    #update to future proof
    row = 3
    column = 2
    # setting up the dimensions to reflect the contingency table
    contingency = [[0 for x in range(row)] for x in range(column)]
# assigning the values to the row
    c = 0
    for x,y in zip(row0,row1):
        contingency[0][c] = x
        contingency[1][c] = y
        c += 1
#assigning the row and column totals to the extra row and column made
    sumrow0 = 0
    sumrow1 = 0
    total = 0
    sumcolumn = []
#Dealing with row totals
    for x,y in zip(contingency[0],contingency[1]):
        sumrow0 += x
        sumrow1 += y
    #contingency[0].extend(sumrow1) decided to not include
    #contingency[1].extend(sumrow2) decided to not include
    print("This is the sum of row 0: ", sumrow0)
    print("This is the sum of row 1: ", sumrow1)
#Dealing with column totals   
    c = 0
    ele = 0
    for x in range(0,column + 1):
        ele = 0
        s = [z[c] for z in contingency]
        while (ele < len(s)):
            total += s[ele]
            ele += 1
        print("This is the sum of column",x,": ",total)
        sumcolumn.append(total)
        c += 1
        ele = 0 # needed or else it won't reset the while loop
        total = 0 # needed or else total dosen't reset when moving columns

    #contingency.append(sumcolumn) decided to not include
    #calculating expected number of observations for each cell
    c = 0
    expected = [[0 for x in range(row)] for x in range(column)]
    for x,y in zip(row0,row1):
        n = sumrow0 + sumrow1 #sample size
        expected[0][c] = (sumrow0 * sumcolumn[c]) / n
        expected[1][c] = (sumrow1 * sumcolumn[c]) / n
        c += 1
    #calculating  the test statistic chi-square
    teststatistic = 0
    for i in range(len(contingency)) : 
        for j in range(len(contingency[i])) :
              teststatistic += (((contingency[i][j] - expected[i][j]) ** 2) / expected[i][j])
    print("This is the test statistic: ", "%.2f" %teststatistic)
    #Doing the p-value test for right-tailed only
    try:
        alpha = (float(input("What is the level of significance(in decimals)?: ")))
        cnp = 1 - norm.cdf(teststatistic)
        print("The observed significance is: ", cnp)
        if cnp <= alpha:
            return "The null hypothesis is rejected"
        else:
            return "The null hypothesis is accepted"
    except ValueError:
        print(" You either entered a blank or mispelled something")   


# In[ ]:


def chisquaredhypothesis(*args):
    import sys #needed for system argument counting
    from scipy.stats import norm #needed for critical value
    unit_x = len(args[0])
    unit_y = len(args) #*args stores all arguments into args as a list
    df = (unit_x - 1) * (unit_y - 1)
    print("The Chi-squared distribution has", "%.2f" %df,"degrees of freedom")
    # setting up the dimensions to reflect the contingency table
    contingency = [[0 for x in range(unit_x)] for x in range(unit_y)]
    
#Assigning the values to the row
    c_1 = 0
    t_1 = 0 
    while t_1 < (unit_y): # number of total arguments
        for x_1 in args[t_1]:
            try:
                x = args[t_1][c_1]
                contingency[t_1][c_1] = x
                c_1 += 1
            except IndexError:
                t_1 += 1 # but go to the next sublist
                c_1 = 0 #go back to the start of a sublist            
    print("These are the contingency core cells: ",contingency)
#Assigning the row and column totals to the extra row and column made
    sumrow = []
    total = 0
    sumcolumn = []
#Dealing with row totals
    c = 0
    for d in range(0,unit_y):
        totalrow = 0
        for x in contingency[c]:
            totalrow += x
        sumrow.append(totalrow)
        print("This is the sum of row", c ,": ",totalrow)
        c += 1
#Dealing with column totals   
    c = 0
    ele = 0
    for x in range(0,unit_x):
        ele = 0
        s = [z[c] for z in contingency]
        while (ele < len(s)):
            total += s[ele]
            ele += 1
        print("This is the sum of column",x,": ",total)
        sumcolumn.append(total)
        c += 1
        ele = 0 # needed or else it won't reset the while loop
        total = 0 # needed or else total dosen't reset when moving columns

#Calculating expected number of observations for each cell
    c = 0
    t = 0
    n = sum(sumrow) #sample size
    print("This is the grand total of the table: ",n)
    expected = [[0 for x in range(unit_x)] for x in range(unit_y)]
        #the argument length is the row amount from how i've made this
    while t < unit_y: # go through each sublist
        for x in args[t]: #go through each element in each sublist
            try:
                expected[t][c] = (sumrow[t] * sumcolumn[c]) / n
                c += 1
            except IndexError:
                c = 0 #go back to the start of a sublist
                t += 1 # but go to the next sublist
    print("These are the expected values: ", expected)
#Calculating  the test statistic chi-square
    teststatistic = 0
    for i in range(len(contingency)) : 
        for j in range(len(contingency[i])) :
              teststatistic += (((contingency[i][j] - expected[i][j]) ** 2) / expected[i][j])
    print("This is the test statistic: ", "%.2f" %teststatistic)
    line = input("Do you want a hypothesis test?(Y/N): ")
    if line == "Y":
        #Doing the p-value test for right-tailed only
            try:
                alpha = (float(input("What is the level of significance(in decimals)?: ")))
                cnp = 1 - norm.cdf(teststatistic)
                print("The observed significance is: ", cnp)
                if cnp <= alpha:
                    return "The null hypothesis is rejected"
                else:
                    return "The null hypothesis is accepted"
            except ValueError:
                print(" You either entered a blank or mispelled something")   


# In[ ]:


def chigoodnessoffithypothesis(*args):
    import sys #needed for system argument counting
    from scipy.stats import norm #needed for critical value
    unit_x = len(args[0])
    unit_y = len(args) #*args stores all arguments into args as a list
    df = (unit_y - 1)
    print("The Chi-squared distribution has", "%.2f" %df,"degrees of freedom")
    # setting up the dimensions to reflect the contingency table
    contingency = [[0 for x in range(unit_x)] for x in range(unit_y)]
    
#Assigning the values to the row
    c_1 = 0
    t_1 = 0 
    while t_1 < (unit_y): # number of total arguments
        for x_1 in args[t_1]:
            try:
                x = args[t_1][c_1]
                contingency[t_1][c_1] = x
                c_1 += 1
            except IndexError:
                t_1 += 1 # but go to the next sublist
                c_1 = 0 #go back to the start of a sublist            
    print("These are the contingency cells: ",contingency)

#Calculating expected number of observations for each cell
    c = unit_x #make it the last in the row
    t = 0
    pos = 1
    n = sum([(s[pos]) for s in contingency])#sample size by adding observed frequncies
    expected = []
        #the argument length is the row amount from how i've made this
    while t < unit_y: # go through each sublist
        try:
            for x in range(0,len(sys.argv)): #go through each element in each sublist
                expectedvalue =  n * contingency[t][c - 2]
                expected.append(expectedvalue)
                t += 1
        except IndexError:
            continue
    print("These are the expected values: ", expected)
#Calculating  the test statistic chi-square
    teststatistic = 0
    for i in range(len(contingency)) : 
        teststatistic += (((contingency[i][c - 1] - expected[i]) ** 2) / expected[i])
    print("This is the chi-squared test statistic: ", "%.2f" %teststatistic)
    line = input("Do you want a hypothesis test?(Y/N): ")
    if line == "Y":
        #Doing the p-value test for right-tailed only
            try:
                alpha = (float(input("What is the level of significance(in decimals)?: ")))
                cnp = 1 - norm.cdf(teststatistic)
                print("The observed significance is: ", cnp)
                if cnp <= alpha:
                    return "The null hypothesis is rejected, the assumed probability distribution for X is not valid"
                else:
                    return "The null hypothesis is accepted, the assumed probability distribution for X is valid"
            except ValueError:
                print(" You either entered a blank or mispelled something")   


# In[ ]:


def Fvalue():
    import scipy.stats as stats
    alpha = float(input("What is the significance level?(in decimals): "))
    dfn = int(input("What is the numerator degrees of freedom?: "))
    dfd = int(input("What is the denominator degrees of freedom?: "))
    teststatistic = stats.f.ppf(1 - alpha,dfn,dfd)
    return str("%.2f" %teststatistic) + " is the value of the F random variable" 


# In[ ]:


def TwoPopVarianceHypTest(var1: float,var2: float):
    import scipy.stats as stats 
    #teststatistic and sample sizes
    teststatistic = var1 / var2
    n1 = int(input("What is the sample size of population 1?: "))
    n2 = int(input("What is the sample size of population 2?: "))
    #Doing the rejection region method
    try:    
        tail = input("Enter which tailed test this is from right, left and two: ")
        alpha = float(input("What is the level of significance(in decimals)?: "))
        if tail == "left":
            dfn = n1 - 1
            dfd = n2 - 1
            F = stats.f.ppf(alpha,dfn,dfd)
            print("This is the test statistic: ","%.2f" %teststatistic)
            print("The critical F value is: ", "%.2f" %F)
            if teststatistic <= F:
                return "The null hypothesis is rejected"
            else:
                return "The null hypothesis is accepted and follows an F-distribution with degrees of freedom df1 = " + str(dfn) + " and  df2 = " + str(dfd)
        elif tail == "right":
            dfn = n1 - 1
            dfd = n2 - 1
            F = stats.f.ppf(1 - alpha,dfn,dfd)
            print("This is the test statistic: ","%.2f" %teststatistic)
            print("The critical F value is: ", "%.2f" %F)
            if teststatistic >= F :
                return "The null hypothesis is rejected"
            else:
                return "The null hypothesis is accepted and follows an F-distribution with degrees of freedom df1 = " + str(dfn) + " and  df2 = " + str(dfd)
                
        elif tail == "two":
            dfn = n1 - 1
            dfd = n2 - 1
            upperF = stats.f.ppf(1 - (1 - alpha/2),dfn,dfd)
            lowerF = stats.f.ppf((1 - alpha) / 2,dfn,dfd)
            print("This is the test statistic: ","%.2f" %teststatistic)
            print("The upper critical F value is: ", "%.2f" %upperF)
            print("The lower critical F value is: ","%.2f" %lowerF)
            if teststatistic >= upperF or teststatistic <= lowerF:
                return "The null hypothesis is rejected"
            else:
                return "The null hypothesis is accepted and follows an F-distribution with degrees of freedom df1 = " + str(dfn) + " and  df2 = " + str(dfd) 
                
        else:
            return "You mispelled the test type"    
    except ValueError:
        print(" You either entered a blank or mispelled something")


# In[ ]:


def psmvtable(*args: list):
    import pandas as pd #for dataframe at the end
    unit_x = 4
    unit_y = len(args) #*args stores all arguments into args as a list
    # setting up the dimensions to reflect the table
    table = [[0 for x in range(unit_x)] for x in range(unit_y)]
    
    #Assigning the values to the table
    t_1 = 0 
    while t_1 < (unit_y): # number of total arguments
        population = t_1
        table[t_1][0] = population
        samplesize = len(args[t_1])    
        table[t_1][1] = samplesize
        samplemean = sum([s for s in args[t_1]]) / samplesize
        table[t_1][2] = samplemean
        samplevariance = sum([((s - samplemean) ** 2) / (samplesize - 1) for s in args[t_1]])
        table[t_1][3] = samplevariance
        t_1 += 1
    df = pd.DataFrame(table,index = [" "," "," "," "] ,columns= ["Population", "Sample Size", "Sample Mean", "Sample Variance"])
    print(table)
    return  df


# In[ ]:


def ANOVA(*args):
    import scipy.stats as stats
    # Combined Sample Size
    combsampsize = sum([(s[1]) for s in args])
    print("This is the combined sample size: ",combsampsize)
    
    #Mean of the combined sample of all n observations
    sumofx = sum([(s[1] * s[2]) for s in args])
    mean = sumofx / combsampsize
    print("This is the mean of the combined samples of all",combsampsize,         "observations: ","%.2f" %mean)
    
    #Mean Square for Treatment
    sumofmeantreatment = sum([s[1] * (s[2] - mean) ** 2 for s in args])
    K = len(args) # number of arguments = population
    MST = sumofmeantreatment / (K - 1)
    print("This is the mean square for treatment: ", "%.2f" %MST)
    
    #Mean Square for Error
    sumoferror = sum([ (s[1] - 1) * s[3]  for s in args])
    MSE = sumoferror / (combsampsize - K)
    print("This is the mean square for error: ", "%.2f" %MSE)
    
    # Hypothesis (F-Value Critical Range) Test
    teststatistic = MST / MSE
    print("This is the test statistic: ", "%.2f" %teststatistic)
    line = input("Do you need a hypothesis test?(Y/N): ")
    if line == "Y":
        alpha = float(input("What is the level of significance?(in decimals): "))
        dfn = K - 1
        dfd = combsampsize - K
        F = stats.f.ppf(1 - alpha,dfn,dfd)
    
        print("The critical F value is: ", "%.2f" %F)
        if teststatistic >= F :
            return "The null hypothesis is rejected"
        else:
            return "The null hypothesis is accepted and follows an F-distribution with degrees of freedom df1 = " + str(dfn) + " and  df2 = " + str(dfd)

