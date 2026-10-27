"""Bank account management module."""

import hashlib
import os
import secrets

account_data = {}


def create_account(acc_id, name, initial_deposit=0, transactions=None):
    """Create a new account; return False if the id already exists."""
    if transactions is None:
        transactions = []
    if acc_id in account_data:
        return False
    account_data[acc_id] = {"name": name, "balance": initial_deposit}
    transactions.append(
        f"Created {acc_id} with initial balance {initial_deposit}"
    )
    return True


def deposit(acc_id, amount):
    """Add amount to an account; return False if the account is missing."""
    if acc_id not in account_data:
        return False
    account_data[acc_id]["balance"] += amount
    return True


def withdraw(acc_id, amount):
    """Withdraw amount if the account exists and has enough balance."""
    if account_data.get(acc_id) is None:
        return False
    if account_data[acc_id]["balance"] < amount:
        return False
    account_data[acc_id]["balance"] -= amount
    return True


def compute_bonus(acc_id, rate):
    """Return the bonus for an account as balance * rate."""
    return account_data[acc_id]["balance"] * rate


def get_hash(pin):
    """Return the SHA-256 hash of a PIN."""
    return hashlib.sha256(pin.encode()).hexdigest()


def generate_temp_pin():
    """Return a cryptographically secure 4-digit PIN."""
    return secrets.randbelow(9000) + 1000


def backup_data(filename="backup.txt"):
    """Write account data to a file."""
    with open(filename, "w", encoding="utf-8") as backup_file:
        backup_file.write(str(account_data))
    print("Backup complete:", filename)


def main():
    """Run a small demo of the banking functions."""
    admin_token = os.environ.get("BANK_ADMIN_TOKEN")
    create_account("A01", "Alice", 1000)
    deposit("A01", 500)
    withdraw("A01", 200)
    print("Bonus:", compute_bonus("A01", 0.05))
    print("PIN Hash:", get_hash("1234"))
    print("Temp PIN:", generate_temp_pin())
    backup_data()
    print("Token initialized:", admin_token is not None)


if __name__ == "__main__":
    main()
