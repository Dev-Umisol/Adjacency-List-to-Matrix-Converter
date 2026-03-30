def adjacency_list_to_matrix(adj_list_dict):
    """
    Implementing a adjacency list to adjacency matrix converter to gain a better understanding of nodes
    Args: adj_list_dict: Takes in a dictionary and converts it to a matrix
    Return: adj_matrix
    """
    
    num_nodes = len(adj_list_dict) # Size of matrix = num of nodes
    adj_matrix = [[0 for col in range(num_nodes)] for row in range(num_nodes)] # Creating matrix
    
    for k, v in adj_list_dict.items():
        for neighbor in adj_list_dict[k]: # For each adjacent node, mark the matrix
            adj_matrix[k][neighbor] = 1
    
    for lst in adj_matrix:
        print(f"{lst}") # Print each inner loop
            
    return adj_matrix

# --> Example Usage <--
adjacency_list_to_matrix({0: [2], 1: [2, 3], 2: [0, 1, 3], 3: [1, 2]})
adjacency_list_to_matrix({0: [1, 2], 1: [2], 2: [0, 3], 3: [2]})
adjacency_list_to_matrix({0: [1], 1: [0]})
adjacency_list_to_matrix({0: [], 1: [], 2: []})