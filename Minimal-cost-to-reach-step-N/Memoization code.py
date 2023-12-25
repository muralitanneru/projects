class Tree:
    def __init__(self):
        self.call: str = ''       # to store keys
        self.returned: Any = None    # to store the returned value for the key
        self.children: List[Tree] = []   # to store the sub calls

def min_cost_climbing_stairs(n, cost, root):
    memo = {}  # Memoization dictionary to store results

    # Recursive function with memoization
    def find_min_cost(i, root):
        root.call = 'find_min_cost(' + str(i) + ')'
        if i < 0:
            root.returned = 0
            return 0
        if i in memo:    # if already computed
            root.returned = memo[i]
            return memo[i]

        # Calculate the minimum cost to reach step i
        child1 = Tree()
        child2 = Tree()
        root.children.append(child1)
        root.children.append(child2)
        dp_i = min(cost[i] + find_min_cost(i - 1, child1), cost[i] + find_min_cost(i - 2, child2))
        memo[i] = dp_i  # Store the result in the memoization dictionary
        root.returned = dp_i
        return dp_i

    # Calculate the minimal cost to reach step n
    return find_min_cost(n, root)

def printTree(tree, indent=''):
    if tree is None or len(tree.children) == 0:
        print(tree.call + ' returned ' + str(tree.returned))
    else:
        print(tree.call + ' returned ' + str(tree.returned))
        for child in tree.children[:-1]:
            print(indent + '|' + '-' * 4, end='')
            printTree(child, indent + '|' + ' ' * 4)
        child = tree.children[-1]
        print(indent + '└' + '-' * 4, end='')
        printTree(child, indent + '  ' * 4)

# Test the function
n = 9
cost_list = [1, 100, 1, 1, 1, 90, 1, 1, 80, 1]  # Example cost list, you can replace it with our own list
root = Tree()
total_cost = min_cost_climbing_stairs(n, cost_list, root)
print("total cost:", total_cost)
printTree(root)
