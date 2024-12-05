def TowerOfHanoi(n, from_rod, to_rod, aux_rod):
    if n == 1:
        print(f"Move disk 1 from {from_rod} to {to_rod}")
        return

    TowerOfHanoi(n-1, from_rod, aux_rod, to_rod)
    
    print(f"Move disk {n} from {from_rod} to {to_rod}")
    
    TowerOfHanoi(n-1, aux_rod, to_rod, from_rod)

if __name__ == "__main__":
    n = 3 
    TowerOfHanoi(n, 'A', 'C', 'B')  
