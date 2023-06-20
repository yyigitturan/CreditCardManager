class CreditCard:
    """ A consumer credit card."""
    
    def __init__(self, customer, bank, acnt, limit):
        """Creat a new credit cardd instance.
        
        The initial balance is zero.
        
        customer the name of the customer
        bank     the name of the bank
        acnt     the acount identifier
        limit    credit limit (measured in dollars)
        """
        self._customer= customer
        self._bank = bank 
        self._account =  acnt
        self._limit = limit
        self._balance = 0
        self._transaction_history = []  # Initialize an emptylist for transaction history
        
    def get_customer(self):
        """Returnname of the customer."""
        return self._customer
    
    def get_bank(self):
        """Return the bank's name."""
        return self._bank

    def get_account(self):
        """Return the card identifying number (typically stored as a string)."""
        return self._account

    def get_limit(self):
        """Return current credit limit."""
        return self._limit

    def get_balance(self):
        """Return current balance."""
        return self._balance
    
    def charge(self, price):
        """ Charge given price to card, assuming sufficient credit limit.
        
        Return True if charge was processed; False if charge was denied.
        """
        
        if price + self._balance > self._limit:         # if charge would exceed limit, 
            return False                                # cannot accept charge
        else:
            self._balance += price
            return True
        
    def make_payment(self, amount):
        """Process customer payment that reduces balance."""
        self._balance -= amount    

    def get_transaction_history(self):
        """Return the transaction history."""
        return self._transaction_history        
     
cc = CreditCard("Michael", "1st Bank", "5391 0375 9387 5309", 1000)

print(cc.get_customer())  # Get the customer name
print(cc.get_bank())  # Get the bank name
print(cc.get_account())  # Get the account number
print(cc.get_limit())  # Get the credit limit
print(cc.get_balance())  # Get the balance

cc.charge(500)  # Perform a transaction of 500 units

print(cc.get_balance())  # Get the updated balance

cc.make_payment(200)  # Make a payment of 200 units

print(cc.get_balance())  # Get the updated 

print(cc.get_transaction_history())