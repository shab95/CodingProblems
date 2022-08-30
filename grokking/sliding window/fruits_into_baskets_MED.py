def fruitbasket(fruits):
    window_start = 0
    charHM = {}
    maxFruits = 0
    for window_end in range(len(fruits)):
        curFruit = fruits[window_end]
        if curFruit not in charHM:
            charHM[curFruit] = 0
        charHM[curFruit] += 1
  
        while len(charHM) > 2:
            leftFruit = fruits[window_start]
            charHM[leftFruit] -= 1
            if charHM[leftFruit] == 0:
                del charHM[leftFruit]
            window_start += 1
        maxFruits = max(maxFruits, window_end - window_start + 1)
    return maxFruits

print(str(fruitbasket(['A','B','C','A','C'])))
print(str(fruitbasket(['A','B','C','B', 'B','C'])))        
  