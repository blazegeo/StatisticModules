#!/usr/bin/env python
# coding: utf-8

# In[ ]:



def LargeStandsTic_Version1(x: float, u: float, n: int):
    from scipy.stats import norm #will use for figure 12.2 cumulative normal probability
    #giving me the observed significance
    import math
    # x is sample statistic
    #u is the sample mean = population mean
    # o is the standard deviation (population if none available uses sample)
    #n is the sample size
    difference = x - u
    if n >= 30:
        n = math.sqrt(n)
        # exception block to catch any errors
        try:
            o = float(input("Enter the population standard deviation, if none enter the sample standard deviation: ")
                     )
            teststatistic = difference / (o / n)
            print("This is the test statistic: ",teststatistic) 
            #this is to solve out whether the null hypothesis should be accepted or rejected for me
            tail = input("Enter which tailed test this is from right, left and two: ")
            alpha = float(input("What is the level of significance(in decimals)?: "))
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
                if teststatistic > 0: #if z is postive for a two-tailed test
                    cnp = 2 * (1 - norm.cdf(teststatistic))
                    print("The observed significance is: ", cnp)
                    if cnp <= alpha:
                        return "The null hypothesis is rejected"
                    else:
                        return "The null hypothesis is accepted"
                else: #if z is negative for a two-tailed test
                    cnp = 2 * (norm.cdf(teststatistic))
                    print("The observed significance is: ", cnp)
                    if cnp <= alpha:
                        return "The null hypothesis is rejected"
                    else:
                        return "The null hypothesis is accepted"
            else:
                return "You mispelled the test type"    
        except UnboundLocalError:
            print("Sample size too small to enter standard deviation for this test")
        except ValueError:
            print(" You either entered a blank or mispelled something")      
    #will stop the whole function is the sample size is less than 30
    else:
        return "This sample size is too small for large sample hypothesis tests"
    


# In[ ]:


def StandsTic(x: float, u: float, n: int):
    import scipy.stats as stats
    from scipy.stats import t # used for student's t-distribution
    from scipy.stats import norm #will use for figure 12.2 cumulative normal probability
    #giving me the observed significance
    import math
    # x is sample statistic
    #u is the sample mean = population mean
    # o is the standard deviation (population if none available uses sample)
    #n is the sample size
    difference = x - u
#Large Sample size hypothesis testing concerning a single population mean
    if n >= 30:
        n = math.sqrt(n)
        o = float(input("Enter the population standard deviation, if none enter the sample standard deviation: "))
        teststatistic = difference / (o / n)
        print("This is the test statistic: ",teststatistic)
#Small sample size hypothesis testing concerning a single population mean
    else:
        o = input("Enter the population standard deviation, if none enter the sample standard deviation: ")
        if o != "":
            o = float(o)
            n = math.sqrt(n)
            teststatistic = difference / (o / n)
            print("This is the test statistic: ",teststatistic)         
        #else:
        #    q = float(input("Enter the level of significance(in decimals): "))
        #    s = stats.t.ppf(q, n-1) #t-distribution at degrees of freedom (n-1)
        #    n = math.sqrt(n) #square root the n after so the supplied value is still correct
        #    teststatistic = difference / (s / n)
        #    print("This is the test statistic: ",teststatistic)
    
#This is to solve out whether the null hypothesis should be accepted or rejected for me
    try:    
        tail = input("Enter which tailed test this is from right, left and two: ")
        alpha = float(input("What is the level of significance(in decimals)?: "))
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
            if teststatistic > 0: #if z is postive for a two-tailed test
                cnp = 2 * (1 - norm.cdf(teststatistic))
                print("The observed significance is: ", cnp)
                if cnp <= alpha:
                    return "The null hypothesis is rejected"
                else:
                    return "The null hypothesis is accepted"
            else: #if z is negative for a two-tailed test
                cnp = 2 * (norm.cdf(teststatistic))
                print("The observed significance is: ", cnp)
                if cnp <= alpha:
                    return "The null hypothesis is rejected"
                else:
                    return "The null hypothesis is accepted"
        else:
            return "You mispelled the test type"    
    except ValueError:
        print(" You either entered a blank or mispelled something")      
  


# In[ ]:


def LargeStandsTic(n:int):
    ## This is for Large Sample Hypothesis Tests 
    import math
    import scipy.stats as stats
    from scipy.stats import norm #will use for figure 12.2 cumulative normal probability
    #Checking if the interval is between [0,1] for being called a large sample
    
    p = float(input("What is the population proportion?: "))
    smallinterval = p - 3 * (math.sqrt(p * (1 - p) / n))
    largeinterval = p + 3 * (math.sqrt(p * (1 - p) / n))
    
    if smallinterval > 0 and largeinterval < 1:
        p_0 = float(input("What is the specific number between 0 and 1 that the null hypothesis is based on? : "))
        q_0 = (1 - p_0)
        teststatistic = (p - p_0) / math.sqrt((p_0 * q_0) / n)
        print("This is the test statistic: ", teststatistic)
        #Doing the p-value test
        try:    
            tail = input("Enter which tailed test this is from right, left and two: ")
            alpha = float(input("What is the level of significance(in decimals)?: "))
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
                if teststatistic > 0: #if z is postive for a two-tailed test
                    cnp = 2 * (1 - norm.cdf(teststatistic))
                    print("The observed significance is: ", cnp)
                    if cnp <= alpha:
                        return "The null hypothesis is rejected"
                    else:
                        return "The null hypothesis is accepted"
                else: #if z is negative for a two-tailed test
                    cnp = 2 * (norm.cdf(teststatistic))
                    print("The observed significance is: ", cnp)
                    if cnp <= alpha:
                        return "The null hypothesis is rejected"
                    else:
                        return "The null hypothesis is accepted"
            else:
                return "You mispelled the test type"    
        except ValueError:
            print(" You either entered a blank or mispelled something")   
    else:
        question = input("This isn't a Large Sample, do you want to use the small sample hypothesis test? (Y/N): ")
        if question == "Y":
            x = float(input("What is the sample value?"))
            u = float(input("What is the sample mean?"))
            return StandStic(x,u,n)


# In[ ]:


def ConfInterval(sample1:float,sample2:float):
    import statistics #for the mean function
    import scipy.stats #For getting the critical value such as Figure 12.3 Critical Values of T
    import math #For the sqaure root function
    n1 = int(input("What is the size of population 1?: "))
    s1 = float(input("What is the sample/population standard deviation of population 1?: "))
    n2 = int(input("What is the size of population 2?: "))
    s2 = float(input("What is the sample/population standard deviation of population 2?: "))
    if (n1 >= 30 and n2 >= 30): # Makes sure the sample sizes are both greater than or equal to 30
        confidence = (float(input("What is the level of confidence(in decimals)?: ")))
        z = scipy.stats.norm.ppf((1 - confidence) / 2)
        sum = math.sqrt((( s1 ** 2 ) / n1 ) + (( s2 ** 2 ) / n2 ))
        try:
            if range(sample1) != 1: #if the sample is a list it will get the mean for me
                x1 = statistics.mean(sample1)
            elif range(sample2) != 1:
                x2 =  statistics.mean(sample2)
        except TypeError:#catching the float typeerror by converting to lists then assigning to a variable
            #turning sample1 float into a list
            sample1list = []
            sample1list.append(sample1)
            sample1 = sample1list
            x1 = sample1[0]
            #turining sample2 float into a list then assigning to a variable
            sample2list = []
            sample2list.append(sample2)
            sample2 = sample2list
            x2 = sample2[0]
        meanrange = x1 - x2
        interval = z * sum
        alpha = (1 - confidence)*100
        print("We are",confidence*100,"% confident that the true answer that lies within the confidence interval at","%.2f" %alpha,"%", "is","%.2f" %meanrange,"plus or minus","%.2f" %interval)
    else:
        print("These two sample's size must both be greater than or equal to 30")


# In[ ]:


def LargIndeConfInterval(sample1:float,sample2:float):
    import statistics #for the mean function
    import scipy.stats #For getting the critical value such as Figure 12.3 Critical Values of T
    import math #For the sqaure root function
    from scipy.stats import norm #will use for figure 12.2 cumulative normal probability
    n1 = int(input("What is the size of population 1?: "))
    s1 = float(input("What is the sample/population standard deviation of population 1?: "))
    n2 = int(input("What is the size of population 2?: "))
    s2 = float(input("What is the sample/population standard deviation of population 2?: "))
    if (n1 >= 30 and n2 >= 30): # Makes sure the sample sizes are both greater than or equal to 30
        alpha = (float(input("What is the level of significance(in decimals)?: ")))
        z = scipy.stats.norm.ppf((1 - alpha) / 2)
        sum = math.sqrt((( s1 ** 2 ) / n1 ) + (( s2 ** 2 ) / n2 ))
        try:
            if range(sample1) != 1: #if the sample is a list it will get the mean for me
                x1 = statistics.mean(sample1)
            elif range(sample2) != 1:
                x2 =  statistics.mean(sample2)
        except TypeError:#catching the float typeerror by converting to lists then assigning to a variable
            #turning sample1 float into a list
            sample1list = []
            sample1list.append(sample1)
            sample1 = sample1list
            x1 = sample1[0]
            #turining sample2 float into a list then assigning to a variable
            sample2list = []
            sample2list.append(sample2)
            sample2 = sample2list
            x2 = sample2[0]
        meanrange = x1 - x2
        interval = z * sum
        confidence = (1 - alpha)*100
        print("We are",alpha*100,"% confident that the true answer that lies within the confidence interval at","%.2f" %confidence,"%", "is","%.2f" %meanrange,"plus or minus","%.2f" %interval)
    else: #for smaller sample sizes
        alpha = (float(input("What is the level of confidence(in decimals)?: ")))
        df = n1 + n2 - 2
        t = scipy.stats.t.ppf(q = ((1 - alpha)/2) , df = df) #gets the t critical value, scipy stats are very useful
        pooledsv = (((n1 - 1) * (s1 ** 2)) + ((n2 - 1) * (s2 ** 2))) / df # pooled sample variance
        sum = math.sqrt(pooledsv * ((1 / n1) + (1 / n2)))
        try:
            if range(sample1) != 1: #if the sample is a list it will get the mean for me
                x1 = statistics.mean(sample1)
            elif range(sample2) != 1:
                x2 =  statistics.mean(sample2)
        except TypeError:#catching the float typeerror by converting to lists then assigning to a variable
            #turning sample1 float into a list
            sample1list = []
            sample1list.append(sample1)
            sample1 = sample1list
            x1 = sample1[0]
            #turining sample2 float into a list then assigning to a variable
            sample2list = []
            sample2list.append(sample2)
            sample2 = sample2list
            x2 = sample2[0]
        meanrange = x1 - x2
        interval = t * sum
        confidence = (1 - alpha)*100
        print("We are",alpha*100,"% confident that the true answer that lies within the confidence interval at","%.2f" %confidence,"%", "is","%.2f" %meanrange,"plus or minus","%.2f" %interval)
       
#The Hypothesis Test for difference between mean    
    D_0 = float(input("What is the number deduced from the statement of the situation?: "))
    teststatistic = (meanrange - D_0) / sum #same as the equation above
    print("This is the test statistic: ", teststatistic)
#Doing the p-value test
    try:    
        tail = input("Enter which tailed test this is from right, left and two: ")
        alpha = float(input("What is the level of significance(in decimals)?: "))
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
            if teststatistic > 0: #if z is postive for a two-tailed test
                cnp = 2 * (1 - norm.cdf(teststatistic))
                print("The observed significance is: ", cnp)
                if cnp <= alpha:
                    return "The null hypothesis is rejected"
                else:
                    return "The null hypothesis is accepted"
            else: #if z is negative for a two-tailed test
                cnp = 2 * (norm.cdf(teststatistic))
                print("The observed significance is: ", cnp)
                if cnp <= alpha:
                    return "The null hypothesis is rejected"
                else:
                    return "The null hypothesis is accepted"
        else:
            return "You mispelled the test type"    
    except ValueError:
        print(" You either entered a blank or mispelled something")   


# In[ ]:


#Updated for Small, Independent Samples
def ConfInterval(sample1:float,sample2:float):
    import statistics #for the mean function
    import scipy.stats #For getting the critical value such as Figure 12.3 Critical Values of T
    import math #For the sqaure root function
    n1 = int(input("What is the size of population 1?: "))
    s1 = float(input("What is the sample/population standard deviation of population 1?: "))
    n2 = int(input("What is the size of population 2?: "))
    s2 = float(input("What is the sample/population standard deviation of population 2?: "))
    if (n1 >= 30 and n2 >= 30): # Makes sure the sample sizes are both greater than or equal to 30
        alpha = (float(input("What is the level of confidence(in decimals)?: ")))
        z = scipy.stats.norm.ppf((1 - alpha) / 2)
        sum = math.sqrt((( s1 ** 2 ) / n1 ) + (( s2 ** 2 ) / n2 ))
        try:
            if range(sample1) != 1: #if the sample is a list it will get the mean for me
                x1 = statistics.mean(sample1)
            elif range(sample2) != 1:
                x2 =  statistics.mean(sample2)
        except TypeError:#catching the float typeerror by converting to lists then assigning to a variable
            #turning sample1 float into a list
            sample1list = []
            sample1list.append(sample1)
            sample1 = sample1list
            x1 = sample1[0]
            #turining sample2 float into a list then assigning to a variable
            sample2list = []
            sample2list.append(sample2)
            sample2 = sample2list
            x2 = sample2[0]
        meanrange = x1 - x2
        interval = z * sum
        confidence = (1 - alpha)*100
        print("We are",alpha*100,"% confident that the true answer that lies within the confidence interval at","%.2f" %confidence,"%", "is","%.2f" %meanrange,"plus or minus","%.2f" %interval)
    else: #for smaller sample sizes
        alpha = (float(input("What is the level of confidence(in decimals)?: ")))
        df = n1 + n2 - 2
        t = scipy.stats.t.ppf(q = ((1 - alpha)/2) , df = df) #gets the t critical value, scipy stats are very useful
        pooledsv = (((n1 - 1) * (s1 ** 2)) + ((n2 - 1) * (s2 ** 2))) / df # pooled sample variance
        sum = math.sqrt(pooledsv * ((1 / n1) + (1 / n2)))
        try:
            if range(sample1) != 1: #if the sample is a list it will get the mean for me
                x1 = statistics.mean(sample1)
            elif range(sample2) != 1:
                x2 =  statistics.mean(sample2)
        except TypeError:#catching the float typeerror by converting to lists then assigning to a variable
            #turning sample1 float into a list
            sample1list = []
            sample1list.append(sample1)
            sample1 = sample1list
            x1 = sample1[0]
            #turining sample2 float into a list then assigning to a variable
            sample2list = []
            sample2list.append(sample2)
            sample2 = sample2list
            x2 = sample2[0]
        meanrange = x1 - x2
        interval = t * sum
        confidence = (1 - alpha)*100
        print("We are",alpha*100,"% confident that the true answer that lies within the confidence interval at","%.2f" %confidence,"%", "is","%.2f" %meanrange,"plus or minus","%.2f" %interval)


# In[ ]:


def IndeMeanDiffTest(sample1:float,sample2:float):
    import statistics #for the mean function
    import scipy.stats #For getting the critical value such as Figure 12.3 Critical Values of T
    import math #For the sqaure root function
    from scipy.stats import norm #will use for figure 12.2 cumulative normal probability
    n1 = int(input("What is the size of population 1?: "))
    n2 = int(input("What is the size of population 2?: "))
    s1 = float(input("What is the sample/population standard deviation of population 1?: "))
    s2 = float(input("What is the sample/population standard deviation of population 2?: "))
    # For large sample sizes
    if (n1 >= 30 and n2 >= 30): 
        try:
            
            if len(sample1) > 1 and len(sample2) > 1: #if the sample is a list it will get the mean for me
                
                x1 = statistics.mean(sample1)
                x2 = statistics.mean(sample2)
                s1 = statistics.stdev(sample1)
                s2 = statistics.stdev(sample2)
                
        except TypeError:#catching the float typeerror by converting to lists then assigning to a variable
            #turning sample1 float into a list
            sample1list = []
            sample1list.append(sample1)
            sample1 = sample1list
            x1 = sample1[0]
            #turining sample2 float into a list then assigning to a variable
            sample2list = []
            sample2list.append(sample2)
            sample2 = sample2list
            x2 = sample2[0]
            
        alpha = (float(input("What is the level of significance(in decimals)?: ")))
        z = scipy.stats.norm.ppf((1 - alpha) / 2)
        sum = math.sqrt((( s1 ** 2 ) / n1 ) + (( s2 ** 2 ) / n2 ))    
        meanrange = x1 - x2
        interval = z * sum
        confidence = (1 - alpha)*100
        print("We are",alpha*100,"% confident that the true answer that lies within the confidence interval at","%.2f" %confidence,"%", "is","%.2f" %meanrange,"plus or minus","%.2f" %interval)
        
    #For smaller sample sizes   
    else: 
        try:
            
            if len(sample1) > 1 and len(sample2) > 1: #if the sample is a list it will get the mean for me
                
                x1 = statistics.mean(sample1)
                x2 = statistics.mean(sample2)
                s1 = statistics.stdev(sample1)
                s2 = statistics.stdev(sample2)
                
        except TypeError:#catching the float typeerror by converting to lists then assigning to a variable
            #turning sample1 float into a list
            sample1list = []
            sample1list.append(sample1)
            sample1 = sample1list
            x1 = sample1[0]
            #turining sample2 float into a list then assigning to a variable
            sample2list = []
            sample2list.append(sample2)
            sample2 = sample2list
            x2 = sample2[0]
           
        alpha = (float(input("What is the level of confidence(in decimals)?: ")))
        df = n1 + n2 - 2
        t = scipy.stats.t.ppf(q = ((1 - alpha)/2) , df = df) #gets the t critical value, scipy stats are very useful
        pooledsv = (((n1 - 1) * (s1 ** 2)) + ((n2 - 1) * (s2 ** 2))) / df # pooled sample variance
        sum = math.sqrt(pooledsv * ((1 / n1) + (1 / n2)))    
        meanrange = x1 - x2
        interval = t * sum
        confidence = (1 - alpha)*100
        print("We are",alpha*100,"% confident that the true answer that lies within the confidence interval at","%.2f" %confidence,"%", "is","%.2f" %meanrange,"plus or minus","%.2f" %interval)
       
 #The Hypothesis Test for difference between mean    
    D_0 = float(input("What is the number deduced from the statement of the situation?: "))
    teststatistic = (meanrange - D_0) / sum #same as the equation above
    print("This is the test statistic: ", teststatistic)
 #Doing the p-value test
    try:    
        tail = input("Enter which tailed test this is from right, left and two: ")
        alpha = float(input("What is the level of significance(in decimals)?: "))
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
        else:
            return "You mispelled the test type"    
    except ValueError:
        print(" You either entered a blank or mispelled something")   


# In[ ]:


def PairedConfInterval(sample:list):
    import scipy.stats
    import math
    import statistics
    
    mean = statistics.mean(sample)
    s = statistics.stdev(sample)
    
    #counting number of pairs in list
    c = 0
    for x in sample:
        c += 1
    n = c
    
    confidence = (float(input("What is the level of confidence(in decimals)?: ")))
    alpha = 100 * (1 - confidence)
    df = n - 1
    t = scipy.stats.t.ppf(q = ((1 - confidence)/2) , df = df) #gets the t critical value
    interval = t * (s / (math.sqrt(n)))
    print("We are",confidence*100,"% confident that the true answer that lies within the confidence interval at",          "%.2f" %alpha,"%", "is","%.2f" %mean,"plus or minus","%.2f" %interval)
    


# In[ ]:


def PairedMeanDiffTest(sample:list):
    import scipy.stats
    import math
    import statistics
    from scipy.stats import norm
    
    mean = statistics.mean(sample)
    s = statistics.stdev(sample)
    
    #counting number of pairs in list
    c = 0
    for x in sample:
        c += 1
    n = c
    
    confidence = (float(input("What is the level of confidence(in decimals)?: ")))
    alpha = 100 * (1 - confidence)
    df = n - 1
    t = scipy.stats.t.ppf(q = ((1 - confidence)/2) , df = df) #gets the t critical value
    interval = t * (s / (math.sqrt(n)))
    print("We are",confidence*100,"% confident that the true answer that lies within the confidence interval at",          "%.2f" %alpha,"%", "is","%.2f" %mean,"plus or minus","%.2f" %interval)
    
 #The Hypothesis Test for difference between mean    
    D_0 = float(input("What is the number deduced from the statement of the situation?: "))
    teststatistic = (mean - D_0) / (s / math.sqrt(n)) #same as the equation above
    print("This is the test statistic: ", teststatistic)
 #Doing the p-value test
    try:    
        tail = input("Enter which tailed test this is from right, left and two: ")
        alpha = float(input("What is the level of significance(in decimals)?: "))
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
        else:
            return "You mispelled the test type"    
    except ValueError:
        print(" You either entered a blank or mispelled something")   


# In[ ]:


def PairedMeanDiffTest():
    import scipy.stats
    import math
    import statistics
    from scipy.stats import norm
    #if statement to see if point estimate has already been calculated
    line = input("Is the sample data already in its point estimate form?(Y/N): ")
    
    if line == "Y":
        samplestring = input("What is the point estimate for this data? :")
        #turn the string into a list with split method
        #then iterate over each to convert to floats
        #then append to a new list
        samplestring = list(sample.split(","))
        sample = []
        for x in samplestring:
            x = float(x)
            sample.append(x)
        mean = statistics.mean(sample)
        print("This is the mean(d) and point estimate: ","%.2f" %mean)
        s = statistics.stdev(sample)
        print("This is the standard deviation(s): ","%.2f" %s)
        
    elif line == "N":
        samplestring1 = input("What is the first set of sample data?: ")
        samplestring2 = input("What is the second set of sample data?: ")
        #turn the strings into a list with split method, 
        #then iterate over each to convert to floats
        #then append to a new list
        sample1 = []
        sample2 = []
        samplestring1 = list(samplestring1.split(","))
        for x in samplestring1:
            x = float(x)
            sample1.append(x)
        samplestring2 = list(samplestring2.split(","))
        for x in samplestring2:
            x = float(x)
            sample2.append(x)
            
        #uses zip method to subtract two lists    
        sample = list()
        for item1, item2 in zip(sample1, sample2):
            item = item1 - item2
            sample.append(item)
        print("This is the set of differences : ",sample)
        mean = statistics.mean(sample)
        print("This is the mean(d) and point estimate: ", ".2f" %mean)
        s = statistics.stdev(sample)
        print("This is the standard deviation(s): ", ".2f" %s)
        
    #counting number of pairs in list
    c = 0
    for x in sample:
        c += 1
    n = c
    
    #the meat of the confidence interval formula
    confidence = (float(input("What is the level of confidence(in decimals)?: ")))
    alpha = 100 * (1 - confidence)
    df = n - 1
    t = scipy.stats.t.ppf(q = ((1 - confidence)/2) , df = df) #gets the t critical value
    interval = t * (s / (math.sqrt(n)))
    
    #Replacing t with z if the sample is large for confidence interval
    if n >= 30:
        z = scipy.stats.norm.ppf((1 - alpha) / 2)
        interval = z * (s / (math.sqrt(n)))
        
    print("We are",confidence*100,"% confident that the true answer that lies within the confidence interval at",          "%.2f" %alpha,"%", "is","%.2f" %mean,"plus or minus","%.2f" %interval)
    
 #The Hypothesis Test for difference between mean    
    D_0 = float(input("What is the number deduced from the statement of the situation?: "))
    teststatistic = (mean - D_0) / (s / math.sqrt(n)) #same as the equation above   
    print("This is the test statistic: ", ".2f" %teststatistic)
 #Doing the p-value test
    try:    
        tail = input("Enter which tailed test this is from right, left and two: ")
        alpha = float(input("What is the level of significance(in decimals)?: "))
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
        else:
            return "You mispelled the test type"    
    except ValueError:
        print(" You either entered a blank or mispelled something")   


# In[ ]:


def TwoPopProportionsConf(p1:float,p2:float):
    import math
    import scipy.stats as stats
    from scipy.stats import norm #will use for figure 12.2 cumulative normal probability
    
    #Checking if the interval is between [0,1] for being called a large sample
    n1 = (int(input("What is the size of population 1?: ")))
    n2 = (int(input("What is the size of population 2?: ")))
    smallinterval_1 = p1 - 3 * (math.sqrt(p1 * (1 - p1) / n1))
    largeinterval_1 = p1 + 3 * (math.sqrt(p1 * (1 - p1) / n1))
    smallinterval_2 = p2 - 3 * (math.sqrt(p2 * (1 - p2) / n2))
    largeinterval_2 = p2 + 3 * (math.sqrt(p2 * (1 - p2) / n2))
    if smallinterval_1 > 0 and largeinterval_1 < 1 and smallinterval_2 > 0 and largeinterval_2 < 1:
    #the meat of the confidence interval formula
        confidence = (float(input("What is the level of confidence(in decimals)?: ")))
        alpha = (1 - confidence)
        sum = math.sqrt((p1 * (1 - p1) / n1) + (p2 * (1 - p2) / n2))
        z = stats.norm.ppf((alpha) / 2) #gets the z critical value
        interval = z * sum
        proportiondiff = p1 - p2
        print("This is the point estimate: ",proportiondiff)
        print("We are",confidence * 100,"% confident that the true answer that lies within the confidence interval at",
         "%.2f" %(alpha * 100),"%", "is","%.2f" %proportiondiff,"plus or minus","%.2f" %interval)
    else:
        print("Each of the samples is not large so the confidence interval formula will not represent accurately")


# In[ ]:


def TwoPopProportions(p1:float,p2:float):
    import math
    import scipy.stats as stats
    from scipy.stats import norm #will use for figure 12.2 cumulative normal probability
    
#Checking if the interval is between [0,1] for being called a large sample
    n1 = (int(input("What is the size of population 1?: ")))
    n2 = (int(input("What is the size of population 2?: ")))
    smallinterval_1 = p1 - 3 * (math.sqrt(p1 * (1 - p1) / n1))
    largeinterval_1 = p1 + 3 * (math.sqrt(p1 * (1 - p1) / n1))
    smallinterval_2 = p2 - 3 * (math.sqrt(p2 * (1 - p2) / n2))
    largeinterval_2 = p2 + 3 * (math.sqrt(p2 * (1 - p2) / n2))
    if smallinterval_1 > 0 and largeinterval_1 < 1 and smallinterval_2 > 0 and largeinterval_2 < 1:
#the meat of the confidence interval formula
        confidence = (float(input("What is the level of confidence(in decimals)?: ")))
        alpha = (1 - confidence)
        sum = math.sqrt((p1 * (1 - p1) / n1) + (p2 * (1 - p2) / n2))
        z = stats.norm.ppf((alpha) / 2) #gets the z critical value
        interval = z * sum
        proportiondiff = p1 - p2
        print("This is the point estimate: ","%.2f" %proportiondiff)
        print("We are",confidence * 100,"% confident that the true answer that lies within the confidence interval at",
         "%.2f" %(alpha * 100),"%", "is","%.2f" %proportiondiff,"plus or minus","%.2f" %interval)
        
#The Hypothesis Test for difference between mean    
        D_0 = float(input("What is the number deduced from the statement of the situation?: "))
        teststatistic = (proportiondiff - D_0) / sum  #same as the equation above   
        print("This is the test statistic: ", "%.2f" %teststatistic)
#Doing the p-value test
        try:    
            tail = input("Enter which tailed test this is from right, left and two: ")
            alpha = float(input("What is the level of significance(in decimals)?: "))
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
            else:
                return "You mispelled the test type"    
        except ValueError:
            print(" You either entered a blank or mispelled something")   
    else:
        print("Each of the samples is not large so the confidence interval formula will not represent accurately")


# In[ ]:


def MinSampleSize(E: float):
    import scipy.stats as stats
    from scipy.stats import norm #will use for figure 12.2 cumulative normal probability
    import math # used for the ceil() function which rounds up
    line = input("What type of sample is this from Independent, Paired or Proportion?: ")
    confidence = float(input("What is the level of confidence(in decimals)?: "))
    alpha = 1 - confidence
    z = stats.norm.ppf(alpha/2)
    if line == "Independent":
        s_1 = float(input("What is the standard deviation of population 1?: "))
        s_2 = float(input("What is the standard deviation of population 2?: "))
        n = ((z ** 2) * ((s_1 ** 2) + (s_2 ** 2))) / (E ** 2)
    elif line == "Paired":
        s = float(input("What is the standard deviation of the population?: "))
        n = ((z ** 2) * (s ** 2)) / (E ** 2)
    elif line == "Proportion":
        value = input("Is prior knowledge about the proportions available?(Yes/No): ")
        if value == "Yes" or value == "Y":
            p_1 = float(input("What is the proportion of population 1?: "))
            p_2 = float(input("What is the proportion of population 2?: "))
            n = ((z ** 2) * (p_1 * (1 - p_1) + p_2 * (1 - p_2))) / (E ** 2)
            # uses the most conservative estimate
        if value == "No" or value == "N": 
            p_1 = 0.5
            p_2 = 0.5
            n = ((z ** 2) * (p_1 * (1 - p_1) + p_2 * (1 - p_2))) / (E ** 2)
    n = math.ceil(n) # rounding up to the nearest int
    return n  

