import numpy as np

def z_score_normalize(data, threshold = 1.0):
    """Assigned to Aysha: Normalizes and removes outliers."""
    print("\nZ-score Normalizer function called.\n")
    
    # TODO: Implemented logic
    

    np.set_printoptions(legacy = '1.25') #added this so the data prints without np.float64. referenced stackOverflow
    
    #implementing my assigned algorithm now:
    str_checker = False
    for i in range(0, len(data)):
        if (isinstance(data[i], str) == True): #referenced geeksforgeeks
            str_checker = True
    if(len(data) == 0):
        print("Dataset needs at least one data value. This is empty.\n")
        clean_list = data
    elif(str_checker == True):
        print("List cannot contain any strings. This contains a string.\n")
        clean_list = data #maybe I should be returning the list without the string?
    elif(len(set(data)) == 1): #referenced geeksforgeeks
        print("all of the elements in the list are the same. Standard deviation is 0 and Z-scores DNE.")
        clean_list = data
    else: 
        #accepts negative and duplicate values
        mean_data = np.mean(data)
        sd_data = np.std(data)
        z_score = (data[0:len(data)] - mean_data)/sd_data
        
        clean_list = [] #the list where we store the "cleaned" values (no outliers)
        for i in range(0, len(z_score)):
            if z_score[i] < threshold:
                #only adding the values into the cleaned list that are less than the threshold
                clean_list.append(z_score[i])
    print('\n')
    return (clean_list) #this is the cleaned list that we are returning
    #pass

    
def impute_missing_values(data):
    """Assigned to Priyanshu: Replaces None, "", and "NA" with the mean."""
    print("Impute missing value function called")
    # TODO: Implement logic
    print("Impute Missing Values function called")

    MissingValues = [None, "", "NA"] #Created Group for all possible missing values
    NumberValues = []
    
    #Below is the for loop to go over each values in the List and looks for whether it has any missingvalue or not.
    #Also then we convert Non-missing values to String and make sure whether this has valid numbers and if yes then we store it and if not then we display error to user. 
    for i in data:
        if i in MissingValues:
            pass
        else:
            AllStrings = str(i) #referenced from W3schools to convert into string
            Number = True
            for ch in AllStrings:
                if ch not in "0123456789":
                    Number = False
            
            if Number == True:
                NumberValues.append(AllStrings)
            else:
                print("The element from a string is no valid number, please check the values")
                    
                return data
    
    
    #This returns 0 for the same length of missing values if whole list is missing data. 
    if len(NumberValues) == 0:
        return [0] * len(data)
    
    #Below code it loks for all the missing entry and then we determine previous value and next value to calculate average and add it in the list. 
    for p in range(len(data)):
        if data[p] in MissingValues:
            
            #Added for loop to keep looking for PreviousValue until its found. 
            PreviousValue = None
            for k in range(p - 1, -1, -1):
                if data[k] not in MissingValues:
                    PreviousValue = data[k]
                    break
            
            #Added for loop to keep looking for NextValue until its found.
            NextValue = None
            for j in range(p + 1, len(data)):
                if data[j] not in MissingValues:
                    NextValue = data[j]
                    break
            
            #Incase if NextValue is blank then basically for loop begins and look for the value from the start to end of list. 
            if NextValue in MissingValues:
                for l in range(0,p):
                    if data[l] not in MissingValues:
                        NextValue = data[l]
                        break

            if NextValue is not None and PreviousValue is not None:
                Avg = ((PreviousValue + NextValue) / 2)
                if Avg.is_integer(): #Referenced from StackOverflow and Google AI Overview upon search
                    Avg = int(Avg)
            elif PreviousValue is not None:
                Avg = PreviousValue
            else:
                Avg = NextValue
            for value in range(p, len(data)):
                if data[value] not in MissingValues:
                    break
                data[value] = Avg
                
    
    return data
    pass

def min_max_scale(data):
    """Assigned to Glenn: Scales values to the range ."""
    print("First revision on a feature branch.")
    # TODO: Implement logic
    pass
