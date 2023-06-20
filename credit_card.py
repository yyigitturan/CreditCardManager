class CreditCard:
    """A consumer credit card."""
    
    def __init__(self, customer, bank, acnt, limit):
        """Create a new credit card instance.
        
        The initial balance is zero.
        
        customer -- the name of the customer
        bank -- the name of the bank
        acnt -- the account identifier
        limit -- credit limit (measured in dollars)
        """
        self._customer = customer
        self._bank = bank 
        self._account = acnt
        self._limit = limit
        self._balance = 0
        self._transaction_history = []  # Initialize an empty list for transaction history
        
    def get_customer(self):
        """Return name of the customer and print it."""
        print("Customer:", self._customer)
        return self._customer
    
    def get_bank(self):
        """Return the bank's name and print it."""
        print("Bank:", self._bank)
        return self._bank

    def get_account(self):
        """Return the card identifying number (typically stored as a string) and print it."""
        print("Account:", self._account)
        return self._account

    def get_limit(self):
        """Return current credit limit and print it."""
        print("Credit Limit:", self._limit)
        return self._limit

    def get_balance(self):
        """Return current balance and print it."""
        print("Current Balance:", self._balance)
        return self._balance
    
    def charge(self, price):
        """Charge given price to card, assuming sufficient credit limit.
        
        Return True if charge was processed; False if charge was denied.
        """
        if price + self._balance > self._limit:
            return False
        else:
            self._balance += price
            self._transaction_history.append(('Charge', price))
            return True
        
    def make_payment(self, amount):
        """Process customer payment that reduces balance."""
        self._balance -= amount  
        self._transaction_history.append(('Payment', amount))

    def get_transaction_history(self):
        """Print the transaction history and current balance."""
        print("Transaction History:")
        for transaction_type, amount in self._transaction_history:
            print(f"{transaction_type}: ${amount}")
        print("Current Balance:", self._balance)
            

# Create a CreditCard instance
cc = CreditCard("Michael", "YGT Bank", "5391 0375 9387 5309", 1000)

# Get and print the customer information
cc.get_customer()
cc.get_bank()
cc.get_account()
cc.get_limit()
cc.get_balance()

# Perform a transaction of 500 units
cc.charge(500)

# Get and print the updated balance
cc.get_balance()

# Make a payment of 200 units
cc.make_payment(200)

# Get and print the updated balance
cc.get_balance()

# Print the transaction history and current balance
cc.get_transaction_history()
