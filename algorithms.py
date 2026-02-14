import numpy as np

def z_score_normalize(data, threshold=3.0):
    """Assigned to Aysha: Normalizes and removes outliers."""
    # TODO: Implement logic
    pass

def impute_missing_values(data):
    """Assigned to Priyanshu: Replaces None, "", and "NA" with the mean."""
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
            PreviousValue = data[p - 1]

            NextValue = None
            for j in range(p + 1, len(data)):
                if data[j] not in MissingValues:
                    NextValue = data[j]
                    break

            if NextValue is not None:
                Avg = (PreviousValue + NextValue) / 2
            else:
                Avg = PreviousValue
            for value in range (p,j):
                data[value] = Avg
                
    
    return data
    pass

def min_max_scale(data):
    """Assigned to Glenn: Scales values to the range ."""
    # TODO: Implement logic
    pass
