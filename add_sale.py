import sys

main_file = "./bakery.csv"

input_prices = list(map(lambda y: f"{float(y):100.2f}", filter(
    lambda x: x.replace(".", "").isdigit(), sys.argv[1:])))

with open(main_file, "a", encoding="utf-8") as f:
    print(*input_prices, sep="\n", file=f)
