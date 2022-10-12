# FruitionSciencesTechnicalTest

This is a technical test for Fruition Sciences. The goal is to create a simple program who take file:
    
    - The first line is a size of the map [x,y] separated by a space
    
    - The second line is the position of the vacuum {x,y}, and that direction {N,W,S,E} [x,y,dir] separated by a space
    
    - The third line is a list of instructions {A,D,G}. Where A is advance, D is turn right, G is turn left

At the end this program print the final position and direction of the vacuum [x,y,dir].


To launch the program:

    $> python3 main.py [file]



NB: The map index begin at 0. For example is the map size is x:10 y:10, the vancuum can't to position where x = 10 or y = 10. But it can be position where x = 0 or y = 0.


NB: I've implemented a little error gestion for the file. If the file is not correct, the program print an error message and exit.

NB: You can pass the file as argument of the program. If you don't pass any argument, the program will use the file "test.txt" in the same directory.

