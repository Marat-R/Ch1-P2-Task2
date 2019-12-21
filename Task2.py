N = input("Students: ")
K = input("Apples: ")

X = int(K) // int(N)
Z = int(K) % int(N)

print("Each student will get " + str(X) + " apples, " + str(Z) + " apples will remain")