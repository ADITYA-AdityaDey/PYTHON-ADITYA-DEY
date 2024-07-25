def check_user_input(input):
    try:
        # Convert it into integer
        val = int(input)
        print("INPUT IS AN INTEGER NUMBER. NUMBER = ", val)
    except ValueError:
        try:
            # Convert it into float
            val = float(input)
            print("INPUT IS A FLOAT  NUMBER. NUMBER = ", val)
        except ValueError:
            print("NO.. INPUT IS NOT A NUMBER. IT'S A STRING")


input1 = input("ENTER YOUR AGE : ")
check_user_input(input1)

input2 = input("ENTER ANY NUMBER : ")
check_user_input(input2)

input2 = input("ENTER THE LAST NUMBER : ")
check_user_input(input2)
