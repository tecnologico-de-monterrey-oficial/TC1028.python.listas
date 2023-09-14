# List of tuples
# Each tuple contains a test:
# - the first element are the inputs,
# - the second are the output,
# - and the third is the message in case of an error
# To test another case, add another tuple

input_values = [
    # Test case 1
    (
        ["2","3","1","25","8","30","2","4"],
        ["","","","","","","","","[1, 8, 2, 4]"],
        "Error"
    ),   
    (
        ["2","0"],
        ["","","[]"],
        "Error"
    )
]