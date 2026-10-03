account_no=0
depositAmount=0
withdrawalAmount=0
choices=0
balance=0

account_no = int(input("Enter your account number: "))

while choices !=4:
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check balance")
    print("4. Exit")

    choices=int(input("Please choose an option (1,2,3or 4)to continue: "))

    match(choices):

        case 1:
            depositAmount=int(input("Enter amount to Deposit : "))
            if depositAmount<=0:
                print("Amount should be greater than 0")

            else:
                balance = balance + depositAmount


        case 2:
            withdrawalAmount=int(input("Enter amount to Withdraw: "))
            if withdrawalAmount > balance:
                print("Insufficient funds!!Please try a lower amount: ")

            else:
                balance=balance-withdrawalAmount



        case 3:
            print(f"Your account balance is: {balance}")


        case 4:
            print("Thank you for using our app!")
            break







