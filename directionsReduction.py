# Simple program that will eliminate opposing directions that are adjacent to one another in a list.
# Date: 6-30-21 Dev: Richard C.

def dirReduc(arr):
    hit = 0
    while True:    
        if len(arr) < 2:
            break
        for bi_direction in range(0, len(arr)):
            if "EAST" in arr[bi_direction:bi_direction+2] and "WEST" in arr[bi_direction:bi_direction+2]:
                del arr[bi_direction:bi_direction+2]
                hit = 1
            elif "NORTH" in arr[bi_direction:bi_direction+2] and "SOUTH" in arr[bi_direction:bi_direction+2]:
                del arr[bi_direction:bi_direction+2]
                hit = 1
        
        if hit == 1:    
            hit = 0
            continue
        else:
            break

    return print(arr)

dir_array = ['SOUTH', 'NORTH', 'WEST']
dirReduc(dir_array)