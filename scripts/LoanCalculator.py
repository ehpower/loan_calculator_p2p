
import sys
sys.path.append("../")
from LoanCalculatorP2P.LoanCalculator import borrow
if __name__== "__main__":
    borrow(int(sys.argv[2]))
