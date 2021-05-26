import csv


def write_into_file(info):
    with open('Student_info.csv', 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)

        if csv_file.tell() == 0:
            writer.writerow(["Name", "Age", "Contact Number", "Email ID"])

        writer.writerow(info)


if __name__ == "__main__":

    condition = True

    while condition:
        stud_info = input("Enter information of the student (in the format Name Age Contact_number Email_ID):")

        separated_stud_info = stud_info.split(' ')

        print("Check the entered information\nName:{} \nAge:{} \nContact number:{} \nE-Mail:{}"
              .format(separated_stud_info[0], separated_stud_info[1], separated_stud_info[2], separated_stud_info[3]))

        info_check = input("Enter yes or no if the information is correct or not:")
        if info_check == "yes":
            write_into_file(separated_stud_info)
            continue_cond = input("Do you want to enter information for another student? (yes/no):")
            if continue_cond == "yes":
                condition = True
            else:
                condition = False
        elif info_check == "no":
            print("\nPlease re-enter the information:\n")
