# Write a program that will iteratively update and
# predict based on the location measurements 
# and inferred motions shown below. 

def update(mean1, var1, mean2, var2):
    new_mean = float(var2 * mean1 + var1 * mean2) / (var1 + var2)
    new_var = 1./(1./var1 + 1./var2)
    return [new_mean, new_var]

def predict(mean1, var1, mean2, var2):
    new_mean = mean1 + mean2
    new_var = var1 + var2
    return [new_mean, new_var]

measurements = [5., 6., 7., 9., 10.]
motion = [1., 1., 2., 1., 1.]
measurement_sig = 4.
motion_sig = 2.
mu = 0.
sig = 10000.

#Please print out ONLY the final values of the mean
#and the variance in a list [mu, sig]. 

# Insert code here
for i in range(len(measurements)):
    [mu, sig] = update(mu, sig, measurements[i], measurement_sig)
    # print("update: ", [mu, sig])
    [mu, sig] = predict(mu, sig, motion[i], motion_sig)
    # print("predict: ", [mu, sig])

# Output
# ('update: ', [4.998000799680128, 3.9984006397441023])
# ('predict: ', [5.998000799680128, 5.998400639744102])
# ('update: ', [5.999200191953932, 2.399744061425258])
# ('predict: ', [6.999200191953932, 4.399744061425258])
# ('update: ', [6.999619127420922, 2.0951800575117594])
# ('predict: ', [8.999619127420921, 4.09518005751176])
# ('update: ', [8.999811802788143, 2.0235152416216957])
# ('predict: ', [9.999811802788143, 4.023515241621696])
# ('update: ', [9.999906177177365, 2.0058615808441944])
# ('predict: ', [10.999906177177365, 4.005861580844194])

# Final values
print [mu, sig]
# [10.999906177177365, 4.005861580844194]
