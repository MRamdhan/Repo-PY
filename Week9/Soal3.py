import array as arr

kamar = arr.array('u', [])
for i in range(10):
    if i + 1 in [2, 4, 7, 9]:
        kamar.insert(i, 'O')
    else:
        kamar.insert(i, 'X')

print("Sebelum dirobohkan:", kamar)

while len(kamar) > 0:
    kamar.pop()

print("Setelah dirobohkan:", kamar)
