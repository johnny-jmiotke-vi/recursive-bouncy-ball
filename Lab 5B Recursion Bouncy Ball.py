def calculate_total_distance(initial_height, num_bounces): #outer recursive function occurs, declaring input parameters
    # Stop condition stops function if there are no more bounces
    if num_bounces == 0:
        return initial_height
    
    # Size-n-1 problem (smaller problem) calculates how high ball the bounces after hitting the ground
    bounciness_index = 0.6
    next_height = initial_height * bounciness_index
    
    # Size-n problem calculates the total distance of ball bouncing down and up
    distance_for_bounce = next_height * 2
    
    # Where the recursion occurs the function calls itself again to figure out the remaining distance for next bounce
    remaining_distance = calculate_total_distance(next_height, num_bounces - 1)
    
    # Where the program unwinds the solution, adds everything together & returns the total distance traveled by the ball 
    return initial_height + distance_for_bounce + remaining_distance

# Get user inputs
initial_height = float(input("Enter the initial height in meters from which the ball is dropped: "))
num_bounces = int(input("Enter the number of bounces:"))

# Calculate the total distance traveled by the ball
total_distance = calculate_total_distance(initial_height, num_bounces)

# Print the total distance
print(f"The total distance traveled by the ball is: {total_distance:.1f} meters")