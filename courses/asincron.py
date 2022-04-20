import time


async def sync(x):
    time.sleep(3)
    return x + 1

print('1')
y = sync(2)
print(y)
print('2')
print(y)


