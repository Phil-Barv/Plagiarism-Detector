from hashing_strategies.multiplicative_hashing import HashTableV2
from hashing_strategies.rolling_hashing import HashTableV1

w = "iloveallpartsofnaturethesunflowersandevenannoyinghumans"
z = "ilovepickingsunflowersinthesummer"

avg_word = "\nThe average word-length is: {} characters.\n".format((len(w)+len(z))/20)
print(avg_word)

ht9 = HashTableV1(w,z,4)
ht9.rh_get_match()
ht9.summary()

ht7 = HashTableV2(w,z,4)
ht7.regular_get_match()
ht7.summary()

avg_pla = "\nThe average plagiarism detected is: {:.2%}\n".format((21.57+23.53)/200)
print(avg_pla)