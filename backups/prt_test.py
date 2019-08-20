import time
for i in range(100001):
    print('\r', '进度:{0}%'.format(i/1000), flush=True)
    time.sleep(0.01)
