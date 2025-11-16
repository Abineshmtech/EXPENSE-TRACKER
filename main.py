from datetime import date

income = 0
expense = 0
transactions = []

while True:
    print("    🎉 Welcome 🎉   ")
    print("\n🔎 Personal Expense Tracker 🔍")
    print("1. Add Income ")
    print("2. Add Expense ")
    print("3. Show Balance ")
    print("4. Daily Report 🗓")
    print("5. Monthly Report ")
    print("6. Exit 👋")

    choice = input("Enter your choice: ")

    if choice == '1':
        amt = float(input("Enter income amount: ₹"))
        category = input("Enter income category (e.g., Salary ): ")
        transactions.append({
            "type": "income",
            "amount": amt,
            "category": category,
            "date": date.today()
        })
        income += amt
        print(f"✅ Income added for {category}")

    elif choice == '2':
        amt = float(input("Enter expense amount: ₹"))
        category = input("Enter expense category (e.g., Food ): ")
        transactions.append({
            "type": "expense",
            "amount": amt,
            "category": category,
            "date": date.today()
        })
        expense += amt
        print(f" Expense added for {category}")

    elif choice == '3':
        print(f"\nTotal Income  : ₹{income}")
        print(f"Total Expense : ₹{expense}")
        print(f"💵Balance       : ₹{income - expense}")

    elif choice == '4': 
        today = date.today()
        daily_trans = [t for t in transactions if t['date'] == today]
        print(f"\n--- 🗓 Daily Report ({today}) ---")

        if not daily_trans:
            print("No transactions today ")
        else:
            for t in daily_trans:
                print(f"{t['type'].title():8} | ₹{t['amount']} | {t['category']}")
            daily_income = sum(t['amount'] for t in daily_trans if t['type'] == 'income')
            daily_expense = sum(t['amount'] for t in daily_trans if t['type'] == 'expense')
            print(f"👉 Income: ₹{daily_income} | Expense: ₹{daily_expense} | Balance: ₹{daily_income - daily_expense}")

    elif choice == '5':  
        today = date.today()
        monthly_trans = [t for t in transactions if t['date'].month == today.month and t['date'].year == today.year]
        print(f"\n---  Monthly Report ({today.month}/{today.year}) ---")

        if not monthly_trans:
            print("No transactions this month ")
        else:
            for t in monthly_trans:
                print(f"{t['date']} | {t['type'].title():8} | ₹{t['amount']} | {t['category']}")
            monthly_income = sum(t['amount'] for t in monthly_trans if t['type'] == 'income')
            monthly_expense = sum(t['amount'] for t in monthly_trans if t['type'] == 'expense')
            print(f"👉 Income: ₹{monthly_income} | Expense: ₹{monthly_expense} | Balance: ₹{monthly_income - monthly_expense}")

    elif choice == '6':
        print("👋 Thanks for using Personal Expense Tracker! Stay smart with money 💰")
        break

    else:
        print("❌ Invalid choice! Try again.")
