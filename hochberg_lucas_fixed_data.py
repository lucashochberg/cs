# Name: Lucas Hochberg
# Log: 1.0
# Bonus Features: None
# Bugs: None
# Description: Writes high school information data to a csv

fhand = open(r"c:\Users\lhochberg26\Documents\CS Stuff\Computer Science\CS2\student_data_cs2.txt", "r")             # open the input file in read mode
output = open(r"c:\Users\lhochberg26\Documents\CS Stuff\Computer Science\CS2\write_student_data.csv", "w")          # open the output file in write mode

for line in fhand:                                                                                                  # iterate through each line of input file
    id = (line[0:6]).strip()                                                                                        # take characters from lines 0-6 and delete any spaces
    first_name = (line[6:21]).strip()
    last_name = (line[21:36]).strip()
    grade = (line[36:42]).strip()
    gpa = (line[42:48]).strip()
    birthday = (line[48:60]).strip()
    gender = (line[60:67]).strip()
    class_rank = (line[67:76]).strip()
    attend_percent = (line[76:86]).strip()
    honors = (line[86:93]).strip()
    sports = (line[93:102]).strip()
    club_count = (line[102:111]).strip()

    output.write(id + ", " + first_name + ", " + last_name + ", " + grade + ", " + gpa + ", " + birthday + ", " + gender + ", " + class_rank + ", " + attend_percent + ", " + honors + ", " + sports + ", " + club_count + "\n")
    # write each variable to the output file, each on a new line
