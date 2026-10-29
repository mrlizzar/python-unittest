amount = 1000
tax_rate = 0.15

assert amount >= 0, "The amount should be negative"
assert tax_rate > 0 and tax_rate < 1, "The tax_rate should be 0-1"

