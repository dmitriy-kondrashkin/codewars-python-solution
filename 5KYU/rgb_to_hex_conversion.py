def rgb(r, g, b):
    return f'{max(0, min(r, 255)):02x}{max(0, min(g, 255)):02x}{max(0, min(b, 255)):02x}'.upper()

# rgb(255, 255, 255)    # returns FFFFFF
# rgb(255, 255, 300)    # returns FFFFFF
# rgb(0,0,0)            # returns 000000
# rgb(148, 0, 211)      # returns 9400D3


r, g, b = -20, 275, 130
print(rgb(r, g, b))
