from dictionary import get_p_distance_matrix, get_p_distance
#import dictionary

def is_valid_sequence(sequence):
    valid_chars = {'A', 'C', 'G', 'T'}
    return all(char.upper() in valid_chars for char in sequence)

def get_valid_sequence_count():
    while True:
        n = input("Enter the number of sequences: ")
        if not n.isdigit():
            print("Invalid input. Please enter a number for the 'number of sequences.' ")
        else:
            return int(n)

while True:
    print("\nMenu:")
    print("1- Get p distance matrix")
    print("2- Exit")
    choice = input("Select an option: ")

    if choice == '1':
        n = get_valid_sequence_count()
        sequences = []
        length = None  # Initialize the length variable
        valid_input = False  # Flag to track if the first sequence is valid

        for i in range(n):
            while True:
                sequence = input(f"Enter sequence {i + 1}: ").strip()

                if not is_valid_sequence(sequence):
                    print("Invalid characters in the sequence. Please use only 'A', 'C', 'G', or 'T': ")
                    continue #Ask for input again

                if valid_input and len(sequence) != length:
                    print("The sequences you entered are not the same length. Please try again.")
                    continue #Ask for input again

                if not valid_input:
                        valid_input = True
                        length = len(sequence)

                sequences.append(list(sequence))
                break
        
        distance_matrix = get_p_distance_matrix(sequences)
        print("P-distance matrix is:")
        for row in distance_matrix:
            print(' '.join(f'{distance:.5f}' for distance in row))
    elif choice == '2':
        print("Exiting the program.")
        break
    else:
        print("Invalid option. Please choose 1 or 2.")
    