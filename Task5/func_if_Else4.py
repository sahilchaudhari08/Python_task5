#Function 6
# Check if Vehicle Numbers Start with "MH" (for Maharashtra) or Other State

def vehicle(state):
    if state.startswith('MH'):
        return 'Maharashtra State'
    else:
        return 'Other State'
    
vehicle_Num = ("MH49SA8181", "DL02CD5678","KA03EF9012","MH04GH3456","UP05IJ7890","RJ06KL1234","MH07MN5678","TN08OP9012",)

for state in vehicle_Num:
    print('---------------------')
    print(f'vehicle_num = {state}')
    number = vehicle(state)
    print(f'State = {number}')
