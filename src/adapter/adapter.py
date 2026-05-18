# ===================================================================
# ADAPTER PATTERN 
# ===================================================================

# 1. Old Incompatible Class (Existing Code)
class OldPaymentSystem:
    """Old system - uses different method name"""
    def make_payment(self, amount):
        print(f"Old System: Payment of ₹{amount} done successfully!")


# 2. New Desired Interface (What we want to use)
class NewPaymentGateway:
    """New modern interface"""
    def pay(self, amount):
        print(f"New Gateway: Paid ₹{amount} via UPI")


# 3. Adapter - The Bridge
class PaymentAdapter:
    """Adapter makes OldPaymentSystem work like NewPaymentGateway"""
    
    def __init__(self, old_system):
        self.old_system = old_system
    
    def pay(self, amount):          # New method name
        # Convert new call to old method
        self.old_system.make_payment(amount)


# ====================== USAGE ======================
if __name__ == "__main__":
    print("=== Adapter Pattern Demo ===\n")
    
    # Old system
    old_payment = OldPaymentSystem()
    
    # Using Adapter to make old system compatible with new interface
    adapter = PaymentAdapter(old_payment)
    
    # Now we can use modern method name
    adapter.pay(500)
    adapter.pay(1200)