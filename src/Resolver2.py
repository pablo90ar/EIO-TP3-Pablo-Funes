# # Import all classes of PuLP module
from pulp import LpVariable, LpProblem, LpMinimize, makeDict, LpBinary, lpSum

workers = [1, 2, 3, 4]
jobs = [1, 2, 3, 4]

# Cost Matrix
costs = [[1, 2, 1, 9],
         [4, 5, 2, 2],
         [7, 3, 9, 3],
         [2, 3, 5, 1]]

prob = LpProblem("Assignment_Problem", LpMinimize)

# The cost data is made into a dictionary
costs = makeDict([workers, jobs], costs, 0)

# Creates a list of tuples containing all the possible assignments
assign = [(w, j) for w in workers for j in jobs]

# A dictionary called 'Vars' is created to contain the referenced variables
value = LpVariable.dicts("Assign", (workers, jobs), 0, None, LpBinary)

# The objective function is added to 'prob' first
prob += (
    lpSum([value[w][j] * costs[w][j] for (w, j) in assign]),
    "Sum_of_Assignment_Costs",
)

# There are row constraints. Each job can be assigned to only one employee.
for j in jobs:
    prob += lpSum(value[w][j] for w in workers) == 1

# There are column constraints. Each employee can be assigned to only one job.
for w in workers:
    prob += lpSum(value[w][j] for j in jobs) == 1

# The problem is solved using PuLP's choice of Solver
prob.solve()

# Print the variables optimized value
for v in prob.variables():
    print(v.name, "=", v.varValue)

# The optimised objective function value is printed to the screen
print("Value of Objective Function = ", value(prob.objective))
