# Calculator -> Arithmetic Operations 

a = int(input("Enter the value of a : "))
b = int(input("Enter the value of b : "))

choice = int (input("""Enter your choice :
1. Addition
2. Subtraction
3. Division
4. Modulus
5. Exponentiation
6. Multiplication
7. Floor division : """))

if(choice == 1):{
    print("Your answer is a+b : ", a+b)
}
    
elif(choice == 2):{
    print("Your answer is a-b : ", a-b)
}   

elif choice == 3:
        if b != 0:
            print(f"Your answer is a/b : {a/b}")
        else:
            print("Error: Division by zero is not allowed.")

elif(choice == 4):{
    print("Your answer is a%b : ", a%b)
}

elif(choice == 5):{
    print("Your answer is a**b : ", a**b)
}

elif(choice == 6):{
    print("Your answer is a*b : ", a*b)
}

elif choice == 7:
        if b != 0:
            print(f"Your answer is a//b : {a//b}")
        else:
            print("Error: Division by zero is not allowed.")
else:
    print("Invalid choice. Please choose a valid operation.")
