import time
def main():
    for i in range(10, 0 ,-1):
        print(f"{i}" , end="  " , flush="end")
        time.sleep(1)
    print('Lift off!')
    
    
main()