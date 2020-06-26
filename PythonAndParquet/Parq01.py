import numpy as np
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

df = pd.DataFrame({'one': [-1, np.nan, 2.5],
                   'two': ['foo', 'bar', 'baz'],
                   'three': [True, False, True]
                   },
                   index=list('abc')
                  )

t = pa.Table.from_pandas(df)
pq.write_table(t, 'ParqFiles\example.parquet')

print(t)

#

# pa.parquet.write_table(table, 'example.parquet')
# table2 = pa.parquet.read_table('example.parquet')