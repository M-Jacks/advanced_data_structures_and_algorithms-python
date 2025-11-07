# Towers of Hanoi with three pegs
def hanoi_three_pegs(n, peg_start, peg_intermed, peg_dest):
    if n == 1:
        print(f'Move disk 1 from peg {peg_start} to peg {peg_dest}')
        return
    hanoi_three_pegs(n-1, peg_start, peg_dest, peg_intermed)
    print(f'Move disk {n} from peg {peg_start} to peg {peg_dest}')
    hanoi_three_pegs(n-1, peg_intermed, peg_start, peg_dest)   
    
def hanoi3(n, peg_start, peg_intermed, peg_dest):
    if n == 1:
        print('{} -> {}'.format(peg_start, peg_dest))
        return
    hanoi3(n-1, peg_start, peg_dest, peg_intermed)
    print('{} -> {}'.format(peg_start, peg_dest))
    hanoi3(n-1, peg_intermed, peg_start, peg_dest)

    
hanoi_three_pegs(3, 'A', 'B', 'C') 
hanoi3(3, 'A', 'B', 'C')
    
    
# Towers of Hanoi with 4 pegs
def hanoi_four_pegs(n, peg_start, peg_intermed1, peg_intermed2, peg_dest):
    if n == 0:
        return
    if n == 1:
        print(f'Move disk 1 from peg {peg_start} to peg {peg_dest}')
        return
    hanoi_four_pegs(n-2, peg_start, peg_dest, peg_intermed2, peg_intermed1)
    print(f'Move disk {n-1} from peg {peg_start} to peg {peg_intermed2}')
    print(f'Move disk {n} from peg {peg_start} to peg {peg_dest}')
    print(f'Move disk {n-1} from peg {peg_intermed2} to peg {peg_dest}')
    hanoi_four_pegs(n-2, peg_intermed1,  peg_start, peg_intermed2, peg_dest)
    
def hanoi4(n, peg_start, peg_intermed1, peg_intermed2, peg_dest):
    if n == 0:
        return
    if n == 1:
        print('{} -> {}'.format(peg_start, peg_dest))
        return
    hanoi4(n-2, peg_start, peg_dest, peg_intermed2, peg_intermed1)
    print('{} -> {}'.format(peg_start, peg_intermed2))
    print('{} -> {}'.format(peg_start, peg_dest))
    print('{} -> {}'.format(peg_intermed2, peg_dest))
    hanoi4(n-2, peg_intermed1,  peg_start, peg_intermed2, peg_dest)
    
hanoi_four_pegs(4, 'A', 'B', 'C', 'D')
hanoi4(4, 'A', 'B', 'C', 'D')