**The Collatz Conjecture**

The Collatz Conjecture is one of the most famous unsolved problems in mathematics. It was proposed in 1937 and remains unproven to this day.

The conjecture is based on a very simple process:

Start with any positive integer.
If the number is even, divide it by 2.
If the number is odd, multiply it by 3 and add 1.
Repeat the process with the resulting number.

The conjecture states that no matter which positive integer you start with, the sequence will always eventually reach the number 1.

Once the sequence reaches 1, it enters a repeating cycle:

1 → 4 → 2 → 1 → 4 → 2 → 1 ...

Example

Starting with 6:

6 is even → 6 ÷ 2 = 3
3 is odd → 3 × 3 + 1 = 10
10 is even → 10 ÷ 2 = 5
5 is odd → 5 × 3 + 1 = 16
16 → 8 → 4 → 2 → 1

Even though the rules are simple, mathematicians have not yet been able to prove that this process works for all positive integers. However, it has been tested for extremely large numbers using computers, and every tested number eventually reaches 1.

**informations of this program**

This program was developed using Python.

It allows the user to enter a positive integer and then automatically applies the rules of the Collatz Conjecture until the sequence reaches 1.

During execution, the program:

1-Calculates each step of the sequence
2-Counts how many even numbers were generated
3-Counts how many odd numbers were generated
4-Calculates the total number of steps required to reach 1

The purpose of this project is to demonstrate the behavior of the Collatz sequence in a practical way
