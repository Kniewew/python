import pandas as pd
a = input("_")
xle = pd.Series([bin(i)[2:] for i in range(0,31)], index=['а','б','в','г','д','е','ё','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ы','э','ю','я'])
print(' '.join(xle[c] for c in a))
