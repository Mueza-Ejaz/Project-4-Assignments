# Problem Statement:
# Fill out the subtract_seven helper function to subtract 7 from num, and fill out the main() method to call the subtract_seven helper function! If you're stuck, revisit the add_five example from lecture.


# This function will subtract 7 from every number the user enters.
def subtract_seven(num):
    return num - 7  


def main():
    user_num = int(input("Enter a number: "))
    final_number = subtract_seven(user_num)

    print(f"Result after subtracting 7: {final_number}\n")

main()    

# output1:

# Enter a number: 10
# Result after subtracting 7: 3




