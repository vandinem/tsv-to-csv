import sys

for line in sys.stdin.buffer:

    line = line.decode('utf-8', errors='replace')
    
    cleaned = []

    for char in line.encode('utf-8', errors='surrogateescape'):
        if char > 127:
            cleaned.append(b'\\xff')
        else:
            cleaned.append(bytes([char]))
            
    clean_line = b''.join(cleaned).decode('utf-8', errors='replace')
    
    print(clean_line, end="")