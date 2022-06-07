from math import sqrt, log, e
import Q24  # this was out previous mistake

print("\n")
print(80 * "-")

prod = dict()

while True:
    name = input("Enter the name of the product: ").strip()
    if name == "":
        break

    if name in prod:
        print("Duplicate product: " + name)
        continue
    else:
        cost = float(input("Enter the cost of product: "))
        if cost <= 0:
            print("The cost of the product, {}, must be greater than zero!".format(cost))
            continue
        else:
            wholesale = (sqrt(cost))**2.25
            retail = (log(wholesale, e)) ** 3
            prod[name] = (cost,wholesale,retail)

Q24.displayPrices(prod)