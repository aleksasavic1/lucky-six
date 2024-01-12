import random
import time

while True:  
    start_game = input("Do you want to start the game? y\\n: ").lower()
    if start_game == "y":
        print("\nThe game has started!")
        print("\nPlease enter numbers in the range of 1-48.\n\
(The numbers you enter must be unique; you cannot input the same number more than once!)")
        my_numbers = []

        while True:
            try:
                input_number1 = int(input("Enter the first number: "))
                if 1 <= input_number1 <= 48:
                    input_number2 = int(input("Enter the second number: "))
                    if 1 <= input_number2 <= 48:
                        input_number3 = int(input("Enter the third number: "))
                        if 1 <= input_number3 <= 48:
                            input_number4 = int(input("Enter the fourth number: "))
                            if 1 <= input_number4 <= 48:
                                input_number5 = int(input("Enter the fifth number: "))
                                if 1 <= input_number5 <= 48:    
                                    input_number6 = int(input("Enter the sixth number: "))
                                    if 1 <= input_number6 <= 48:
                                        break
                                    else:
                                        print("\nThe number must be in the range of 1-48.\nLet's try again from the beginning!")
                                else:
                                    print("\nThe number must be in the range of 1-48.\nLet's try again from the beginning!")
                            else:
                                print("\nThe number must be in the range of 1-48.\nLet's try again from the beginning!")
                        else:
                            print("\nThe number must be in the range of 1-48.\nLet's try again from the beginning!")
                    else:
                        print("\nThe number must be in the range of 1-48.\nLet's try again from the beginning!")
                else:
                    print("\nThe number must be in the range of 1-48.\nLet's try again from the beginning!")

            except ValueError:
                print("Please enter only numbers.\nLet's try again from the beginning!\n")
            
        
        print()
        while True:
            try:
                deposite = float(input("Enter the amount of money you want to deposit for your ticket ($): "))
                break

            except ValueError:
                print("Please enter only the number!\n")
        print(f"You have deposited ${deposite} onto your ticket.\n")
        
        my_numbers.append(input_number1)
        my_numbers.append(input_number2)
        my_numbers.append(input_number3)
        my_numbers.append(input_number4)
        my_numbers.append(input_number5)
        my_numbers.append(input_number6)

        

        drawn_numbers = []
        
        for i in range(35):
            while True:
                no = random.randint(1, 48)
                if no not in drawn_numbers:
                    drawn_numbers.append(no)
                    break

            print(f"The number {no} has been drawn.")
            time.sleep(1.5)

            
        print("\nDrawn Numbers:", drawn_numbers)
        print("Your Numbers:", my_numbers)

        common_elements = set(my_numbers) & set(drawn_numbers)
        common_numbers = list(common_elements)

        percentage_matched = (len(common_numbers) / len(my_numbers)) * 100

        print(f"\nYou matched {len(common_numbers)} numbers out of {len(my_numbers)}.")
        print(f"Percentage matched: {percentage_matched:.2f}%")

        if percentage_matched == 100:
            print("\nYOU WON!")

            if my_numbers[0] == drawn_numbers[-1] or my_numbers[1] == drawn_numbers[-1] \
               or my_numbers[2] == drawn_numbers[-1] or my_numbers[3] == drawn_numbers[-1] \
               or my_numbers[4] == drawn_numbers[-1] or my_numbers[5] == drawn_numbers[-1]:
                deposite *= 1
                print(f"You won ${deposite}! (x1 multiplier)")  
            elif my_numbers[0] == drawn_numbers[-2] or my_numbers[1] == drawn_numbers[-2] \
               or my_numbers[2] == drawn_numbers[-2] or my_numbers[3] == drawn_numbers[-2] \
               or my_numbers[4] == drawn_numbers[-2] or my_numbers[5] == drawn_numbers[-2]:
                deposite *= 2
                print(f"You won ${deposite}! (x2 multiplier)")
                
            elif my_numbers[0] == drawn_numbers[-3] or my_numbers[1] == drawn_numbers[-3] \
               or my_numbers[2] == drawn_numbers[-3] or my_numbers[3] == drawn_numbers[-3] \
               or my_numbers[4] == drawn_numbers[-3] or my_numbers[5] == drawn_numbers[-3]:
                deposite *= 3
                print(f"You won ${deposite}! (x3 multiplier)")

                
            elif my_numbers[0] == drawn_numbers[-4] or my_numbers[1] == drawn_numbers[-4] \
               or my_numbers[2] == drawn_numbers[-4] or my_numbers[3] == drawn_numbers[-4] \
               or my_numbers[4] == drawn_numbers[-4] or my_numbers[5] == drawn_numbers[-4]:
                deposite *= 4
                print(f"You won ${deposite}! (x4 multiplier)")
            elif my_numbers[0] == drawn_numbers[-5] or my_numbers[1] == drawn_numbers[-5] \
               or my_numbers[2] == drawn_numbers[-5] or my_numbers[3] == drawn_numbers[-5] \
               or my_numbers[4] == drawn_numbers[-5] or my_numbers[5] == drawn_numbers[-5]:
                deposite *= 5
                print(f"You won ${deposite}! (x5 multiplier)")
            elif my_numbers[0] == drawn_numbers[-6] or my_numbers[1] == drawn_numbers[-6] \
               or my_numbers[2] == drawn_numbers[-6] or my_numbers[3] == drawn_numbers[-6] \
               or my_numbers[4] == drawn_numbers[-6] or my_numbers[5] == drawn_numbers[-6]:
                deposite *= 6
                print(f"You won ${deposite}! (x6 multiplier)")
            elif my_numbers[0] == drawn_numbers[-7] or my_numbers[1] == drawn_numbers[-7] \
               or my_numbers[2] == drawn_numbers[-7] or my_numbers[3] == drawn_numbers[-7] \
               or my_numbers[4] == drawn_numbers[-7] or my_numbers[5] == drawn_numbers[-7]:
                deposite *= 7
                print(f"You won ${deposite}! (x7 multiplier)")
            elif my_numbers[0] == drawn_numbers[-8] or my_numbers[1] == drawn_numbers[-8] \
               or my_numbers[2] == drawn_numbers[-8] or my_numbers[3] == drawn_numbers[-8] \
               or my_numbers[4] == drawn_numbers[-8] or my_numbers[5] == drawn_numbers[-8]:
                deposite *= 8
                print(f"You won ${deposite}! (x8 multiplier)")
            elif my_numbers[0] == drawn_numbers[-9] or my_numbers[1] == drawn_numbers[-9] \
               or my_numbers[2] == drawn_numbers[-9] or my_numbers[3] == drawn_numbers[-9] \
               or my_numbers[4] == drawn_numbers[-9] or my_numbers[5] == drawn_numbers[-9]:
                deposite *= 9
                print(f"You won ${deposite}! (x9 multiplier)")
            elif my_numbers[0] == drawn_numbers[-10] or my_numbers[1] == drawn_numbers[-10] \
               or my_numbers[2] == drawn_numbers[-10] or my_numbers[3] == drawn_numbers[-10] \
               or my_numbers[4] == drawn_numbers[-10] or my_numbers[5] == drawn_numbers[-10]:
                deposite *= 10
                print(f"You won ${deposite}! (x10 multiplier)")
            elif my_numbers[0] == drawn_numbers[-11] or my_numbers[1] == drawn_numbers[-11] \
               or my_numbers[2] == drawn_numbers[-11] or my_numbers[3] == drawn_numbers[-11] \
               or my_numbers[4] == drawn_numbers[-11] or my_numbers[5] == drawn_numbers[-11]:
                deposite *= 15
                print(f"You won ${deposite}! (x15 multiplier)")
            elif my_numbers[0] == drawn_numbers[-12] or my_numbers[1] == drawn_numbers[-12] \
               or my_numbers[2] == drawn_numbers[-12] or my_numbers[3] == drawn_numbers[-12] \
               or my_numbers[4] == drawn_numbers[-12] or my_numbers[5] == drawn_numbers[-12]:
                deposite *= 20
                print(f"You won ${deposite}! (x20 multiplier)")
            elif my_numbers[0] == drawn_numbers[-13] or my_numbers[1] == drawn_numbers[-13] \
               or my_numbers[2] == drawn_numbers[-13] or my_numbers[3] == drawn_numbers[-13] \
               or my_numbers[4] == drawn_numbers[-13] or my_numbers[5] == drawn_numbers[-13]:
                deposite *= 25
                print(f"You won ${deposite}! (x25 multiplier)")
            elif my_numbers[0] == drawn_numbers[-14] or my_numbers[1] == drawn_numbers[-14] \
               or my_numbers[2] == drawn_numbers[-14] or my_numbers[3] == drawn_numbers[-14] \
               or my_numbers[4] == drawn_numbers[-14] or my_numbers[5] == drawn_numbers[-14]:
                deposite *= 30
                print(f"You won ${deposite}! (x30 multiplier)")
            elif my_numbers[0] == drawn_numbers[-15] or my_numbers[1] == drawn_numbers[-15] \
               or my_numbers[2] == drawn_numbers[-15] or my_numbers[3] == drawn_numbers[-15] \
               or my_numbers[4] == drawn_numbers[-15] or my_numbers[5] == drawn_numbers[-15]:
                deposite *= 40
                print(f"You won ${deposite}! (x40 multiplier)")
            elif my_numbers[0] == drawn_numbers[-16] or my_numbers[1] == drawn_numbers[-16] \
               or my_numbers[2] == drawn_numbers[-16] or my_numbers[3] == drawn_numbers[-16] \
               or my_numbers[4] == drawn_numbers[-16] or my_numbers[5] == drawn_numbers[-16]:
                deposite *= 50
                print(f"You won ${deposite}! (x50 multiplier)")
            elif my_numbers[0] == drawn_numbers[-17] or my_numbers[1] == drawn_numbers[-17] \
               or my_numbers[2] == drawn_numbers[-17] or my_numbers[3] == drawn_numbers[-17] \
               or my_numbers[4] == drawn_numbers[-17] or my_numbers[5] == drawn_numbers[-17]:
                deposite *= 60
                print(f"You won ${deposite}! (x60 multiplier)")
            elif my_numbers[0] == drawn_numbers[-18] or my_numbers[1] == drawn_numbers[-18] \
               or my_numbers[2] == drawn_numbers[-18] or my_numbers[3] == drawn_numbers[-18] \
               or my_numbers[4] == drawn_numbers[-18] or my_numbers[5] == drawn_numbers[-18]:
                deposite *= 70
                print(f"You won ${deposite}! (x70 multiplier)")
            elif my_numbers[0] == drawn_numbers[-19] or my_numbers[1] == drawn_numbers[-19] \
               or my_numbers[2] == drawn_numbers[-19] or my_numbers[3] == drawn_numbers[-19] \
               or my_numbers[4] == drawn_numbers[-19] or my_numbers[5] == drawn_numbers[-19]:
                deposite *= 80
                print(f"You won ${deposite}! (x80 multiplier)")
            elif my_numbers[0] == drawn_numbers[-20] or my_numbers[1] == drawn_numbers[-20] \
               or my_numbers[2] == drawn_numbers[-20] or my_numbers[3] == drawn_numbers[-20] \
               or my_numbers[4] == drawn_numbers[-20] or my_numbers[5] == drawn_numbers[-20]:
                deposite *= 90
                print(f"You won ${deposite}! (x90 multiplier)")
            elif my_numbers[0] == drawn_numbers[-21] or my_numbers[1] == drawn_numbers[-21] \
               or my_numbers[2] == drawn_numbers[-21] or my_numbers[3] == drawn_numbers[-21] \
               or my_numbers[4] == drawn_numbers[-21] or my_numbers[5] == drawn_numbers[-21]:
                deposite *= 100
                print(f"You won ${deposite}! (x100 multiplier)")
            elif my_numbers[0] == drawn_numbers[-22] or my_numbers[1] == drawn_numbers[-22] \
               or my_numbers[2] == drawn_numbers[-22] or my_numbers[3] == drawn_numbers[-22] \
               or my_numbers[4] == drawn_numbers[-22] or my_numbers[5] == drawn_numbers[-22]:
                deposite *= 150
                print(f"You won ${deposite}! (x150 multiplier)")
            elif my_numbers[0] == drawn_numbers[-23] or my_numbers[1] == drawn_numbers[-23] \
               or my_numbers[2] == drawn_numbers[-23] or my_numbers[3] == drawn_numbers[-23] \
               or my_numbers[4] == drawn_numbers[-23] or my_numbers[5] == drawn_numbers[-23]:
                deposite *= 200
                print(f"You won ${deposite}! (x200 multiplier)")
            elif my_numbers[0] == drawn_numbers[-24] or my_numbers[1] == drawn_numbers[-24] \
               or my_numbers[2] == drawn_numbers[-24] or my_numbers[3] == drawn_numbers[-24] \
               or my_numbers[4] == drawn_numbers[-24] or my_numbers[5] == drawn_numbers[-24]:
                deposite *= 300
                print(f"You won ${deposite}! (x300 multiplier)")
            elif my_numbers[0] == drawn_numbers[-25] or my_numbers[1] == drawn_numbers[-25] \
               or my_numbers[2] == drawn_numbers[-25] or my_numbers[3] == drawn_numbers[-25] \
               or my_numbers[4] == drawn_numbers[-25] or my_numbers[5] == drawn_numbers[-25]:
                deposite *= 500
                print(f"You won ${deposite}! (x500 multiplier)")
            elif my_numbers[0] == drawn_numbers[-26] or my_numbers[1] == drawn_numbers[-26] \
               or my_numbers[2] == drawn_numbers[-26] or my_numbers[3] == drawn_numbers[-26] \
               or my_numbers[4] == drawn_numbers[-26] or my_numbers[5] == drawn_numbers[-26]:
                deposite *= 1000
                print(f"You won ${deposite}! (x1000 multiplier)")
            elif my_numbers[0] == drawn_numbers[-27] or my_numbers[1] == drawn_numbers[-27] \
               or my_numbers[2] == drawn_numbers[-27] or my_numbers[3] == drawn_numbers[-27] \
               or my_numbers[4] == drawn_numbers[-27] or my_numbers[5] == drawn_numbers[-27]:
                deposite *= 2500
                print(f"You won ${deposite}! (x2500 multiplier)")
            elif my_numbers[0] == drawn_numbers[-28] or my_numbers[1] == drawn_numbers[-28] \
               or my_numbers[2] == drawn_numbers[-28] or my_numbers[3] == drawn_numbers[-28] \
               or my_numbers[4] == drawn_numbers[-28] or my_numbers[5] == drawn_numbers[-28]:
                deposite *= 5000
                print(f"You won ${deposite}! (x5000 multiplier)")
            elif my_numbers[0] == drawn_numbers[-29] or my_numbers[1] == drawn_numbers[-29] \
               or my_numbers[2] == drawn_numbers[-29] or my_numbers[3] == drawn_numbers[-29] \
               or my_numbers[4] == drawn_numbers[-29] or my_numbers[5] == drawn_numbers[-29]:
                deposite *= 7500
                print(f"You won ${deposite}! (x7500 multiplier)")
            elif my_numbers[0] == drawn_numbers[-30] or my_numbers[1] == drawn_numbers[-30] \
               or my_numbers[2] == drawn_numbers[-30] or my_numbers[3] == drawn_numbers[-30] \
               or my_numbers[4] == drawn_numbers[-30] or my_numbers[5] == drawn_numbers[-30]:
                deposite *= 10000
                print(f"You won ${deposite}! (x10000 multiplier)")
            else:
                print("Not possible!")


            
        elif percentage_matched == 0:
            print("\nYou are a lucky loser!")
            deposite *= 1500
            print(f"You won ${deposite}! (x1500 multiplier)")
            
        else:
            print("\nBetter luck next time!")
            
        input("\nPress Enter to exit..")
        exit()
    
    elif start_game == "n":
        input("Press Enter to exit..")
        exit()
        
    else:
        print("Please Enter \"y\" or \"n\".")
