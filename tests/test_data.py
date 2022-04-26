#Test 0: showing that the impementation meets an illustrative example
X = "today is Monday"
Y = "day"
K = 3

# Test 1: Two very similar short strings to check collision rates. 
# This is a good test case because the string x contains all 26 letters of the alphabet.

# k=4 is a good choice for collision detection because as k increases the longer k-grams have 
# a lower probability of collision. The inverse is true. k=1 would be impractical as we would just
# be checking individual letters. k as 3-5 is the sweet spot, as most English words are arounf this length.

test1_x = "thequickbrownfoxjumpsoverthelazydogforthekingsheartybreakfastofeggstoastandbeans"
test1_y = "ilovethelazydogeatingthefoxsbeans"
test1_k = 4

# Test 2: Two somewhat similar very long strings to check collision rates.
# This is a good test case as it checks the robustness of the hash function as x, y grow larger.
# the expectation is that in a larger data set, the probability of collisions is increased,
# and test 2 and 3 investigate this aspect. 

# The test data was obtained from: http://www.cse.psu.edu/~sxz16/papers/ISSTA_alg_plagrism.pdf

test2_x = ("In recent years, plagiarism has raised great concern over"
"intellectual property protection. Plagiarists violate intellectual" 
"property rights either by copying source binary code or by stealing" 
"and covertly implementing protected algorithms. The first case is also" 
"known as software plagiarism, which has been thoroughly discussed in" 
"many literatures. However, very little attention has"
"been paid to the second case, namely algorithm plagiarism."
"Detection of algorithm plagiarism is desired in many practical" 
"scenarios. For example, when an algorithm is protected"
"by patent right, the owners of this algorithm need to defend"
"their proprietary by examining the plagiarism of this algorithm" 
"in other programs. Another scenario is that software"
"companies often need to verify that their software products"
"do not plagiarize any patent protected algorithms before release" 
"to avoid lawsuits. In addition to its commercial potential," 
"algorithm plagiarism detection can also provide important insight" 
"into the identification of essential characteristics of an algorithm." 
"However, to the best of our knowledge,"
"there has been little previous work focusing on this topic.")

test3_y = ("In this work, we address the problem of algorithm"
"plagiarism, which occurs when a plagiarist, violating intellectual"
"property rights, steals others algorithms and covertly implements" 
"them. In contrast to software plagiarism, which has"
"been extensively studied, limited attention has been paid"
"to algorithm plagiarism. In this paper, we propose two dynamic "
"value based approaches, namely N version and annotation, for" 
"algorithm  plagiarism detection. Our approaches are motivated by "
"the observation that there exist some critical runtime values which "
"are irreplaceable and uneliminatable for all implementations of the "
"same algorithm. The N version approach extracts such values by" 
"filtering out noncore values. The annotation approach leverages" 
"auxiliary information to flag important variables which "
"contain corevalues. We also propose a value dependence graph based"
"similarity metric in addition to the longest common subsequence based" 
"one, in order to address the potential value reordering attack. We "
"have implemented a prototype and evaluated the proposed schemes on "
"various algorithms. The results show that our approaches to"
"algorithm plagiarism detection are practical, effective and" 
"resilient to many automatic obfuscation techniques")

# In this test, we are interested in seeing whether this random string y (contained within x)
# can be found without causing any collisions.

test2_y = "eleasetoavo"
test2_k = len(test2_y)