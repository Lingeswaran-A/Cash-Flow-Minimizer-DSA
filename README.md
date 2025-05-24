# 💸 Cash Flow Minimizer

**A Python + Java-based application to minimize cash flow among a group of people by optimizing their debts and payments using a greedy recursive algorithm.**

---

## 🚀 Overview

The **Cash Flow Minimizer** helps groups efficiently settle shared expenses with the **minimum number of transactions**. This is ideal for:

- Splitting bills among roommates or friends
- Settling balances in travel groups or events
- Managing debts in informal or small business setups

Built with:
- 🐍 **Python (Flask)** backend
- ☕ **Java** implementation for CLI or Android integration
- 💡 **Greedy Algorithm + Recursion** for optimal results

---

## 🧠 Key Features

- ✅ Simplifies debts using **net balance calculation**
- ✅ Uses **Greedy Recursive Matching** to minimize transactions
- ✅ Web interface with JSON-based input
- ✅ Java and Python implementations available
- ✅ Scalable and accurate for any number of people

---

## 🧠 Algorithm Used

- **Greedy Recursive Algorithm** for minimizing cash flow
- Computes net balances for each person
- Recursively transfers the minimum possible amount from the max debtor to the max creditor
- Continues until all balances are zero

## ⏱️ Time & Space Complexities

| Operation              | Complexity     |
|------------------------|----------------|
| Net Balance Calculation | O(N²)         |
| Recursive Settlement    | O(N²) (worst) |
| Space Usage             | O(N)          |

## 🚀 Future Enhancements

- Add graph visualization of transactions
- Integrate multi-currency support
- Build Android frontend using Java backend

