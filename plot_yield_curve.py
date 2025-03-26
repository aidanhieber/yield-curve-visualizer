import matplotlib.pyplot as plt

def plot_yield_curve(yield_data, date_str=None):
    maturities = list(yield_data.index)
    yields = list(yield_data.values)

    plt.figure(figsize=(10, 6))
    plt.plot(maturities, yields, marker='o')
    plt.title(f"US Treasury Yield Curve {'on ' + date_str if date_str else '(Most Recent)'}")
    plt.xlabel("Maturity")
    plt.ylabel("Yield (%)")
    plt.grid(True)
    plt.show()
