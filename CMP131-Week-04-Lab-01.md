# CMP 131 – Python Programming


> **Required file location:** Keep every Python file directly in the repository root. Do not create a `src` folder.

## Week 4 – Lab 1: Box Office Report and Interest Earned

### Learning Objectives

After completing this lab, students should be able to:

* Create and run Python programs that accept user input.
* Store text and numeric information in variables.
* Convert user input to the appropriate numeric data type.
* Perform arithmetic calculations using Python.
* Apply percentages in calculations.
* Use a mathematical formula to calculate compound interest.
* Format monetary values to two decimal places.
* Organize program output using headings, labels, and spacing.
* Test programs using specific input values.
* Follow the required file and folder organization.

## Assignment Overview

In this lab, you will create two separate Python programs.

The first program will prepare a box office report for a movie theater. It will calculate ticket revenue and determine how much money the theater keeps.

The second program will calculate the interest earned on an account during one year when the interest is compounded multiple times.

The two programs must be saved in separate Python files:

* `box_office_report.py`
* `interest_earned.py`

Both programs must accept information from the user, perform the required calculations, and display the results in a clear and organized format.

The instructor is not providing completed Python code or an exact output design. Students must design and write their own programs.

# Program 1: Box Office Report

## Program Description

A movie theater charges different ticket prices for adults and children.

Use the following ticket prices:

* Adult ticket: $10.00
* Child ticket: $6.00

The theater does not keep all the money collected from ticket sales. The theater keeps 20% of the gross box office revenue. The remaining 80% is paid to the movie distributor.

Create a Python program that asks the user for the movie title and the number of adult and child tickets sold.

The program must calculate and display a complete box office report.

## Required Python File

Create a Python file named:

`box_office_report.py`

Include a comment header at the beginning of the file containing:

* Student name
* Course number
* Week number
* Lab number
* Assignment title
* Date

## Part 1: User Input

Ask the user to enter:

* Movie title
* Number of adult tickets sold
* Number of child tickets sold

Store each response in an appropriately named variable.

The movie title must be stored as text.

The numbers of adult and child tickets must be converted to an appropriate numeric data type before they are used in calculations.

## Part 2: Box Office Calculations

Use the ticket prices provided in the assignment to calculate:

* Revenue from adult ticket sales
* Revenue from child ticket sales
* Total gross box office revenue
* Amount kept by the theater
* Amount paid to the movie distributor

Use the following information:

* Adult ticket revenue equals the number of adult tickets multiplied by $10.00.
* Child ticket revenue equals the number of child tickets multiplied by $6.00.
* Gross box office revenue is the total revenue from all adult and child tickets.
* The theater keeps 20% of the gross box office revenue.
* The distributor receives the remaining 80%.

The amount kept by the theater and the amount paid to the distributor must add up to the total gross box office revenue.

## Part 3: Box Office Report

Display a clearly labeled box office report.

The report must include:

* Movie title
* Number of adult tickets sold
* Number of child tickets sold
* Adult ticket revenue
* Child ticket revenue
* Gross box office revenue
* Amount kept by the theater
* Amount paid to the distributor

All monetary values must:

* Include a dollar sign.
* Display exactly two digits after the decimal point.
* Include a clear label.

## Part 4: Output Formatting

Format the report so that it is neat and easy to read.

The output must include:

* A descriptive report title.
* The name of the movie.
* Clear labels for every value.
* Blank lines between major sections.
* Consistent capitalization and spacing.
* Decorative characters that separate sections.
* Monetary values formatted to two decimal places.

Possible decorative characters include:

* Equal signs
* Hyphens
* Asterisks
* Number signs

Students should create their own output layout. Do not copy an output design from another student or ask an AI tool to generate the completed report.

## Required Test Values for Program 1

Test the program using the following information:

* Movie title: `The Midnight Adventure`
* Adult tickets sold: `120`
* Child tickets sold: `80`

Run the program and confirm that:

* The adult ticket revenue is calculated correctly.
* The child ticket revenue is calculated correctly.
* The gross revenue includes both ticket categories.
* The theater keeps exactly 20% of the gross revenue.
* The distributor receives the remaining 80%.
* All monetary values display two decimal places.

# Program 2: Interest Earned

## Program Description

Create a second Python program that calculates the interest earned on a savings account during one year.

The account uses compound interest. This means that interest is added to the account more than once during the year, depending on the number of compounding periods.

The program must ask the user for the principal amount, the annual interest rate, and the number of times the interest is compounded during the year.

## Required Python File

Create a Python file named:

`interest_earned.py`

Include a comment header at the beginning of the file containing:

* Student name
* Course number
* Week number
* Lab number
* Assignment title
* Date

## Part 1: User Input

Ask the user to enter:

* Principal amount originally deposited
* Annual interest rate as a percentage
* Number of times the interest is compounded during the year

Examples of compounding periods include:

* Once per year: `1`
* Quarterly: `4`
* Monthly: `12`
* Daily: `365`

The principal and interest rate may contain decimal values.

The number of compounding periods must be stored as a whole number.

Convert all numeric input to the appropriate data type before performing calculations.

## Part 2: Convert the Interest Rate

The user will enter the interest rate as a percentage.

For example, the user may enter:

`5`

This represents an annual interest rate of 5%.

Before using the interest rate in the compound-interest formula, convert the percentage to decimal form.

For example:

* 5% becomes 0.05.
* 4.5% becomes 0.045.

## Part 3: Calculate the Final Account Balance

Use the following compound-interest formula:

**Final amount = Principal × (1 + Rate ÷ Number of compounding periods) raised to the Number of compounding periods**

The values represent:

* **Principal:** The amount originally deposited.
* **Rate:** The annual interest rate written as a decimal.
* **Number of compounding periods:** The number of times interest is added during the year.
* **Final amount:** The account balance after one year.

Use Python’s exponent operator when raising a value to a power.

## Part 4: Calculate the Interest Earned

After calculating the final account balance, calculate the total interest earned.

Use the following relationship:

**Interest earned = Final amount − Principal**

The interest earned should represent only the additional money added to the account during the year.

## Part 5: Interest Report

Display a clearly labeled interest report containing:

* Original principal
* Annual interest rate
* Number of compounding periods
* Interest earned during the year
* Final account balance after one year

The annual interest rate should display as a percentage.

All monetary values must:

* Include a dollar sign.
* Display exactly two digits after the decimal point.
* Include a clear label.

## Part 6: Output Formatting

Format the report so that it is neat and easy to read.

The output must include:

* A descriptive report title.
* Clear labels for all information.
* Blank lines between major sections.
* Consistent capitalization and spacing.
* Decorative characters that separate sections.
* Monetary values formatted to two decimal places.
* The annual interest rate displayed with a percent sign.

Students should design their own output layout. The instructor is not providing a completed program or exact output design.

## Required Test Values for Program 2

Test the program using the following information:

* Principal amount: `$1,000.00`
* Annual interest rate: `5`
* Number of compounding periods: `12`

The value `5` represents an annual interest rate of 5%.

Run the program and confirm that:

* The interest percentage is converted correctly.
* Monthly compounding uses 12 compounding periods.
* The compound-interest formula is applied correctly.
* The interest earned is the final balance minus the original principal.
* All monetary values display two decimal places.

# Functional Requirements

When the two programs run, they must:

* Ask the user for all required information.
* Store the information in appropriately named variables.
* Convert numeric input to the correct data type.
* Perform all required calculations.
* Display descriptive report titles.
* Display clear labels for every result.
* Format all monetary values to two decimal places.
* Use appropriate spacing and decorative characters.
* Run completely without errors.

The `box_office_report.py` program must:

* Calculate adult ticket revenue.
* Calculate child ticket revenue.
* Calculate total gross box office revenue.
* Calculate the theater’s 20% share.
* Calculate the distributor’s 80% share.
* Display a complete box office report.

The `interest_earned.py` program must:

* Convert the annual interest percentage to decimal form.
* Apply the compound-interest formula.
* Calculate the interest earned.
* Calculate the final account balance.
* Display a complete interest report.

# General Requirements

* Use Python to complete the assignment.
* Save the programs as `box_office_report.py` and `interest_earned.py`.
* Write the two programs separately.
* Use appropriate variables for all input and calculations.
* Use meaningful and consistent variable names.
* Convert user input to the required data type.
* Include the required comment header in both files.
* Format monetary values to two decimal places.
* Use clear prompts, headings, and labels.
* Check spelling, capitalization, grammar, and punctuation.
* Test both programs using the required test values.
* Make sure both programs run without errors.
* Follow the course AI-use policy.
* Record any AI assistance in `AI-Use-Report.md`.

# Required Organization

Organize the assignment as follows:

* `Week-04`

  * `Lab-01`

    * `CMP131-Week-04-Lab-0.md1.md`
    * `AI-Use-Report.md`
    * `src`

      * `box_office_report.py`
      * `interest_earned.py`

# Submission Requirements

Submit or push the complete `Lab-01` folder.

The submission must include:

* `box_office_report.py`
* `interest_earned.py`
* `AI-Use-Report.md`

Before submitting, verify that:

* Both required Python files are included.
* Both filenames are correct.
* Both programs contain complete comment headers.
* Both programs accept the required user input.
* Numeric input is converted to an appropriate data type.
* All calculations are correct.
* Monetary values are formatted to two decimal places.
* Both programs use clear headings and labels.
* Both programs were tested using the required test values.
* Both programs run without errors.
* The AI-use report is complete.
* The latest work has been committed and pushed to GitHub.

# Suggested Git Commit Messages

* Create Week 4 Lab 1 Python files
* Add box office user input
* Complete box office calculations
* Add compound interest user input
* Complete interest calculations
* Improve report formatting
* Test both Week 4 programs
* Complete Week 4 Python lab

---

## GitHub Starter Repository

Use the following public starter repository:

[CMP131-Week-04-Lab-01](https://github.com/ahedhli12/CMP131-Week-04-Lab-01)

### Getting Started

1. Open the starter repository using the link above.
2. If **Use this template** is available, select **Use this template → Create a new repository**.
3. Choose your personal GitHub account as the owner.
4. Name your repository `LastName-FirstName-CMP131-Week-04-Lab-01`.
5. Set your repository to **Public**.
6. Clone your own newly created repository—not the instructor’s starter repository.
7. Open the entire cloned folder in Visual Studio Code.
8. Complete and test every required Python file.
9. Commit and push your work to GitHub.
10. Verify that your latest files appear on GitHub.
11. Complete `AI-Use-Report.md`.
12. Submit the required work through Blackboard Ultra and include your public repository link when requested.

### Required Repository Files

- `CMP131-Week-04-Lab-01.md`
- `AI-Use-Policy.md`
- `AI-Use-Report.md`
- `box_office_report.py`
- `interest_earned.py`

### Before You Submit

- [ ] All required Python files are in the repository root.
- [ ] Every required filename is exact.
- [ ] Each program runs successfully.
- [ ] Required tests and screenshots are complete.
- [ ] `AI-Use-Report.md` is complete and accurate.
- [ ] The latest commit is visible on GitHub.
