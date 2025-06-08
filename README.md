# Tracko 

**Tracko** is a lightweight command-line Python app that helps users track daily expenses by adding, listing, and totaling them. Data is stored in a local CSV file and can be accessed or updated anytime.

---

##  Features

| Feature     | Description                                  |
|-------------|----------------------------------------------|
| Add Expense | `add 100 groceries` — adds an expense entry with timestamp |
| View All    | `list` — lists all expenses from the CSV file |
| Get Total   | `total` — shows the total spending amount    |
| Save Data   | All expenses are saved in a local CSV file   |

---

## Technologies Used

- Python 3
- `csv` module (built-in)
- Command-line interface
- GitHub Codespaces

---

##  How to Run

From your terminal inside GitHub Codespaces (or locally):

```bash
python tracker.py add 200 groceries
python tracker.py list
python tracker.py total

 ---