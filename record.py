with open("best_score.txt", 'w', encoding = "UTF-8") as file:
    file.write(str(100))
with open("best_score.txt", 'r', encoding = "UTF-8") as file:
    print(int(file.read()))
    