#

def get_hamming_distance(dna1, dna2):
    if len(dna1) != len(dna2):
        raise ValueError("DNA strings must have equal length")
    
    return sum(c1 != c2 for c1, c2 in zip(dna1, dna2))

def get_dna_complement(dna):
    complement_dict = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join(complement_dict.get(base, base) for base in reversed(dna))

#Main Menu Program
def main():
    while True:
        print("Menu:")
        print("1-Hamming Distance")
        print("2-Dna Complement")
        print("3-Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            dna1 = input("Enter the first DNA string: ")
            dna2 = input("Enter the second DNA string: ")
            try:
                distance = get_hamming_distance(dna1, dna2)
                print(f"Hamming Distance: {distance}")
            except ValueError as e:
                print(e)
        elif choice == '2':
            dna = input("Enter the DNA string: ")
            complement = get_dna_complement(dna)
            print(f"DNA Complement: {complement}")
        elif choice == '3':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please choose a valid option.")