# Plagiarism Detection

<br>

I implement a hash function, insert and search functionality for two versions of plagiarism detection: V1(Rolling Hashing) and V2(Multiplicative Hashing). We will need the insert functionality to store the x-string k-gram hash values generated from the hash function into our hash table and the search functionality to look through the hash table for any matches between the x and y k-gram hash values. Object-Oriented Programming is used over procedural programming for three reasons: 

1. Flexibility of breaking down the program into bit-sized problems that can easily be visualized and solved.
2. Easy troubleshooting and maintenance due to its modularized structure.
3. Polymorphism and reusability of the code, especially beneficial in building version 2 of the plagiarism detector.

<br>

### Discussion of Version 1 and Version 2 Tests

<br>

> The tests I designed were meant to gauge the algorithm's collusions. This is why I decided to conduct the same tests on the two algorithms as a means of drawing a comparison. Table 1. below shows a summary of the results from the test. Both pass test 1 and 2 with 0 collusions. They also detect the same amount of plagiarism which is good to see. Generally, the amount of plagiarism that the two versions detect should be within 1-5% of each other for large input sizes. If this error margin were exeeded during the tests, then it would have drawn attention to the possibility that one of the implementations was wrong. However, here we see that in test 3, the variance in plagiarism detected is 0.02% which is acceptable. To have an even robust result, I take the average of the two versions as the final value for the plagiarism detected.

> In regards to our builds, they are a good starting point as a means of the "copy-paste" plagiarism detection because they search for carbon copies of y k-grams in the x string. However, they lack the capacity to scale up as a general plagiarism detector. In this light, our plagiarism detector is very good at one aspect of plagiarism detection. Nonetheless, there are nuances to this definition of 'good' especially when we consider what our build versions are actually doing. The scrub_input() functionality strips whitespaces and any symbols not represented in the English alphabet from the string inputs. It then takes samples of k-length from these concancated strings and compares them to each other.

<br>

<table style="align:center;width:900px">
  <tr tr style="background-color:#7F96FF;color:#ffffff;height:50px;font-size:20px;">
    <th style="text-align:right;width:40px">Version</th>
    <th style="text-align:right;width:105px">Test</th>
    <th style="text-align:center;width:145px">Matches</th>
    <th style="text-align:center;width:75px">Collisions</th>
    <th style="text-align:center;width:150px">Plagiarism Level</th>
    <th style="text-align:left;width:105px">Lengths</th>
  </tr>
  <tr tr style="height:30px;text-align:center;font-size:14px;">
    <td style="text-align:right">V.1</td>
    <td style="text-align:right">Test 1</td>
    <td style="text-align:center">8</td>
    <td style="text-align:center">0.00%</td> 
    <td style="text-align:center">10.67%</td> 
    <td style="text-align:left;font-size:15px;">
        <ul>
            <br>
            <li>x-length: 80</li>
            <li>y-length: 33</li>
            <li>k-length: 4</li> 
        </ul>
    </td>
  </tr>
  <tr tr style="height:30px;text-align:center;font-size:14px;">
    <td style="text-align:right">V.2</td>
    <td style="text-align:right">Test 1</td>
    <td style="text-align:center">8</td>
    <td style="text-align:center">0.00%</td> 
    <td style="text-align:center">10.67%</td> 
    <td style="text-align:left;font-size:15px;">
        <ul>
            <br>
            <li>x-length: 80</li>
            <li>y-length: 33</li>
            <li>k-length: 4</li> 
        </ul>
    </td>
  </tr>
  <tr tr style="height:30px;text-align:center;font-size:14px;">
    <td style="text-align:right">V.1</td>
    <td style="text-align:right">Test 2</td>
    <td style="text-align:center">1</td>
    <td style="text-align:center">0.00%</td> 
    <td style="text-align:center">0.11%</td> 
    <td style="text-align:left;font-size:15px;">
        <ul>
            <br>
            <li>x-length: 1142 </li>
            <li>y-length: 11</li>
            <li>k-length: 11</li> 
        </ul>
    </td>
  </tr>
  <tr tr style="height:30px;text-align:center;font-size:14px;">
    <td style="text-align:right">V.2</td>
    <td style="text-align:right">Test 2</td>
    <td style="text-align:center">1</td>
    <td style="text-align:center">0.00%</td> 
    <td style="text-align:center">0.11%</td> 
    <td style="text-align:left;font-size:15px;">
        <ul>
            <br>
            <li>x-length: 1142</li>
            <li>y-length: 11</li>
            <li>k-length: 11</li> 
        </ul>
    </td>
  </tr>
  <tr tr style="height:30px;text-align:center;font-size:14px;">
    <td style="text-align:right">V.1</td>
    <td style="text-align:right">Test 3</td>
    <td style="text-align:center">189</td>
    <td style="text-align:center">0.22%</td> 
    <td style="text-align:center">20.54%</td> 
    <td style="text-align:left;font-size:15px;">
        <ul>
            <br>
            <li>x-length: 1142</li>
            <li>y-length: 1230</li>
            <li>k-length: 13</li> 
        </ul>
    </td>
  </tr>
  <tr tr style="height:30px;text-align:center;font-size:14px;">
    <td style="text-align:right">V.2</td>
    <td style="text-align:right">Test 3</td>
    <td style="text-align:center">189</td>
    <td style="text-align:center">0.00%</td> 
    <td style="text-align:center">20.52%</td> 
    <td style="text-align:left;font-size:15px;">
        <ul>
            <br>
            <li>x-length: 1142</li>
            <li>y-length: 1230</li>
            <li>k-length: 13</li> 
        </ul>
    </td>
  </tr>
</table>
<br>
<p style="font-size:15px;text-align:center"><i>Table 1. A table showing the summary of V1 and V2 Tests.</i></p><br>

<br>

### Discussion of Version 1 and Version 2 Runtimes

<br>

> Since we're interested in the performance of the algorithm with the scaling of x in test 4, and scaling of k in test 5, the tests shown below tracked the growth of time during insertion and searching as the values of x and k are varied respectively. The cells below show the results. 

<br>

Fig.1 shows the growth of the multiplicative and rolling hashing methods to be logarithmic in O(p log p), where p is the length of string x with some variations as the length of x is increased.  

<br>

<p align="center">
  <img src="https://github.com/Phil-Barv/Regression-Models-for-Applicant-Best-Fit/blob/main/plots/Susie.png" alt="Multiplicative and rolling hashing methods to be logarithmic in O(p log p) as the length of x is increased."/>
</p>

<br>

Fig 2. as well shows the growth of the multiplicative and rolling hashing methods to be logarithmic in O(p log p) with some variations as the length of k is increased.
s
<br>

<p align="center">
  <img src="https://github.com/Phil-Barv/Regression-Models-for-Applicant-Best-Fit/blob/main/plots/Susie.png" alt="Multiplicative and rolling hashing methods to be logarithmic in O(p log p) with some variations as the length of k is increased"/>
</p>

<br>

> In both cases, even though they are in O(p log p) time, the multiplicative hashing method has a relatively higher average runtime which could hint that even though its in O(p log p) time, it has a higher constant C. This meets our expectation that multiplicative hashing would perform worse because it does not save on computation time the way rolling hashing does by having a window of k-length and only removing the first element and adding a new last element. We can verify that this is the case by conducting an analytical analysis for the recurrence time. 
