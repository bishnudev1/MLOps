import threading


def numbers():
    for i in range(1, 11):
        print(f"Number: {i}")

def letters():
    for i in range(65, 75):
        print(f"Letter: {chr(i)}")
        
if __name__ == "__main__":
    t1 = threading.Thread(target=numbers)
    t2 = threading.Thread(target=letters)
    
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()
    
    print("Done!")