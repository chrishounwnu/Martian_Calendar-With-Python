""""
In this problem, you will try your solution on three different datasets: small, medium, and large
To test your solution on each one of them run the following in the terminal,
for small: 
    python autograder.py -p aims -s small

for medium: 
    python autograder.py -p aims -s medium

for large: 
    python autograder.py -p aims -s large

"""

def aims(n, S):
    max_sum = 0
    current_sum = 0

    for char in S:
        if char in 'aims':
            current_sum += 1
        else:
            current_sum -= 1
        if current_sum < 0:
            current_sum = 0
        if current_sum > max_sum:
            max_sum = current_sum

    return max_sum

#################   DO NOT CHANGE BELOW ###########################

def run_code(name):
    fin = open(name, 'r')
    fout = open('datasets/aims/aims_sol.out', 'w')
    n_tests = int(fin.readline())
    for i in range(n_tests):
        n = int(fin.readline())
        S = fin.readline()[:-1]
        assert len(S) == n
        fout.write('%d\n' % aims(n, S))
    fin.close()
    fout.close()
