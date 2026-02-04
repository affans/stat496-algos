import numpy as np

#fake data set:
fake_data = [2, 3, 4, 5, 6, 7, 1, 6, 90000]

def z_score_normalize(data, threshold=3.0):
    """Assigned to Aysha: Normalizes and removes outliers."""
    str_checker = False 
    for i in range(0, len(data)):
        if (isinstance(data[i], str) == True): #referenced geeksforgeeks
            str_checker = True
    if(len(data) == 0):
        print("Dataset needs at least one data value. This is empty.\n")
        clean_list = []
    elif(str_checker == True):
        print("List cannot contain any strings. This has a string in it.\n")
        clean_list = [] #instead of returning the empty list, return the list without the string? 
    else:
        print("Correct format.\n")
        mean_data = np.mean(data)
        sd_data = np.std(data)
        z_score = (data[0:len(data)] - mean_data)/sd_data
        print("Before cleaning", z_score) #before we clean the list 
        clean_list = [] #the list we are cleaning
        for i in range(0, len(z_score)):
            if z_score[i] < threshold:
                #remove the values from the list 
                clean_list.append(z_score[i])
        print("after cleaning:", clean_list)
    return (clean_list) #this is the cleaned list that we are returning
    #pass

result = z_score_normalize(fake_data, threshold = 3.0)
print(result)

def impute_missing_values(data):
    """Assigned to Priyanshu: Replaces None, "", and "NA" with the mean."""
    # TODO: Implement logic
    pass

def min_max_scale(data):
    """Assigned to Glenn: Scales values to the range ."""
    # TODO: Implement logic
    pass
