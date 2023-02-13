from tabulate import tabulate

all_data = [
        ["System", "CPU", "GPU", "GPU VRAM"],
        ["High-end compute server", "AMD EPYC 7742", "(2x) NVIDIA Tesla V100 (32GB)"],
        ["High-end compute server", "Intel Core i5-11400F", "NVIDIA GTX 1660 SUPER (6GB)"]
]

table = tabulate(all_data, headers="firstrow", tablefmt="latex")
print(table)
