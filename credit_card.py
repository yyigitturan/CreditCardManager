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
       
class PredatoryCreditCard(CreditCard):
    """An extension to CreditCard that compounds interest and fees."""

    def __init__(self, customer, bank, acnt, limit, apr):
        """Create a new predatory credit card instance.
        
        The initial balance is zero.
        
        customer -- the name of the customer
        bank -- the name of the bank
        acnt -- the account identifier
        limit -- credit limit (measured in dollars)
        apr -- annual percentage rate (e.g., 0.0825 for 8.25% APR)
        """
        super().__init__(customer, bank, acnt, limit)  # call super constructor
        self.apr = apr

    def charge(self, price):
        """Charge given price to the card, assuming sufficient credit limit.
        
        Return True if charge was processed.
        Return False and assess $5 fee if charge is denied.
        """
        success = super().charge(price)  # call inherited method
        if not success:
            self._balance += 5  # assess penalty
        return success  # caller expects return value

    def process_month(self):
        """Assess monthly interest on outstanding balance."""
        if self._balance > 0:
            monthly_factor = pow(1 + self.apr, 1 / 12)
            self._balance *= monthly_factor
            
# Create a PredatoryCreditCard instance
pcc = PredatoryCreditCard("John", "YGT Bank", "5391 0375 9387 5310", 2000, 0.18)

# Perform a transaction of 1500 units
pcc.charge(1500)

# Get and print the updated balance
print("Updated Balance:", pcc.get_balance())

# Make a payment of 500 units
pcc.make_payment(500)

# Get and print the updated balance
print("Updated Balance:", pcc.get_balance())

# Apply monthly interest
pcc.process_month()

# Print the transaction history and current balance
pcc.get_transaction_history()
