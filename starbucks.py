import sys

#sales tax for Seattle
DEFAULT_SALES_TAX = 0.096
#number of bonus stars per $1 pretax spent
DEFAULT_BONUS_STARS_PER_UNIT = 2
#ratio of bonus stars : $ amount pretax spent
DEFAULT_RATIO = 10

def main() :
    '''Main'''
    
    if len(sys.argv) == 3 :
        bonusStars = int(sys.argv[1])
        cost = float(sys.argv[2])
        bonusStarsPerUnit = DEFAULT_BONUS_STARS_PER_UNIT
        salesTax = DEFAULT_SALES_TAX
        ratio = DEFAULT_RATIO
    elif len(sys.argv) == 6 :
        bonusStars = int(sys.argv[1])
        cost = float(sys.argv[2])
        bonusStarsPerUnit = int(sys.argv[3]) 
        salesTax = float(sys.argv[4]) 
        ratio = float(sys.argv[5])
    else :
        print ("Incorrect argument count. Usage:")
        print ("\tpython " + sys.argv[0] + " <bonus_stars> <cost> [<bonus_stars_per_unit> <sales_tax> <stars_to_cost_ratio>]")
        return

    calculatedRatio = (bonusStars + (bonusStarsPerUnit * cost)) / ((1 + salesTax) * cost)

    if calculatedRatio >= ratio :
        print ("WORTH IT!")
        print ("Ratio: {:.2f} >= {:.2f}".format(calculatedRatio, ratio))
    else :
        print ("DON'T WASTE YOUR MONEY!")
        print ("Ratio: {:.2f} < {:.2f}".format(calculatedRatio, ratio))

    return

if __name__ == "__main__" :
    main()

