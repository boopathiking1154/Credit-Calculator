#import required modules
import argparse
import math
import sys


def main():
    """parsing the command line input"""
    parser = argparse.ArgumentParser()
    parser.add_argument('--type', type=str, help='type of payments: "annuity" or "diff"')
    parser.add_argument('--principal', type=int, help='Enter credit principal')
    parser.add_argument('--periods', type=int, help='Enter count of periods')
    parser.add_argument('--payment', type=float, help='Enter monthly payment')
    parser.add_argument('--interest', type=float, help='Enter credit interest')
    args = parser.parse_args()

    if len(sys.argv) != 5:
        print('Incorrect parameters')
    elif args.type is None or args.type not in ['annuity', 'diff']:
        print('Incorrect parameters')
    elif args.type == 'diff' and args.payment is not None:
        print('Incorrect parameters')
    elif args.interest is None:
        print('Incorrect parameters')

    elif args.type == 'annuity':
        if args.payment is None:
            if args.principal < 0 or args.periods < 0 or args.interest < 0:
                print('Incorrect parameters')
            else:
                calc_payment(args.principal, args.periods, args.interest)

        if args.periods is None:
            if args.principal < 0 or args.payment < 0 or args.interest < 0:
                print('Incorrect parameters')
            else:
                calc_periods(args.principal, args.payment, args.interest)

        if args.principal is None:
            if args.payment < 0 or args.periods < 0 or args.interest < 0:
                print('Incorrect parameters')
            else:
                calc_principal(args.payment, args.periods, args.interest)

    elif args.type == 'diff':
        if args.principal < 0 or args.periods < 0 or args.interest < 0:
            print('Incorrect parameters')
        else:
            calc_diff(args.principal, args.periods, args.interest)


def calc_payment(principal, periods, interest):
    """Function to calculate payment"""
    interest = interest / 100 / 12
    num = interest * math.pow((1 + interest), periods)
    den = math.pow((1 + interest), periods) - 1
    payment = principal * (num / den)
    payment = math.ceil(payment)
    print("Your annuity payment = {}!".format(payment))
    overpayment = periods * payment - principal
    print("Overpayment = {}".format(overpayment))


def calc_principal(payment, periods, interest):
    """Function to calculate principal"""
    interest = interest / 100 / 12
    num = interest * math.pow((1 + interest), periods)
    den = math.pow((1 + interest), periods) - 1
    principal = payment / (num / den)
    print("Your credit principal = {}!".format(principal))
    overpayment = periods * payment - principal
    print("Overpayment = {}".format(overpayment))


def calc_periods(principal, payment, interest):
    """Function to calculate period for repayment"""
    interest = interest / 100 / 12
    periods = math.log(payment / (payment - (interest * principal)), interest + 1)
    periods = math.ceil(periods)
    if periods < 12:
        print("You need {} months to repay this credit!".format(periods))
    elif periods == 12:
        print("You need 1 year to repay this credit!")
    else:
        years = periods // 12
        months = periods % 12
        if months == 0:
            print("You need {} years to repay this credit!".format(years))
        else:
            print("You need {} years and {} months to repay this credit!".format(years, months))

    overpayment = periods * payment - principal
    print("Overpayment = {}".format(overpayment))


def calc_diff(principal, periods, interest):
    """Function to calculate differential monthly payment"""
    interest = interest / 100 / 12
    sum_diff = 0
    for m in range(1, periods + 1):
        diff = math.ceil((principal / periods) + interest * (principal - principal * (m - 1) / periods))
        sum_diff += diff
        print("Month {}: paid out {}".format(m, diff))
    overpayment = sum_diff - principal
    print()
    print("Overpayment = {0}".format(overpayment))


if __name__ == '__main__':
    main()
