import pandas as pd

test_data = [["Beaford"], ["Bridgerule"], ["Bradworthy"]]

df = pd.DataFrame(test_data, columns=["Product Name"])
print(df)
