import numpy as np

def z_score_normalize(data, threshold = 1.0):
    """Assigned to Aysha: Normalizes and removes outliers."""
    print("z-score normalizer function called")
    
    # Implemented logic
    
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
    
    return (clean_list) #this is the cleaned list that we are returning
    
    #pass
    
def impute_missing_values(data):
    """Assigned to Priyanshu: Replaces None, "", and "NA" with the mean."""
    print("Feat Imputer function called")
    # TODO: Implement logic
    pass

def min_max_scale(data):
    """Assigned to Glenn: Scales values to the range ."""
    # TODO: Implement logic
    pass
