print("\n" + "Namashkar Sasriyakal Adab , apka swagat hey is manoranchak khel jiska nam hey KBC")
print("please fill your details before entering our contest so we can harass you in future ")
name = input("Enter your name= ")
age = input("Your age= ")
phone_no = input("Your mobile no.= ")
print("so here is your records right, please confirm: ")
print("\n" + 'name=[{0}] | age=[{1}] | no.=[{2}]'.format(name, age, phone_no))
answer = str(input("Please type in yes or no "))
yes = "yes"
if answer == yes:
    print("\n" + "Toh chaliye shuru karte hey", '\N{sun with face}')
else:
    print("\n" + "Thank you so much for wasting our time so here's your payment", '\N{expressionless face}')
    print("     Receipt : ", "\n", "NAME: " + name.upper(), "\n", "balance: [-Rs 10000000] ")
    quit()
print("please choose the category you want to play in by typing the number")
print("1) [Mythology]       2)[Sports]", "\n", "3)[Movies]       4)[General]")
choice = int(input("your choice : "))
print("\n")
if choice == 1:
    print("In the epic Ramayana, with which weapon did Rama finally kill Ravana ?")
    print(" 1)[Marika]  2)[Sushka]", "\n", "3)[Prasvapna]  4)[Brahmastra]")
    print("\n")
    i = int(input("your choice: "))
    if i == 3:
        print("congo didn't thought you will get this one ... anyways you have been rewarded with Rs 10000 do you wanna play again ? ")
        balance = 10000
        j = input("your choice in yes or no")
        if j==yes:
            print("In the epic Mahabharata, who is called Dharmaputra ?")
            print("1)[Arjuna]  2)[Yudhishtira]", "\n", "3)[Bheeshma]  4)[Duryodhana]")
            k = int(input("your choice: "))
            if k == 2:
                print("and you did it again, Rs 50000 has been added to your account:")
                balance=balance+50000
                print("Now we will ask you rapid fire questions and if you can give the correct answer you will get Rs100000")
                print("\n", "Name of the animal, the 10th avatar of Vishnu (Kalki) ride")
                Devadatta = input("The proper name: ").lower()
                Devadattaa="devadatta"
                if Devadatta==Devadattaa:
                    print("cong so here's the next question: ", "\n", "According to Hindu mythology, who killed seven of her children by drowning them in the river?")
                    ganga = input("Just her name: ").lower()
                    gangaa = "ganga"
                    if ganga == gangaa:
                        print("Noice, next question: ", "\n", "Who informed Hanuman that Sita was taken to Lanka by Ravan")
                        sampati = input("your answer: ").lower()

                        sampatiii = "sampati"
                        if sampati == sampatiii:
                            print("last question then: ", "\n", "Name of the feminine form of Vishnu that helped the devs to get Amrit")
                            mohini = input("Last answer: ").lower()
                            mohinii = "mohini"
                            if mohini == mohinii:
                                print("Congo you have got all the answers correct and Rs 100000 has been added to your account", '\N{military medal}', )
                                balance=balance+100000
                                print("Thank you for playing with us", "\N{kissing face with closed eyes}", "\n", "Hope you liked the game ",  "You can try our other categories as well :"+name, "and you are taking Rs"+balance, "home with you ")
                                quit()
                                
                                

                                
                    
                            

                                    
                        

                                    

                                
                                
                            else:
                                print("you guessed it wrong ", '\N{disappointed face}', "\n", " you have won: Rs"+str(balance), "\n", " Do play with us again")
                                quit()
                        else:
                            print("you guessed it wrong ", '\N{disappointed face}', "\n", " you have won: Rs"+str(balance), "\n", " Do play with us again")
                            quit()
                    else:
                        print("you guessed it wrong ", '\N{disappointed face}', "\n", " you have won: Rs"+str(balance), "\n", " Do play with us again")
                        quit()
                else:
                    print("you guessed it wrong ", '\N{disappointed face}', "\n", " you have won: Rs"+str(balance), "\n", " Do play with us again")
                    quit()
            else :
                print("you guessed it wrong ", '\N{disappointed face}', "\n", " you have won: Rs"+str(balance), "\n", " Do play with us again")
                quit()
        else :
            print("Thank you for playing with us", '\N{sun with face}', '\N{trophy}')
            print(" you have won: Rs"+str(balance), "\n", " Do play with us again")
            quit()
    else:
        print("you guessed it wrong ", '\N{disappointed face}', "\n", " well what are you waiting for you haven't won anything ", '\N{neutral face}', "bye shu shu ..." )
elif choice==2:
    print("Which of the following Indian Sports Team is also known as “The Bhangra Boys?")
    print("1)[Cricket Team]   2)[Hockey Team]", "\n", "3)[Kabaddi Team]  4)[Football Team]", "\n")
    i = input("Enter your choice: ")
    if i==4:
         print("Congo, you guessed it right and you have won Rs10000", "\N{kissing face}", "\n", "so here's the ")
     
    

    

















