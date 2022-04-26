from hashing_strategies.multiplicative_hashing import HashTableV2
from hashing_strategies.rolling_hashing import HashTableV1

# New test data
runtime_x = "thequickbrownfoxjumpsoverthelazydogforthekingsheartybreakfastofeggstoastandbeans"*10
runtime_y = "ilovethelazydogeatingthefoxsbeans"*10
runtime_k = 4

def rh_runtime_test(x,y,k):
    """
    Calculates the average runtime of a rolling hashing function
    """
    import time
    import random
    run_time = 0 
    run_times_rh = []
    
    #average test number of runtimes
    for test in range(k+1,len(x)-k):
        #vary the length of the input data
        testdata = x[:test]
        #Start the timer
        start_time = time.time()
        #Run the function
        HT = HashTableV1(testdata,y,k)
        HT.rh_get_match()
        #func_name(testdata)
        #Stop the timer
        end_time = time.time()
        #Record values
        run_time += (end_time - start_time)
        run_times_rh.append((run_time))
        
    return run_times_rh

def mh_runtime_test(x,y,k):
    """
    Calculates the average runtime of a multiplicative hashing function
    """
    import time
    import random
    run_time = 0 
    run_times_mh = []
    
    #average test number of runtimes
    for test in range(k+1,len(x)-k):
        #vary the length of the input data
        testdata = x[:test]
        #Start the timer
        start_time = time.time()
        #Run the function
        HT = HashTableV2(testdata,y,k)
        HT.regular_get_match()
        #func_name(testdata)
        #Stop the timer
        end_time = time.time()
        #Record values
        run_time += (end_time - start_time)
        run_times_mh.append((run_time))
    
    return run_times_mh

#Experiments
tests_i = [a for a in range(runtime_k+1,len(runtime_x)-runtime_k)]
test_times_rh = rh_runtime_test(runtime_x,runtime_y,runtime_k)
test_times_mh = mh_runtime_test(runtime_x,runtime_y,runtime_k)

#plotting the data!
import matplotlib.pyplot as plt

#plot figs
plt.figure(figsize=(14,8))
plt.grid(axis='both', alpha = 0.3)
plt.plot(tests_i, test_times_rh, label="Rolling Hashing Runtime")
plt.plot(tests_i, test_times_mh, label="Multiplicative Hashing Runtime")

#labels
plt.title("RH vs. MH  Experimental Runtime Analysis Varying x-length\n", fontsize=22)
plt.ylabel("Average runtime in s*10^-3 seconds\n", fontsize=18)
start, end = runtime_k, len(runtime_x)-runtime_k
tag = "Fig.1. showing the experimental runtime of RH vs. MH while varying the x-length({} to {}) as linear time O(p log p)."
plt.xlabel("\nNumber of averaged tests run n= {}\n\n".format(max(tests_i)+1)+tag.format(start,end), fontsize=16)
plt.xlim(0,max(tests_i)+1)
plt.legend()

#save plot to root directory
import os

#get the root directory path
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
new_plot = 'plot1.png'
plt.savefig(os.path.join(ROOT_DIR, new_plot)) 
plt.close()



def rh_runtime_test(x,y,k):
    """
    Calculates the average runtime of a rolling hashing function
    """
    import time
    import random
    run_time = 0 
    run_times_rh = []
    
    #average test number of runtimes
    for test in range(k,len(min(x,y))-k):
        #Start the timer
        start_time = time.time()
        #Run the function
        HT = HashTableV1(x,y,test) #vary the length of the input data
        HT.rh_get_match()
        #func_name(testdata)
        #Stop the timer
        end_time = time.time()
        #Record values
        run_time += (end_time - start_time)
        run_times_rh.append((run_time))
        
        
    return run_times_rh

def mh_runtime_test(x,y,k):
    """
    Calculates the average runtime of a multiplicative hashing function
    """
    import time
    import random
    run_time = 0 
    run_times_mh = []
    
    #average test number of runtimes
    for test in range(k,len(min(x,y))-k):
        #Start the timer
        start_time = time.time()
        #Run the function
        HT = HashTableV2(x,y,test) #vary the length of the input data
        HT.regular_get_match()
        #func_name(testdata)
        #Stop the timer
        end_time = time.time()
        #Record values
        run_time += (end_time - start_time)
        run_times_mh.append((run_time))
    
    return run_times_mh

#Experiments!!!
test_i = [a for a in range(runtime_k,len(min(runtime_x,runtime_y))-runtime_k)]
test_times_rh_t2 = rh_runtime_test(runtime_x,runtime_y,runtime_k)
test_times_mh_t2 = mh_runtime_test(runtime_x,runtime_y,runtime_k)

#plotting the data!
import matplotlib.pyplot as plt

#plot figs
plt.figure(figsize=(14,8))
plt.grid(axis='both', alpha = 0.3)
plt.plot(test_i, test_times_rh_t2, label="Rolling Hashing Runtime")
plt.plot(test_i, test_times_mh_t2, label="Multiplicative Hashing Runtime")

#labels
plt.title("RH vs. MH  Experimental Runtime Analysis Varying k-length\n", fontsize=22)
plt.ylabel("Average runtime in s*10^-3 seconds\n", fontsize=18)

start, end = runtime_k, len(min(runtime_x,runtime_y))-runtime_k
tag = "Fig.2. showing the experimental runtime of RH vs. MH while varying the k-length({} to {}) as linear time O(p log p)."
plt.xlabel("\nNumber of averaged tests run n= {}\n\n".format(max(test_i)+1)+tag.format(start,end), fontsize=16)
plt.xlim(0,max(test_i)+1)
plt.legend()

###Note: This takes around 3-4mins to execute...

#save plot to root directory
import os

#get the root directory path
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
new_plot = 'plot2.png'
plt.savefig(os.path.join(ROOT_DIR, new_plot)) 
plt.close()