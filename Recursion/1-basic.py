count = 0

def greet():
    global count
    if count == 4:
        return
    
    print("rupesh")
    count += 1
    greet()

greet()
