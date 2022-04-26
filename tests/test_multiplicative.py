from hashing_strategies.multiplicative_hashing import HashTableV2
from tests.test_data import X, Y, K, test1_x, test1_y, test1_k, test2_k, test2_x, test2_y, test3_y

print("\n\nTesting Multiplicative Hashing Strategy\n")

print("\nCommencing test 0...")
ht0 = HashTableV2(X,Y,K)
ht0.regular_get_match(True) #toogle True/False to show/hide the matches --> useful for testing runtime
print("\nTest 0 completed \n")

assert(ht0.print_all_matches() == [(2, 0), (10, 0)])

#Test 1
print("\nCommencing test 1...")
HT1 = HashTableV2(test1_x, test1_y, test1_k)
HT1.regular_get_match()
HT1.summary()
print("\nTest 1 completed \n")

#Test 2
print("Commencing test 2...")
HT2 = HashTableV2(test2_x, test2_y, test2_k)
HT2.regular_get_match()
HT2.summary()
print("\nTest 2 completed \n")

#Test 3
print("Commencing test 3...")
HT3 = HashTableV2(test2_x, test3_y, 13)
HT3.regular_get_match()
HT3.summary()
print("\nTest 3 completed \n")