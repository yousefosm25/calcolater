class Calcolator :
    def __init__(self):
        self.num1 = 0
        self.num2 = 0
    
    def continu(self):
         continu=input("Do you want to Continue(yes/no): ")
         if continu.lower()=="yes":
                self.printt()
         else:
           print("Thank you for using My Calcolator")
           exit()
    def inpute1(self):
        try:
            self.num1 = float(input('Enter the first number: '))
            self.num2 = float(input('Enter the second number: '))
        except ValueError:
            print('Error: Invalid input. Please enter a number.')
            self.inpute1()
    def inpute2(self):
        try:
            self.num1 = int(input('Enter the number: '))
        except ValueError:
            print('Error: Invalid input. Please enter an integer.')
            self.inpute2()
    def add(self):
        self.inpute1()
        return self.num1 + self.num2
    
    def subtract(self):
        self.inpute1()
        return self.num1 - self.num2
    
    def multiply(self):
        self.inpute1()
        return self.num1 * self.num2
    
    def divide(self):
        self.inpute1()
        if self.num2 != 0:
            return self.num1 / self.num2
        else:
            print( 'Error: Division by zero')
            self.divide()
            
    
    def power(self):
        self.inpute1()
        return self.num1 ** self.num2
    
   
    def factorial(self, n=None):
        if n is None:  # Check if n is not passed, then prompt for input once
            self.inpute2()
            if self.num1 < 0:
                print('Error: Factorial is not defined for negative numbers')
                return None
            n = self.num1
        if n == 0 or n == 1:
            return 1
        return n * self.factorial(n - 1)

    def fibonacci(self):
        self.inpute2()
        if self.num1 < 0:
            return 'Error: Fibonacci sequence is not defined for negative numbers'
        elif self.num1 == 0:
            return 0
        elif self.num1 == 1:
            return 1
        else:
            a, b = 0, 1
            for _ in range(2, self.num1 + 1):
                a, b = b, a + b
            return b
        
    def is_prime(self):
        self.inpute2()
        if self.num1 <= 1:
            return False
        elif self.num1 == 2:
            return True
        elif self.num1 % 2 == 0:
            return False
        else:
            for i in range(3, int(self.num1 ** 0.5) + 1, 2):
                if self.num1 % i == 0:
                    return False
            return True
        
    def gcd(self):
        self.inpute1()
        if self.num1 < 0 or self.num2 < 0:
            return 'Error: GCD is not defined for negative numbers'
        elif self.num1 == 0:
            return self.num2
        elif self.num2 == 0:
            return self.num1
        else:
            while self.num2 != 0:
                self.num1, self.num2 = self.num2, self.num1 % self.num2
            return self.num1

    def lcm(self):
        self.inpute1()
        if self.num1 < 0 or self.num2 < 0:
            return 'Error: LCM is not defined for negative numbers'
        else:
            return (self.num1 * self.num2) // self.gcd(self.num1, self.num2)
        
    def is_perfect_square(self):
        self.inpute2()
        return int(self.num1 ** 0.5) ** 2 == self.num1
    
    def is_perfect_cube(self):
        self.inpute2()
        return int(self.num1 ** (1/3)) ** 3 == self.num1
    
    def is_armstrong(self):
        self.inpute2()
        num_str = str(self.num1)
        num_digits = len(num_str)
        sum_digits = sum(int(digit) ** num_digits for digit in num_str)
        return sum_digits == self.num1
    
    def is_palindrome(self):
        self.inpute2()
        num_str = str(self.num1)
        return num_str == num_str[::-1]
    
    def printt(self): 
        try:
            print("Welcome to calcolator")
            print('''Please choose an option:
                1- add
                2- subtract
                3- multiply
                4- divide
                5- power
                6- factorial
                7- fibonacci
                8- is_prime
                9- gcd
                10- lcm
                11- is_perfect_square
                12- is_perfect_cube
                13- is_armstrong
                14- is_palindrome''')
            choice = float(input("Enter your choice: "))
            if choice == 1:
                print(f'Result: {self.add()}') 
            elif choice == 2:
                print(f'Result: {self.subtract()}')
            elif choice == 3:
                print(f'Result: {self.multiply()}')
            elif choice == 4:
                print(f'Result: {self.divide()}')
            elif choice == 5:
                print(f'Result: {self.power()}')
            elif choice == 6:
                print(f'Result: {self.factorial()}')
            elif choice == 7:
                print(f'Result: {self.fibonacci()}')
            elif choice == 8:
                print(f'Result: {self.is_prime()}')
            elif choice == 9:
                print(f'Result: {self.gcd()}')
            elif choice == 10:
                print(f'Result: {self.lcm()}')
            elif choice == 11:
                print(f'Result: {self.is_perfect_square()}')
            elif choice == 12:
                print(f'Result: {self.is_perfect_cube()}')
            elif choice == 13:
                print(f'Result: {self.is_armstrong()}')
            elif choice == 14:
                print(f'Result: {self.is_palindrome()}')
            else:
                print('Invalid choice. Please try again.')
                self.printt()
        except ValueError:
            print("Invalid choice. Please try again")
            self.printt()
        self.continu()
        
        
S1= Calcolator()
S1.printt()