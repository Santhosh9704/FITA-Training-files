
n = int(input("Enter number of semesters: "))

for i in range(1, n + 1):
    s= int(input(f"Enter number of subjects in semester {i}: "))
    for j in range(1,s+1):
    
        marks = list(map(int, input(f"Enter marks for subject {j}: ").split()))
    
    # Validation check
        
        if marks < 0 or marks > 100:
            print("You have entered invalid mark")
            exit()
    
    # Find maximum
    print(f"Maximum mark in {i} semester: {max(marks)}")
