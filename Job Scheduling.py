class Job:
    def __init__(self, job_id, deadline, profit):
        self.job_id = job_id
        self.deadline = deadline
        self.profit = profit

def job_scheduling(jobs, n):
    jobs.sort(key=lambda x: x.profit, reverse=True)

    max_deadline = max(job.deadline for job in jobs)

    slots = [-1] * (max_deadline + 1)  # -1 means empty

    total_profit = 0
    job_sequence = []
    for job in jobs:
        for t in range(job.deadline, 0, -1):
            if slots[t] == -1:
                slots[t] = job.job_id
                total_profit += job.profit
                job_sequence.append(job.job_id)
                break

    return job_sequence, total_profit

n = int(input("Enter number of jobs: "))

jobs = []
for i in range(n):
    job_id = input(f"Enter Job ID for job {i+1}: ")
    deadline = int(input(f"Enter deadline for job {i+1}: "))
    profit = int(input(f"Enter profit for job {i+1}: "))
    jobs.append(Job(job_id, deadline, profit))

sequence, profit = job_scheduling(jobs, n)

print("\nSelected Job Sequence:", sequence)
print("Maximum Profit:", profit)
