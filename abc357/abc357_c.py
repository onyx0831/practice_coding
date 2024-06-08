N = int(input())
# grid = [['#' for _ in range(3**N)] for _ in range(3**N)]
def generate_pattern(n):
    if n == 0:
        return ["#"]
    if n == 1:
        return ["###", "#.#", "###"]
    
    # 再帰的に前のパターンを取得
    prev_pattern = generate_pattern(n-1)
    size = len(prev_pattern)
    new_size = size * 3
    new_pattern = [""] * new_size
    
    # 新しいグリッドを構築
    for i in range(new_size):
        if size <= i < 2 * size:
            new_pattern[i] = prev_pattern[i - size] + "." * size + prev_pattern[i - size]
        else:
            new_pattern[i] = prev_pattern[i % size] * 3

    return new_pattern

def print_pattern(n):
    pattern = generate_pattern(n)
    for line in pattern:
        print(line)

print_pattern(N)
