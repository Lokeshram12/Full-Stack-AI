items = [4,5,2,8,9,10]

total=max(item for item in items if item >5)

print(total)  #10

total=min(item for item in items if item >5)

print(total)  #8

total=sum(item for item in items if item >5)

print(total)  #27


def serve_chai():
    yield "Cup 1"
    yield "Cup 2"
    yield "Cup 3"

stall = serve_chai()

for cup in stall:
    print(cup)