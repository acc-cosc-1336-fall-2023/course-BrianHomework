
# Define a function to calculate Hamming Distance between two DNA strings.
def get_hamming_distance(dna1, dna2):
    # Check if the lengths of the two DNA strings are not equal and raise an exception if so.
    if len(dna1) != len(dna2):
        raise ValueError("DNA strings must have equal length")
    
    # Calculate the Hamming Distance by counting the differing symbols.
    return sum(c1 != c2 for c1, c2 in zip(dna1, dna2))

# Define a function to get the reverse complement of a DNA string.
def get_dna_complement(dna):
    # Create a dictionary mapping DNA bases to their complements.
    complement_dict = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    # Generate the reverse complement by iterating through the DNA string.
    reverse_complement = ''.join(complement_dict.get(base, base) for base in reversed(dna))
    return reverse_complement

# Define a function to check if a string consists of valid DNA bases (A, T, C, G).
def is_valid_dna_string(dna):
    return all(base in 'ACGT' for base in dna)

# Define a function to check if a string is in uppercase.
def is_valid_uppercase_string(string):
    return string.isupper()

# Define the main program.
def main():
    while True:
        print("Menu:")
        print("1-Hamming Distance")
        print("2-DNA Complement")
        print("3-Exit")

        # Prompt the user for their choice and store it in the "choice" variable.
        choice = input("Enter your choice: ")

        # Handle the user's choice.
        if choice == '1':  # If the user chooses option 1 (Hamming Distance):
            while True:
                # Prompt the user for the first DNA string and store it in "dna1".
                dna1 = input("Enter the first DNA string: ")
                # Validate and provide appropriate error messages if needed.
                if not is_valid_uppercase_string(dna1):
                    print("Please make your DNA string uppercase.")
                elif not is_valid_dna_string(dna1):
                    print("Those are not valid DNA strands. DNA is an arrangement of A, C, T, G. Please try again.")
                else:
                    break

            while True:
                # Prompt the user for the second DNA string and store it in "dna2".
                dna2 = input("Enter the second DNA string: ")
                # Validate and provide appropriate error messages if needed.
                if not is_valid_uppercase_string(dna2):
                    print("Please make your DNA string uppercase.")
                elif not is_valid_dna_string(dna2):
                    print("Those are not valid DNA strands. DNA is an arrangement of A, C, T, G. Please try again.")
                elif len(dna1) != len(dna2):
                    print("DNA strings must have equal length, please try again.")
                else:
                    # Calculate and print the Hamming Distance between the two DNA strings.
                    distance = get_hamming_distance(dna1, dna2)
                    print(f"Hamming Distance: {distance}")
                    break

        elif choice == '2':  # If the user chooses option 2 (DNA Complement):
            while True:
                # Prompt the user for a DNA string and store it in "dna".
                dna = input("Enter the DNA string: ")
                # Validate and provide appropriate error messages if needed.
                if not is_valid_uppercase_string(dna):
                    print("Input must be uppercase. Please try again.")
                elif not is_valid_dna_string(dna):
                    print("Input may consist of only DNA which are A, T, C, or G. Please try again.")
                else:
                    # Calculate and print the DNA complement of the input DNA string.
                    complement = get_dna_complement(dna)
                    print(f"DNA Complement: {complement}")
                    break

        elif choice == '3':  # If the user chooses option 3 (Exit):
            print("Exiting program.")
            break

        else:  # If the user enters an invalid choice:
            print("Invalid choice. Please choose a valid option.")

        while True:
            # Ask the user if they want to go back to the menu for another selection.
            restart = input("Would you like to head back to the Menu for another selection? (Y/N): ").strip().lower()
            # Validate the input for variations of 'Y' and 'N', providing error message if needed.
            if restart in ('y', 'yes'):
                break
            elif restart in ('n', 'no'):
                print("Exiting program.")
                exit()
            else:
                print("That input is not a Y or N, please try again.")


