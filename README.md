# euclidean_distance
CS5920 - Machine Learning - Chapter 1 - Algorithm for Euclidean distance 


### Setup
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python calculate_euclidean_distance.py

~~

python calculate_euclidean_distance.py
Select an option (integer):

    1: Find Euclidean Distance between 2 n-dimension cartesian-coordinates.
    2: Find Euclidean Distance between multiple n-dimension cartesian-coordinate(s) with given same-dimension cartesian-coordinate

    (note) Send your suggestion on Saurabh.Chopra.2021@live.rhul.ac.uk for any suggestions.

>2

!Enter comma-seperated-without-spaces values your `test-coordinate` vector/cartesian-coordinate (Example: 1,2,3): 1,1

How many coordinates would you like to compute the distance with your test-coordinate with? (Example: 3): 4

!Enter comma-seperated-without-spaces values your `1` vector/cartesian-coordinate (Example: 1,2,3): 0,0

!Enter comma-seperated-without-spaces values your `2` vector/cartesian-coordinate (Example: 1,2,3): 0,2

!Enter comma-seperated-without-spaces values your `3` vector/cartesian-coordinate (Example: 1,2,3): 1,2

!Enter comma-seperated-without-spaces values your `4` vector/cartesian-coordinate (Example: 1,2,3): 0,3

Euclidean Distance Table:

  FromVector ToVector  EuclideanDistance

0        1,1      0,0           1.414214

0        1,1      0,2           1.414214

0        1,1      1,2           1.000000

0        1,1      0,3           2.236068
