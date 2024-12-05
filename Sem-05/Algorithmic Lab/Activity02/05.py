def tower_of_hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    
    tower_of_hanoi(n - 1, source, auxiliary, target)
    
    print(f"Move disk {n} from {source} to {target}")
    
    tower_of_hanoi(n - 1, auxiliary, target, source)

if __name__ == "__main__":
    n = 3  # Number of disks
    tower_of_hanoi(n, 'A', 'C', 'B')  # Move n disks from rod A to rod C using B as auxiliary
