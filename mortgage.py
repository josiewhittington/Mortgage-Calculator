"""Perform fixed-rate mortgage calculations."""

from argparse import ArgumentParser
import math
import sys


def get_min_payment(principal, interest, term = 30, payments = 12):
    """Finds the minimum mortgage payment each month
    Args: 
        principal (float): total amount of the mortgage
        interest (float): annual interest rate
        term (int): optional with default of 30, term of mortgage in years 
        payments (int): optional with default of 12, number of payments each year
        
    Returns:
        (int) minimum mortgage payment
    """
    r = interest/payments
    n = term*payments
    A = principal * r * (1 + r)**n/((1 + r)**n - 1)
    return math.ceil(A)

def interest_due(balance, interest, payments = 12):
    """Finds the interest that is due in the monthly mortgage payment
    
    Args:
        balance (float): remaning balance of mortgage
        interest(float): annual interest rate 
        payments (int): optional with default of 12, number of payments each year
        
    Returns:
        (float): amount of interest due in monthly mortage payment
    
    """
    r = interest/payments
    i = balance * r
    return i

def remaining_payments(balance, interest, target, payments = 12):
    """Finds the total number of payments needed to fully pay off the mortgage
    
    Args: 
        balance (float): remaning balance of mortgage
        interest(float): annual interest rate 
        target (float): how much the user wants to pay for each payment 
        payments (int): optional with default of 12, number of payments each year
        
    Returns:
        (int): number of payments needed to pay off the mortgage
    
    """
    numPayments = 0
    while balance > 0:
        interestLeft = interest_due(balance, interest, payments=payments)
        paid = target - interestLeft
        balance -= paid
        numPayments += 1
    return numPayments
    
def main(principal, interest, term = 30, payments = 12, target = None):
    """ Tells the user the remaining balance needed to be paid and how many payments they have left.
    
    Args:
        principal (float): total amount of the mortgage
        interest (float): annual interest rate
        term (int): optional with default of 30, term of mortgage in years 
        payments (int): optional with default of 12, number of payments each year
        target (float): amount user wants to pay
    
    Side effects: Prints how much the user needs to pay and how many payments it will take
    """
    minimum = get_min_payment(principal, interest, term, payments)
    print(minimum)
    if target is None:
        target = minimum
    elif target < minimum:
        print("Need to increase minimum payment")
    else:
        print(f"This is how much you need to pay: {target}. You will pay it off in {payments} payments")


def parse_args(arglist):
    """Parse and validate command-line arguments.
    
    This function expects the following required arguments, in this order:
    
        mortgage_amount (float): total amount of a mortgage
        annual_interest_rate (float): the annual interest rate as a value
            between 0 and 1 (e.g., 0.035 == 3.5%)
        
    This function also allows the following optional arguments:
    
        -y / --years (int): the term of the mortgage in years (default is 30)
        -n / --num_annual_payments (int): the number of annual payments
            (default is 12)
        -p / --target_payment (float): the amount the user wants to pay per
            payment (default is the minimum payment)
    
    Args:
        arglist (list of str): list of command-line arguments.
    
    Returns:
        namespace: the parsed arguments (see argparse documentation for
        more information)
    
    Raises:
        ValueError: encountered an invalid argument.
    """
    # set up argument parser
    parser = ArgumentParser()
    parser.add_argument("mortgage_amount", type=float,
                        help="the total amount of the mortgage")
    parser.add_argument("annual_interest_rate", type=float,
                        help="the annual interest rate, as a float"
                             " between 0 and 1")
    parser.add_argument("-y", "--years", type=int, default=30,
                        help="the term of the mortgage in years (default: 30)")
    parser.add_argument("-n", "--num_annual_payments", type=int, default=12,
                        help="the number of payments per year (default: 12)")
    parser.add_argument("-p", "--target_payment", type=float,
                        help="the amount you want to pay per payment"
                        " (default: the minimum payment)")
    # parse and validate arguments
    args = parser.parse_args()
    if args.mortgage_amount < 0:
        raise ValueError("mortgage amount must be positive")
    if not 0 <= args.annual_interest_rate <= 1:
        raise ValueError("annual interest rate must be between 0 and 1")
    if args.years < 1:
        raise ValueError("years must be positive")
    if args.num_annual_payments < 0:
        raise ValueError("number of payments per year must be positive")
    if args.target_payment and args.target_payment < 0:
        raise ValueError("target payment must be positive")
    
    return args


if __name__ == "__main__":
    try:
        args = parse_args(sys.argv[1:])
    except ValueError as e:
        sys.exit(str(e))
    main(args.mortgage_amount, args.annual_interest_rate, args.years,
         args.num_annual_payments, args.target_payment)
