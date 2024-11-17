# Martian Calendar Problem

In anticipation of traveling to Mars, a **Martian calendar** has been established to account for different orbital and rotational periods on Mars. The period in which Mars rotates once around its axis is called 1 sol.

A Martian year has:
- **669 sols** for leap years, and  
- **668 sols** for non-leap years.  

A year is a leap year if its number is **odd** or divisible by **10**.  
Each year is divided into **24 months**.  
- For each of the four quarters, the first 5 months have **28 sols**.  
- The sixth month has **27 sols**.  
- As an exception, in a leap year, the last month of the fourth quarter has **28 sols**.

As on Earth, the sols are grouped into weeks from **Sunday** to **Saturday** (7 sols each).  

### Date Format
Martian dates are written in the format:
Where:
- `1 ≤ day ≤ 28`,
- `1 ≤ month ≤ 24`,
- `1 ≤ year ≤ 10^9`.

Assume that the **current date** on Mars is:

---

## Input

The first line contains a positive integer \( n \), the number of test cases.  
Each of the next \( n \) lines contains a date in the format:

---

## Output

For each test case, print one line:  
- The **day of the week** that falls on the given date:
  - `0` for Sunday,
  - `1` for Monday,
  - and so on until `6` for Saturday.
- If the given date is not valid, print `-1`.

---

## Example

### Input:
6 28.24.220
1.1.221 
28.3.1611
1.4.1611
1.1.1
28.6.2

### Output:
1 
2
0 
1
1
-1
---

## Notes
- Handle leap years as defined in the problem.
- Validate the Martian date before computing the day of the week.
- If a date is invalid (e.g., `day` exceeds the allowed range for the given `month` or `month > 24`), return `-1`.
- ![image](https://github.com/user-attachments/assets/3d7ea34a-c200-4791-a51c-a49674176d0b)
- ![image](https://github.com/user-attachments/assets/e8584488-0ce2-493b-a9e3-0977f291e7c9)
- ![image](https://github.com/user-attachments/assets/17bc163c-aaaf-41a0-b29a-bff01dc10797)


