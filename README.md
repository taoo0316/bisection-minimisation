# bisection-minimisation

A program written in Julia for solving minimisation problems using bisection

```Algorithm```

<img width="357" alt="Screenshot 2023-03-28 at 11 20 31 AM" src="https://user-images.githubusercontent.com/95064358/228174461-2203e372-452c-460d-b986-fc732b5675b2.png">

The program takes in four arguments: the first derivative of the objective function, the lower bound, the upper bound and the error tolerance.

It returns the approximate solution x and the number of iterations.

To run the program easily, you might want to check out the online Julia compiler and interpreter by [Replit](https://replit.com/new/julia).

To visualise the algorithm at work, one can perhaps keep track of the points visited when running the program (use print statements to log the x value for each iteration) and plot them on the graph of the objective function. 

<img width="447" alt="Screenshot 2023-03-28 at 12 16 47 PM" src="https://user-images.githubusercontent.com/95064358/228189705-4a0c5c0e-e131-4a20-871a-48f8571d75be.png">

<img width="656" alt="Screenshot 2023-03-28 at 12 16 29 PM" src="https://user-images.githubusercontent.com/95064358/228189712-5ba4ccad-9860-4663-8191-e3bfa898049a.png">

These are created using Desmos, keeping track of all 15 iterations of the program.
