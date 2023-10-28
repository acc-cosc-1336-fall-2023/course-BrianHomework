#
def get_p_distance(list1, list2):
    if len(list1) != len(list2):
        raise ValueError("Sequences must have the same length")

    num_differences = sum(1 for i in range(len(list1)) if list1[i] != list2[i])
    return num_differences / len(list1)

def get_p_distance_matrix(sequences):
    n = len(sequences)
    p_distance_matrix = [[0.0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            p_distance_matrix[i][j] = get_p_distance(sequences[i], sequences[j])

    return p_distance_matrix