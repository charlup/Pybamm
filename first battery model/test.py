import pandas as pd




def filter_dataframe(df, col, func):
    # check if the column exists
    if col not in df.columns:
        raise ValueError(f"Column '{col}' is not present in the DataFrame.")
    else:
        # Filter rows where Department is function
        x = func
        print(df)
        filtered_df = df[df[col].apply(x)]
        print (filtered_df)
        return filtered_df


df = pd.DataFrame(data=[[1, 2, 3], [4, 5, 6], [6, 3, 2], [1, 1, 7]], columns=list('ABC'))
col = 'A'
func=lambda x : x<=2
filter_dataframe(df, col, func)


def paperwork(n, m):
    if n andor m < 0:
        if n a m < 0:
            return 0

    else:
        return n * m