Program that finds calculations for fixed-rate mortgages

get_min_payment (function)
    - Parameters
        - The total amount of the mortgage
        - The annual interest rate (you can assume this is a float between 0 and 1)
        - The term of the mortgage in years (default value of 30)
        - The number of payments per year (default value of 12)

    - Function
        - Calculates minimum necessary mortgage payment
        Formula used:
        𝐴=(𝑃𝑟(1+𝑟)^𝑛)/((1+𝑟)^(𝑛)−1)


interest_due (function)
    - Parameters
        - The balance of the mortgage 
        - The annual interest rate
        - The number of payments per year (default value of 12)

    - Function
        - Calulates interest due at next payment
        Formula used:
        𝑖=𝑏𝑟


remaining_payments (function)
    - Parameters
        - The balance of the mortgage 
        - The annual interest rate 
        - The target payment 
        - The number of payments per year (default value of 12)

    - Function
        - Compute and return the number of payments required to pay off the mortgage
 
 main (function)
    - Parameters
        - The total amount of the mortgage 
        - The annual interest rate 
        - The term of the mortgage in years 
        - The number of payments per year (default value of 12)
        - The user’s target payment 

    - Function
        - Compute and display minimum mortgage payment 
        - Compute and display total number of payments 


Running Program
    - In terminal use file, mortgage amount, and interest rate
        - Example:
            python3 mortgage.py 300000 0.03

    - Using optional argument, -y (the term of the mortgage in years)
        - Example:
            python3 mortgage.py 300000 0.03 -y 15

    - Using optional argument, -n (the number of annual payments)
        - Example:
            python3 mortgage.py 300000 0.03 -n 10

    - Using optional argument, -p (the target payment)
        Example:
            python3 mortgage.py 300000 0.03 -y 15 -p 4000