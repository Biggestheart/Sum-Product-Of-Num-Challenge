"""
CHALLENGE
sum-product numbers

A sum-product number is a number N such that the sum of N's digits times the product of N's digits is N itself. 

For example, for the number abcd, (a, b, c and d are the number digits)

  abcd = (a + b + c + d)*(a * b * c * d) 

Find all sum-product numbers.

There are exactly three such numbers.
"""

from math import prod
found=0
i=-1
while found < 4:
  i+=1
  digits=[int(c) for c in str(i)]
  sdigits=sum(digits)
  pdigits=prod(digits)
  if sdigits * pdigits == i:
    print(i)
    found+=1
    
    
    
    
    
    
    
    
    // package pattern;



public class SumProductNumber {
    static int countSumDigitProductNumber = 0;

    public static void main(String[] args) {

        for (int i = 0; i < 1000; i++) {
            countSumDigitProductNumber = SumProductNumber.findSumProductNumber(i, countSumDigitProductNumber);
        }

    }

    private static int findSumProductNumber(int n, int countSumDigitProductNumber) {
        int digitsSum = 0, digitsProduct = 1;
        for (char ch : String.valueOf(n).toCharArray()) {
            digitsProduct *= (int) (ch - '0');
            digitsSum += (int) (ch - '0');
        }
        if (n == (digitsProduct * digitsSum)) {
            System.out.println(String.format("%d sum-product number is  =>  %d", ++countSumDigitProductNumber, n));
        }
        return countSumDigitProductNumber;
    }

}
