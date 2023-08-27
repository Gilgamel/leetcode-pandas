import pandas as pd

def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:

    # create empty list to add data
    rearranged_rows = []

    # loop

    for i, row in products.iterrows():
        product_id = row['product_id']

        for store_col in ['store1', 'store2', 'store3']:
            price = row[store_col]
            if pd.notna(price):
                rearranged_rows.append((product_id, store_col, price))

    result = pd.DataFrame(rearranged_rows, columns = ['product_id', 'store', 'price'])

    return result


# Another way to do it, use pd.melt()
# products.melt( ..... ) function lets you unpivot the table (go from wide to long)

def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    
    # Saves output in new DataFrame
    result = (
        # use .melt() to unpivot the table
        products.melt(
            # col that wants to keep
            id_vars = ['product_id'],
            # col that wants to unpivot
            value_vars = ['store1', 'store2', 'store3'], 
            # name store col
            var_name = 'store',
            # name price col
            value_name = 'price'
            )
        # drop na values
        .dropna() 
    )

    return result