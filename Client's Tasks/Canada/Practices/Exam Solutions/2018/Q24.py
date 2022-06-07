def displayPrices(product):
    print("\n")
    print("%-15s %10s %10s %10s" % ("Product", "Cost", "Wholesale", "Retail"))

    for k, v in product.items():
        print("%-15s %10.2f %10.2f %10.2f" % (k, v[0], v[1], v[2]))

