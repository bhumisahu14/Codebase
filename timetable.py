
days = int(input("Enter number of days: "))
periods = int(input("Enter periods per day: "))

subjects = {}
remaining = {}

n = int(input("Enter number of subjects: "))

for i in range(n):
    name = input("Enter subject name: ")
    count = int(input("Enter periods for " + name + ": "))
    subjects[name] = count
    remaining[name] = count

total = sum(subjects.values())

if days <= 0 or periods <= 0:
    print("Error: Enter positive numbers")

elif total != days * periods:
    print("Error: Total weekly periods must be equal to available slots")

elif max(subjects.values()) > days * 2:
    print("Error: Timetable cannot be generated. Subject needs more than 2 periods per day")

else:
    timetable = {}
    day_names = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]

    for d in range(days):
        day = day_names[d]
        timetable[day] = []
        count = {}

        for p in range(periods):
            available = []

            for s in subjects:
                if remaining[s] > 0 and count.get(s, 0) < 2:
                    available.append(s)

            if not available:
                break

            subject = max(available, key=lambda x: remaining[x])

            timetable[day].append(subject)
            remaining[subject] -= 1
            count[subject] = count.get(subject, 0) + 1

    print("\nWEEKLY CLASS TIMETABLE")

    for day in timetable:
        print(day, ":", ", ".join(timetable[day]))
