
""""
To test your solution run the following in the terminal: 
    python autograder.py -p entropy
"""
import numpy as np

def entropy(alpha):
    left, right = 0, 0.5
    epsilon = 1e-6  
    max_iterations = int(np.log2((right - left) / epsilon)) + 1  
    for _ in range(max_iterations):
        mid = (left + right) / 2

        
        if mid == 0 or mid == 1:
            h_mid = 0
        else:
            h_mid = -mid * np.log2(mid) - (1 - mid) * np.log2(1 - mid)

        if h_mid < alpha:
            left = mid
        else:
            right = mid

    
    return (left + right) / 2

#################   DO NOT CHANGE BELOW ###########################

INPUT_NAME = 'datasets/entropy/entropy.in'
OUTPUT_NAME = 'datasets/entropy/entropy_sol.out'

def run_code():
    f = open(INPUT_NAME, 'r')
    fout = open(OUTPUT_NAME, 'w')
    
    n_tests = int(f.readline())
    for i in range(n_tests):
        alpha = float(f.readline())
        p_str = entropy(alpha)
        fout.write(str(p_str) + '\n')
    f.close()
    fout.close()




