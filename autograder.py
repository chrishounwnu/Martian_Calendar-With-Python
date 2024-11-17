import collections
import numpy as np 
import time 
import argparse 



EXTREMELY_SLOW = 5
parser = argparse.ArgumentParser()
parser.add_argument("-s","--size", default="small")
parser.add_argument("-p","--problem", default="entropy")
args=parser.parse_args()


if args.problem == "entropy":

    from entropy_sol import run_code as entropy 

    t = 1.2
    start_time = time.time()
    entropy()    
    end_time = time.time()

    time_taken = end_time - start_time

    print("Time taken to execute this script was: ", time_taken, "Seconds!" )
    if time_taken > t:
        if time_taken > EXTREMELY_SLOW:
            print("Your code is very very slow!")

        else:
            print("Your code takes more time than the best solution we have! Please improve your solution to make it faster (reduce the big O complexity)!")



    s_list = []

    with open('datasets/entropy/entropy_sol.out','r') as sol:
        for s in sol:
            s_list.append(float(s))

    o_list = []    

    with open("datasets/entropy/entropy.out",'r') as out:
        for o in out:
            o_list.append(float(o))

    assert len(o_list) == len(s_list), "The length of your output file is incorrect!"

    s_array = np.array(s_list)
    o_array = np.array(o_list)

    x = np.isclose(s_array, o_array, atol=1e-6) 

    t_count = np.sum(x)

    perc = t_count/len(x)
    if perc < 1.0:
      print("Your Solution is Correct for Only ", perc*100, "Percent of the Dataset! Improve Your Solution!")
    else:
       print("Your Solution is Correct for the Entropy Problem!")

if args.problem == "aims":
    from aims_sol import run_code as aims 
    if args.size == "small":
        in_name = 'datasets/aims/aims_small.in'
        out_name = "datasets/aims/aims_small.out"
        t_aims = 0.009

    elif args.size == "medium":
        in_name = 'datasets/aims/aims_medium.in'
        out_name = "datasets/aims/aims_medium.out"
        t_aims = 0.02


    elif args.size == "large":
        in_name = 'datasets/aims/aims_large.in'
        out_name = "datasets/aims/aims_large.out"
        t_aims = 0.15


    else:
        print("Invalid Option: You can only run small, medium, or large tests for this problem!")

    start_time = time.time()
    aims(in_name)
    end_time = time.time()
    time_taken = end_time - start_time

    print("Time taken to execute this script was: ", time_taken, "Seconds!" )

    if time_taken > t_aims:
        if time_taken > EXTREMELY_SLOW:
            print("Your code is very very slow!")

        else:
            print("Your code takes more time than the best solution we have! Please improve your solution to make it faster (reduce the big O complexity)!")


    s_list = []

    with open('datasets/aims/aims_sol.out','r') as sol:
        for s in sol:
            l = s.split(' ')
            s_list.append(l)

    o_list = []    

    with open(out_name,'r') as out:
        for o in out:
            l = o.split(' ')
            o_list.append(l)


    assert len(o_list) == len(s_list), "The length of your output file is incorrect!"

    correct = 0
    
    for i,j in zip(o_list, s_list):

        if collections.Counter(i) == collections.Counter(j):
            correct += 1
    if correct/len(o_list) == 1.0:
        print("Your Solution is Correct on the",  args.size ,"Dataset for the AIMS Problem!")
    
    else:
        print("Your Solution Passed Only ", correct/len(o_list)*100, "Percent of the Given Test Cases!" )


if args.problem == "mars":

    from mars_sol import run_code as mars 
    if args.size == "small":
        in_name = 'datasets/mars/martian_small.in'
        out_name = "datasets/mars/martian_small.out"
        t_mars = 0.0001

    elif args.size == "large":
        in_name = 'datasets/mars/martian_large.in'
        out_name = "datasets/mars/martian_large.out"
        t_mars = 0.02

    else:
        print("Invalid Option: You can only run small or large tests for this problem!")

    start_time = time.time()
    mars(in_name)
    end_time = time.time()
    time_taken = end_time - start_time

    print("Time taken to execute this script was: ", time_taken, "Seconds!" )

    if time_taken > t_mars:
        if time_taken > EXTREMELY_SLOW:
            print("Your code is very very slow!")

        else:
            print("Your code takes more time than the best solution we have! Please improve your solution to make it faster (reduce the big O complexity)!")


    s_list = []

    with open('datasets/mars/mars_sol.out','r') as sol:
        for s in sol:
            l = s.split(' ')
            s_list.append(l)

    o_list = []    

    with open(out_name,'r') as out:
        for o in out:
            l = o.split(' ')
            o_list.append(l)


    assert len(o_list) == len(s_list), "The length of your output file is incorrect!"

    correct = 0
    
    for i,j in zip(o_list, s_list):

        if collections.Counter(i) == collections.Counter(j):
            correct += 1
    if correct/len(o_list) == 1.0:
        print("Your Solution is Correct on the",  args.size ,"Dataset for the MARS Problem!")
    
    else:
        print("Your Solution Passed Only ", correct/len(o_list)*100, "Percent of the Given Test Cases!" )

