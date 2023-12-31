# Define the patients with their attributes
patients = [
    {"name": "A", "arrival_time": 0, "treatment_time": 30, "urgency": 3},
    {"name": "B", "arrival_time": 10, "treatment_time": 20, "urgency": 5},
    {"name": "C", "arrival_time": 15, "treatment_time": 40, "urgency": 2},
    {"name": "D", "arrival_time": 20, "treatment_time": 15, "urgency": 4},
]

# Function to calculate waiting time and turnaround time
def calculate_waiting_turnaround_time(patients):
    n = len(patients)
    waiting_time = [0] * n
    turnaround_time = [0] * n

    waiting_time[0] = 0  # First patient has no waiting time

    for i in range(1, n):
        waiting_time[i] = patients[i - 1]["treatment_time"] + waiting_time[i - 1] - patients[i]["arrival_time"]
        waiting_time[i] = max(waiting_time[i], 0)  # Ensure waiting time is non-negative

    for i in range(n):
        turnaround_time[i] = patients[i]["treatment_time"] + waiting_time[i]

    return waiting_time, turnaround_time

# FCFS (First-Come, First-Served) Scheduling
def fcfs_scheduling(patients):
    patients.sort(key=lambda x: x["arrival_time"])
    waiting_time, turnaround_time = calculate_waiting_turnaround_time(patients)
    return waiting_time, turnaround_time

# SJF (Shortest Job First) Scheduling
def sjf_scheduling(patients):
    patients.sort(key=lambda x: (x["arrival_time"], x["treatment_time"]))
    waiting_time, turnaround_time = calculate_waiting_turnaround_time(patients)
    return waiting_time, turnaround_time

# Priority Scheduling
def priority_scheduling(patients):
    patients.sort(key=lambda x: (x["arrival_time"], -x["urgency"]))  # Higher urgency should be scheduled first
    waiting_time, turnaround_time = calculate_waiting_turnaround_time(patients)
    return waiting_time, turnaround_time

# Round Robin Scheduling
def round_robin_scheduling(patients, time_quantum):
    n = len(patients)
    treatment_time_remaining = [p["treatment_time"] for p in patients]
    waiting_time = [0] * n
    turnaround_time = [0] * n
    current_time = 0
    queue = []

    while True:
        for i in range(n):
            if patients[i]["arrival_time"] <= current_time and treatment_time_remaining[i] > 0:
                if treatment_time_remaining[i] <= time_quantum:
                    current_time += treatment_time_remaining[i]
                    turnaround_time[i] = current_time - patients[i]["arrival_time"]
                    treatment_time_remaining[i] = 0
                else:
                    current_time += time_quantum
                    treatment_time_remaining[i] -= time_quantum
                queue.append(i)

        if not queue:
            break

    for i in range(n):
        waiting_time[i] = turnaround_time[i] - patients[i]["treatment_time"]

    return waiting_time, turnaround_time

# Calculate waiting time and turnaround time for each algorithm
fcfs_waiting_time, fcfs_turnaround_time = fcfs_scheduling(patients)
sjf_waiting_time, sjf_turnaround_time = sjf_scheduling(patients)
priority_waiting_time, priority_turnaround_time = priority_scheduling(patients)
rr_waiting_time, rr_turnaround_time = round_robin_scheduling(patients, time_quantum=10)

# Calculate average waiting time for each algorithm
avg_fcfs_waiting_time = sum(fcfs_waiting_time) / len(fcfs_waiting_time)
avg_sjf_waiting_time = sum(sjf_waiting_time) / len(sjf_waiting_time)
avg_priority_waiting_time = sum(priority_waiting_time) / len(priority_waiting_time)
avg_rr_waiting_time = sum(rr_waiting_time) / len(rr_waiting_time)

# Print the results
print("FCFS Scheduling:")
for i, p in enumerate(patients):
    print(f"Patient {p['name']} - Waiting Time: {fcfs_waiting_time[i]}, Turnaround Time: {fcfs_turnaround_time[i]}")
print(f"Average Waiting Time: {avg_fcfs_waiting_time}\n")

print("SJF Scheduling:")
for i, p in enumerate(patients):
    print(f"Patient {p['name']} - Waiting Time: {sjf_waiting_time[i]}, Turnaround Time: {sjf_turnaround_time[i]}")
print(f"Average Waiting Time: {avg_sjf_waiting_time}\n")

print("Priority Scheduling:")
for i, p in enumerate(patients):
    print(f"Patient {p['name']} - Waiting Time: {priority_waiting_time[i]}, Turnaround Time: {priority_turnaround_time[i]}")
print(f"Average Waiting Time: {avg_priority_waiting_time}\n")

print("Round Robin Scheduling:")
for i, p in enumerate(patients):
    print(f"Patient {p['name']} - Waiting Time: {rr_waiting_time[i]}, Turnaround Time: {rr_turnaround_time[i]}")
print(f"Average Waiting Time: {avg_rr_waiting_time}\n")

# Discussion
print("Algorithm Discussion:")
print("FCFS scheduling may lead to longer waiting times for patients with higher urgency.")
print("SJF scheduling may prioritize shorter treatments, which may not be fair for patients with higher urgency.")
print("Priority scheduling may efficiently handle patient urgency.")
print("Round Robin scheduling can ensure fairness and prevent long waiting times, but it may not be the most efficient.")