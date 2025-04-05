import sys

def find(gate):
    if gates[gate] == gate:
        return gate
    # gate가 사용중이면 상위 게이트로 가서 있는지 확인
    gates[gate] = find(gates[gate])
    return gates[gate]

def docker(bottom, top):
    root_bottom = find(bottom)
    root_top = find(top)
    gates[root_bottom] = root_top

g = int(sys.stdin.readline().strip())
p = int(sys.stdin.readline().strip())
# 0은 사용 불가능하다는 것을 표시
gates = list(range(g+1))
count = 0
for i in range(p):
    gate = int(sys.stdin.readline().strip())
    root = find(gate) # 어디에 착륙시킬지 찾음
    # 남은 게이트가 없다면 브레이크
    if root == 0:
        break

    # 게이트를 사용했으므로 상위 게이트와 연결
    # 0과 연결된다는 것은 사용불가능함을 나타냄
    docker(root, root-1)
    count += 1
print(count)