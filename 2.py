# Define the processes with their attributes
processes = [
    {"name": "P1", "arrival_time": 0, "burst_time": 24, "priority": 3},
    {"name": "P2", "arrival_time": 4, "burst_time": 3, "priority": 1},
    {"name": "P3", "arrival_time": 5, "burst_time": 3, "priority": 4},
    {"name": "P4", "arrival_time": 6, "burst_time": 12, "priority": 2},
]

# Function to calculate waiting time and turnaround time
def calculate_waiting_turnaround_time(processes):
    n = len(processes)
    waiting_time = [0] * n
    turnaround_time = [0] * n

    waiting_time[0] = 0  # First process has no waiting time

    for i in range(1, n):
        waiting_time[i] = processes[i - 1]["burst_time"] + waiting_time[i - 1] - processes[i]["arrival_time"]
        waiting_time[i] = max(waiting_time[i], 0)  # Ensure waiting time is non-negative

    for i in range(n):
        turnaround_time[i] = processes[i]["burst_time"] + waiting_time[i]

    return waiting_time, turnaround_time

# FCFS (First-Come, First-Served) Scheduling
def fcfs_scheduling(processes):
    processes.sort(key=lambda x: x["arrival_time"])
    waiting_time, turnaround_time = calculate_waiting_turnaround_time(processes)
    return waiting_time, turnaround_time

# SJF (Shortest Job First) Scheduling
def sjf_scheduling(processes):
    processes.sort(key=lambda x: (x["arrival_time"], x["burst_time"]))
    waiting_time, turnaround_time = calculate_waiting_turnaround_time(processes)
    return waiting_time, turnaround_time

# Priority Scheduling
def priority_scheduling(processes):
    processes.sort(key=lambda x: (x["arrival_time"], x["priority"]))
    waiting_time, turnaround_time = calculate_waiting_turnaround_time(processes)
    return waiting_time, turnaround_time

# Round Robin Scheduling
def round_robin_scheduling(processes, time_quantum):
    n = len(processes)
    burst_time_remaining = [p["burst_time"] for p in processes]
    waiting_time = [0] * n
    turnaround_time = [0] * n
    current_time = 0
    queue = []

    while True:
        for i in range(n):
            if processes[i]["arrival_time"] <= current_time and burst_time_remaining[i] > 0:
                if burst_time_remaining[i] <= time_quantum:
                    current_time += burst_time_remaining[i]
                    turnaround_time[i] = current_time - processes[i]["arrival_time"]
                    burst_time_remaining[i] = 0
                else:
                    current_time += time_quantum
                    burst_time_remaining[i] -= time_quantum
                queue.append(i)

        if not queue:
            break

    for i in range(n):
        waiting_time[i] = turnaround_time[i] - processes[i]["burst_time"]

    return waiting_time, turnaround_time

# Calculate waiting time and turnaround time for each algorithm
fcfs_waiting_time, fcfs_turnaround_time = fcfs_scheduling(processes)
sjf_waiting_time, sjf_turnaround_time = sjf_scheduling(processes)
priority_waiting_time, priority_turnaround_time = priority_scheduling(processes)
rr_waiting_time, rr_turnaround_time = round_robin_scheduling(processes, time_quantum=4)

# Calculate average waiting time and average turnaround time for each algorithm
def calculate_average(times):
    return sum(times) / len(times)

avg_fcfs_waiting_time = calculate_average(fcfs_waiting_time)
avg_fcfs_turnaround_time = calculate_average(fcfs_turnaround_time)
avg_sjf_waiting_time = calculate_average(sjf_waiting_time)
avg_sjf_turnaround_time = calculate_average(sjf_turnaround_time)
avg_priority_waiting_time = calculate_average(priority_waiting_time)
avg_priority_turnaround_time = calculate_average(priority_turnaround_time)
avg_rr_waiting_time = calculate_average(rr_waiting_time)
avg_rr_turnaround_time = calculate_average(rr_turnaround_time)

# Print the results
print("FCFS Scheduling:")
for i, p in enumerate(processes):
    print(f"{p['name']} - Waiting Time: {fcfs_waiting_time[i]}, Turnaround Time: {fcfs_turnaround_time[i]}")
print(f"Average Waiting Time: {avg_fcfs_waiting_time}, Average Turnaround Time: {avg_fcfs_turnaround_time}\n")

print("SJF Scheduling:")
for i, p in enumerate(processes):
    print(f"{p['name']} - Waiting Time: {sjf_waiting_time[i]}, Turnaround Time: {sjf_turnaround_time[i]}")
print(f"Average Waiting Time: {avg_sjf_waiting_time}, Average Turnaround Time: {avg_sjf_turnaround_time}\n")

print("Priority Scheduling:")
for i, p in enumerate(processes):
    print(f"{p['name']} - Waiting Time: {priority_waiting_time[i]}, Turnaround Time: {priority_turnaround_time[i]}")
print(f"Average Waiting Time: {avg_priority_waiting_time}, Average Turnaround Time: {avg_priority_turnaround_time}\n")

print("Round Robin Scheduling:")
for i, p in enumerate(processes):
    print(f"{p['name']} - Waiting Time: {rr_waiting_time[i]}, Turnaround Time: {rr_turnaround_time[i]}")
print(f"Average Waiting Time: {avg_rr_waiting_time}, Average Turnaround Time: {avg_rr_turnaround_time}\n")

# Analysis
print("Algorithm Analysis:")
avg_waiting_times = [avg_fcfs_waiting_time, avg_sjf_waiting_time, avg_priority_waiting_time, avg_rr_waiting_time]
avg_turnaround_times = [avg_fcfs_turnaround_time, avg_sjf_turnaround_time, avg_priority_turnaround_time, avg_rr_turnaround_time]

algorithm_names = ["FCFS", "SJF", "Priority", "Round Robin"]
best_waiting_time_algo = algorithm_names[avg_waiting_times.index(min(avg_waiting_times))]
best_turnaround_time_algo = algorithm_names[avg_turnaround_times.index(min(avg_turnaround_times))]

print(f"The best algorithm based on average waiting time is {best_waiting_time_algo}")
print(f"The best algorithm based on average turnaround time is {best_turnaround_time_algo}")