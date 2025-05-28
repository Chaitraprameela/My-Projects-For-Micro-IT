import time

def stopwatch():
    print("Simple Stopwatch")
    print("Press ENTER to start. Press Ctrl+C to stop.")
    input()
    start_time = time.time()
    try:
        while True:
            elapsed_time = time.time() - start_time
            print(f"Elapsed Time: {elapsed_time:.2f} seconds", end='\r')
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("\nStopped.")
        final_time = time.time() - start_time
        print(f"Total Time: {final_time:.2f} seconds")

