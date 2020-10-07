# Complete the bonAppetit function below.
def bonAppetit(bill, k, b, n):
    t_actual = 0
    for i in range(n):
        if i != k:
            t_actual += bill[i]
    t_actual = t_actual//2
    if t_actual < b:
        print(b - t_actual)
    elif t_actual == b:
        print("Bon Appetit")
