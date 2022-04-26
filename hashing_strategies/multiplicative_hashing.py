class HashTableV2:
    def __init__(self, x, y, k):
        #set up variables
        self.k = k
        #clean x string
        self.x = self.scrub_input(x)
        #clean y string
        self.y = self.scrub_input(y)
        #large ODD prime number to reduce collisions
        self.q = 664918
        #set up alphabet value calculator where a=1, b=2... z=26
        self.alpha_val = lambda a:(ord(a)-ord("a")+1)
        #initialize hash table of fixed size
        self.Tx = [HashTableNodeV2(float("inf"),float("inf")) for a in range((len(self.x)-self.k+1))]
            
    def scrub_input(self, string):
        """
        Cleans up input string to remove all punctuation symbols and white spaces
        Input:
        - string: string
        - k: int, length of substring
        Output:
        - string: scrubbed concatenated string
        """
        string = string.replace(" ","").lower()
        illegal_chars = [';', ',', '.', '?', '!', '_', '[', ']', ':', '“', '”', '"', '–', '-','/','@','(',')']

        if len(string) == 0:
            raise ValueError("Please pass a non-empty string")

        elif self.k > len(string):
            raise ValueError("A k-gram cannot be greater than the main string")

        else:
            #remove the illegal characters
            string = ''.join(char for char in string if char not in illegal_chars)
            #remove new lines or tabs if present
            string = ''.join(char if (char not in ['\n', '\r', '\t']) else " " for char in string)
            return string
    
    def hash_function(self,lst):
        """
        A hash function that is direction sensitive, such that AAB and BAA 
        do not have the same hash value.
        """
        #import necessary libraries to perform floor()
        import math
        #counter
        k_gram = 0
        #hash table dimension squared to accomodate larger inputs
        m = (len(self.x)-self.k+1)**2
        #calculate the individual value of each character and sum them up
        for j in range(self.k):
            #use power to base 2 to make hash values direction sensitive
            power = self.k-j
            #calculate the hash value using multiplicative hashing
            k_gram += math.floor(m*((self.alpha_val(lst[j])*0.618)%1))*2**power
            
        return k_gram
    
    def multiplicative_hashing_insert(self):
        """
        A hash function that utilizes the multiplicative hash method to calculate the hash values of 
        a string x.
        """
        #initialize the first k-item's hash value 
        hashed_key = self.hash_function(self.x[:self.k])
        #create a node for this k-gram
        node = HashTableNodeV2(hashed_key,[0])
        #insert the node into the hash table
        self.Tx[0] = node
        
        #use multiplicative hashing to calculate the subsequent k-gram hash values
        for m in range(len(self.x)-self.k):
            hashed_key = self.hash_function(self.x[m+1:self.k+m+1])
            #create list of keys to check against
            self.keys = [a.key for a in self.Tx if a.key != float("inf")]
            #record the instance as a list of tuples
            if hashed_key in self.keys:
                self.Tx[self.keys.index(hashed_key)].value.append(m+1)
            else:
                new_node = HashTableNodeV2(hashed_key,[m+1])
                self.Tx[len(self.keys)] = new_node

    def multiplicative_hashing_search(self):
        """
        This function searches y k-grams against the data in the hash table.
        """
        #initialize the first k-item's hash value 
        hashed_key = self.hash_function(self.y[:self.k])
        #set up holder for the matches
        self.matches = []
        #check if the generated hash value is in the hash table
        if hashed_key in self.keys:
            #if the value is a list, unpack it and create (i,j) tuples
            if isinstance(self.Tx[self.keys.index(hashed_key)].value,list):
                for match in self.Tx[self.keys.index(hashed_key)].value:
                    self.matches.append((match,0))
            else:        
                self.matches.append((self.Tx[self.keys.index(hashed_key)].value,0))
                
        #for y-strings longer than k, we want to use multiplicative hashing to generate y-string values
        if len(self.y) > self.k:
            for n in range(len(self.y)-self.k):
                hashed_key = self.hash_function(self.y[n+1:self.k+n+1])  
                #record the instance as a list of tuples
                if hashed_key in self.keys:
                    #if the value is a list, unpack it and create (i,j) tuples
                    if isinstance(self.Tx[self.keys.index(hashed_key)].value,list):
                        for match in self.Tx[self.keys.index(hashed_key)].value:
                            self.matches.append((match,n+1))
                    else:        
                        self.matches.append((self.Tx[self.keys.index(hashed_key)].value,n+1))
             
        if self.display == True:
            #customize output, especially usefull for large x and y strings                
            if len(self.matches) > 9:
                print("Displaying {} out of {} matches:".format(9, len(self.matches)), self.matches[:9])
            else:
                print("Displaying all matches:", self.matches)
            
    def regular_get_match(self, display=False):
        """
        Finds all common length-k substrings of x and y using multiplicative hashing on both strings.
        Input:
        - x, y: strings
        - k: int, length of substring
        Output:
        - matches: A list of tuples (i, j) where x[i:i+k] = y[j:j+k]
        """
        self.display = display
        #insert x k-grams to the hash table
        self.multiplicative_hashing_insert()
        #search against y k-grams for matches
        return self.multiplicative_hashing_search() #return list of (i,j) tuple matches
    
    def print_hash_table(self):
        """
        This function prints the hash table.
        """
        #using a return wraps the output for better viewing
        return self.Tx 
    
    def print_all_matches(self):
        """
        This function prints all matches if required by the user.
        """
        return self.matches
    
    def summary(self):
        """
        This function returns a report of the number of collisions, and their percentage
        out of all k-grams.
        """
        #list to hold match values
        temp = []
        #check only the lists with more than 1 element
        for node in self.Tx:
            if isinstance(node.value,list) and len(node.value) > 1:
                for val in node.value:
                    #add each element to the list
                    temp.append(self.x[val:val+self.k])
        #second list to hold sorted matches            
        temp1 = []
        #eliminate duplicates
        for item in temp:
            if temp.count(item) <= 1:
                temp1.append(item)
                
        #calculate and print the percentage of collisions and plagiarism
        coll = len(temp1)/(len(self.x)-self.k+1)
        plagiarism = (len(self.matches)/len(self.keys)) #number of matches out of all k-grams
        
        if len(temp1) > 0:
            print("The problematic k-grams of length {} that caused {:.2%} collisions are:".format(self.k,coll),temp1)
            print("{:.2%} plagiarism detected in string y.".format(plagiarism))
        else:
            print("There are {:.2%} collisions and {:.2%} plagiarism detected by the multiplicative hashing strategy.".format(coll,plagiarism))
                           

class HashTableNodeV2:
    """
    This hash table node stores the key and value pairs.
    """
    def __init__(self,key,value):
        self.key = key
        self.value = value 
        
    def __repr__(self):
        return f"({self.key}, {self.value})"