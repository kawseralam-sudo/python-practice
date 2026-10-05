# ============================================================
#              SSC STUDENT RESULT SYSTEM
# ============================================================

# ANSI Colors
RESET = "\033[0m"

BOLD = "\033[1m"

GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
WHITE = "\033[97m"


# ============================================================
# 1. GET GRADE
# ============================================================

def get_grade(marks, full_marks):
    """
    Marks থেকে percentage বের করে Grade return করবে।
    """

    percentage = (marks / full_marks) * 100

    if percentage >= 80:
        return "A+"

    elif percentage >= 70:
        return "A"

    elif percentage >= 60:
        return "A-"

    elif percentage >= 50:
        return "B"

    elif percentage >= 40:
        return "C"

    elif percentage >= 33:
        return "D"

    else:
        return "F"


# ============================================================
# 2. GET GRADE POINT
# ============================================================

def get_grade_point(grade):

    grade_points = {
        "A+": 5.00,
        "A": 4.00,
        "A-": 3.50,
        "B": 3.00,
        "C": 2.00,
        "D": 1.00,
        "F": 0.00
    }

    return grade_points[grade]


# ============================================================
# 3. CHECK PASS / FAIL
# ============================================================

def is_pass(grade):

    if grade == "F":
        return False

    return True


# ============================================================
# 4. CALCULATE GPA
# ============================================================

def calculate_gpa(subjects):

    total_grade_point = 0
    passed_subjects = 0

    for subject in subjects:

        if subject["grade"] != "F":

            total_grade_point += subject["grade_point"]
            passed_subjects += 1

    if passed_subjects == 0:
        return 0.00

    gpa = total_grade_point / passed_subjects

    return min(gpa, 5.00)


# ============================================================
# 5. CHECK OVERALL RESULT
# ============================================================

def get_result(subjects):

    for subject in subjects:

        if subject["grade"] == "F":
            return "FAIL"

    return "PASS"


# ============================================================
# 6. PRINT HEADER
# ============================================================

def print_header(name, roll, registration, board, group, year):

    print()
    print(CYAN + "╔" + "═" * 62 + "╗" + RESET)

    print(
        CYAN + "║" +
        "BANGLADESH EDUCATION BOARD".center(62) +
        "║" + RESET
    )

    print(
        CYAN + "║" +
        f"SSC EXAMINATION {year}".center(62) +
        "║" + RESET
    )

    print(
        CYAN + "║" +
        "RESULT SHEET".center(62) +
        "║" + RESET
    )

    print(CYAN + "╚" + "═" * 62 + "╝" + RESET)

    print()

    print(BOLD + "Name          :" + RESET, name)
    print(BOLD + "Roll          :" + RESET, roll)
    print(BOLD + "Registration  :" + RESET, registration)
    print(BOLD + "Board         :" + RESET, board)
    print(BOLD + "Group         :" + RESET, group)
    print(BOLD + "Year          :" + RESET, year)

    print()


# ============================================================
# 7. PRINT RESULT TABLE
# ============================================================

def print_result_table(subjects):

    print("┌" + "─────────┬" + "──────────────────────────────┬"
          + "───────┬" + "───────┬" + "───────┐")

    print(
        "│ " +
        f"{'Code':<7}" +
        " │ " +
        f"{'Subject Name':<28}" +
        " │ " +
        f"{'Marks':>5}" +
        " │ " +
        f"{'Grade':^5}" +
        " │ " +
        f"{'GP':>5}" +
        " │"
    )

    print("├" + "─────────┼" + "──────────────────────────────┼"
          + "───────┼" + "───────┼" + "───────┤")

    for subject in subjects:

        code = subject["code"]
        name = subject["name"]
        marks = subject["marks"]
        grade = subject["grade"]
        gp = subject["grade_point"]

        # Grade অনুযায়ী color
        if grade == "F":
            grade_color = RED
        elif grade == "A+":
            grade_color = GREEN
        else:
            grade_color = YELLOW

        print(
            "│ " +
            f"{code:<7}" +
            " │ " +
            f"{name:<28}" +
            " │ " +
            f"{marks:>5}" +
            " │ " +
            grade_color +
            f"{grade:^5}" +
            RESET +
            " │ " +
            f"{gp:>5.2f}" +
            " │"
        )

    print("└" + "─────────┴" + "──────────────────────────────┴"
          + "───────┴" + "───────┴" + "───────┘")


# ============================================================
# 8. PRINT FAILED SUBJECTS
# ============================================================

def print_failed_subjects(subjects):

    failed = []

    for subject in subjects:

        if subject["grade"] == "F":
            failed.append(subject)

    if len(failed) == 0:
        return

    print()
    print(RED + BOLD + "FAILED SUBJECT(S)" + RESET)
    print("-" * 50)

    for subject in failed:

        print(
            RED +
            f"{subject['code']} - "
            f"{subject['name']} - "
            f"{subject['grade']}" +
            RESET
        )


# ============================================================
# 9. MAIN PROGRAM
# ============================================================

def main():

    print()
    print(MAGENTA + BOLD + "==============================================")
    print("          SSC RESULT MANAGEMENT SYSTEM")
    print("==============================================" + RESET)

    # --------------------------------------------------------
    # Student Information
    # --------------------------------------------------------

    name = input("Enter Student Name: ").strip().upper()

    roll = input("Enter Roll Number: ").strip()

    registration = input("Enter Registration Number: ").strip()

    board = input("Enter Board: ").strip().upper()

    group = input("Enter Group: ").strip().upper()

    year = input("Enter Examination Year: ").strip()

    # --------------------------------------------------------
    # Number of Subjects
    # --------------------------------------------------------

    while True:

        try:
            total_subject = int(
                input("Enter Number of Subjects: ")
            )

            if total_subject <= 0:
                print(RED + "Please enter a valid number." + RESET)
                continue

            break

        except ValueError:
            print(RED + "Please enter a number." + RESET)

    # --------------------------------------------------------
    # Subject List
    # --------------------------------------------------------

    subjects = []

    for i in range(total_subject):

        print()
        print(
            BLUE +
            f"------------- SUBJECT {i + 1} -------------" +
            RESET
        )

        code = input("Subject Code: ").strip()

        subject_name = input(
            "Subject Name: "
        ).strip().upper()

        # Full marks
        while True:

            try:
                full_marks = float(
                    input("Full Marks: ")
                )

                if full_marks <= 0:
                    print(
                        RED +
                        "Full marks must be greater than 0." +
                        RESET
                    )
                    continue

                break

            except ValueError:
                print(
                    RED +
                    "Please enter a valid number." +
                    RESET
                )

        # Obtained marks
        while True:

            try:
                marks = float(
                    input("Obtained Marks: ")
                )

                if marks < 0 or marks > full_marks:

                    print(
                        RED +
                        f"Marks must be between 0 and {full_marks:g}." +
                        RESET
                    )

                    continue

                break

            except ValueError:
                print(
                    RED +
                    "Please enter a valid number." +
                    RESET
                )

        # Grade
        grade = get_grade(
            marks,
            full_marks
        )

        # Grade Point
        grade_point = get_grade_point(
            grade
        )

        # Subject information
        subject = {
            "code": code,
            "name": subject_name,
            "full_marks": full_marks,
            "marks": marks,
            "grade": grade,
            "grade_point": grade_point
        }

        subjects.append(subject)

    # --------------------------------------------------------
    # Calculate GPA and Result
    # --------------------------------------------------------

    gpa = calculate_gpa(subjects)

    result = get_result(subjects)

    # --------------------------------------------------------
    # Display Result
    # --------------------------------------------------------

    print_header(
        name,
        roll,
        registration,
        board,
        group,
        year
    )

    print_result_table(subjects)

    # --------------------------------------------------------
    # GPA
    # --------------------------------------------------------

    print()

    print(
        BOLD +
        " " * 25 +
        f"GPA : {gpa:.2f}" +
        RESET
    )

    # --------------------------------------------------------
    # PASS / FAIL
    # --------------------------------------------------------

    if result == "PASS":

        print(
            GREEN +
            BOLD +
            " " * 22 +
            "RESULT : PASS" +
            RESET
        )

    else:

        print(
            RED +
            BOLD +
            " " * 22 +
            "RESULT : FAIL" +
            RESET
        )

    # --------------------------------------------------------
    # Failed Subjects
    # --------------------------------------------------------

    print_failed_subjects(subjects)

    print()


# ============================================================
# PROGRAM START
# ============================================================

if __name__ == "__main__":
    main()