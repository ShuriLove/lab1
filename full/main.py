import time, math, os

RED = '\u001b[41m'     
WHITE = '\u001b[47m'   
END = '\u001b[0m'  
CLEAR_CMD = 'cls' if os.name == 'nt' else 'clear'


def swiss_flag(size, delay):
    height = width = 2 * size

    cross_thickness = size // 3
    cross_start = size - cross_thickness // 2
    cross_end = size + cross_thickness // 2

    for row in range(height):
        line = ''
        for col in range(width):
            if (cross_start <= col < cross_end) or (cross_start <= row < cross_end):
                line += f'{WHITE}  {END}'
            else:
                line += f'{RED}  {END}'
        print(line)
        if delay > 0:
            time.sleep(delay)

print('task1:')
print(swiss_flag(size=15, delay=0.05))

def draw_double_ring_pattern(ring_radius, gap, repeat_x, repeat_y):
    H = W = ring_radius * 2 + 1
    block = []
    cx1 = ring_radius                      
    cy1 = ring_radius                       
    cx2 = ring_radius + W + gap             
    cy2 = ring_radius 

    block_width = cx2 + ring_radius + 1     

    for y in range(H):                      
        row_chars = []                      
        for x in range(block_width):        
            d1 = math.hypot(x - cx1, y - cy1)  
            d2 = math.hypot(x - cx2, y - cy2) 
            if abs(d1 - ring_radius) <= 0.7 or abs(d2 - ring_radius) <= 0.7: 
                row_chars.append('O')        
            else:                             
                row_chars.append(' ')        
        block.append(''.join(row_chars)) 

    for _ in range(repeat_y):               
        for line in block:                   
            out_line = (line + ' ' * gap) * repeat_x  
            print(out_line)             
        print()     

print('task2:')
print(draw_double_ring_pattern(ring_radius=4, gap=2, repeat_x=3, repeat_y=2))  

def draw_graph_y_eq_x_over_3(width, height):
    max_x = width                            
    max_y = max_x / 3.0                      

    print('График y = x / 3 (I четверть)')    
    grid = [[' ' for _ in range(max_x + 1)] for _ in range(height)]  

    for x in range(max_x + 1):              
        y = x / 3.0                          
        
        if max_y == 0:                       
            row_idx = height - 1             
        else:                                
            row_idx = height - 1 - int(round(y / max_y * (height - 1)))  # 59
        
        if 0 <= row_idx < height and 0 <= x <= max_x:  
            grid[row_idx][x] = '*'          

    
    for r in range(height):                   
        print(''.join(grid[r]))               

    print('^ Y')                              
    print('+' + '-' * max_x + '> X')         

print('task3:')
print(draw_graph_y_eq_x_over_3(width=30, height=12))

def read_sequence_and_draw_pie(path, bar_width):
    counts = {'in_range': 0, 'out_range': 0}  
    total = 0                                 
    with open(path, 'r', encoding='utf-8') as f:  
        for line in f:      
            s = line.strip()                            
            if s == '':                                 
                continue                                
            else:                                        
                val = float(s)                                                        
            total += 1

            if -3.0 <= val <= 3.0:                     
                counts['in_range'] += 1                
            else:                                      
                counts['out_range'] += 1               

    pct_in = counts['in_range'] / total * 100         
    pct_out = counts['out_range'] / total * 100       

    print(f'Всего чисел: {total}')                     
    print(f'В диапазоне [-3, 3]: {counts['in_range']} ({pct_in:.1f}%)')  
    print(f'Остальные: {counts['out_range']} ({pct_out:.1f}%)')          

    in_blocks = int(round(pct_in / 100 * bar_width))  
    out_blocks = bar_width - in_blocks                

    print('[' + '#' * in_blocks + '-' * out_blocks + ']')  

print('task4:')
print(read_sequence_and_draw_pie(path='sequence.txt', bar_width=40))

def simple_animation_demo(frames, delay=0.6):  
    while True:      
        for frame in frames:                              
            os.system(CLEAR_CMD)                          
            print(frame)                                  
            time.sleep(delay)                             

frame1 = 'FRAME 1\n' + '\n'.join(['  ○    ○  '] * 5)  
frame2 = 'FRAME 2\n' + '\n'.join(['   ○○○   '] * 5)

print('task5:')  
#print(simple_animation_demo([frame1, frame2, frame1], delay=0.6))