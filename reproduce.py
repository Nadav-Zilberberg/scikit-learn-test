import polars as pl
from sklearn.impute import SimpleImputer
import numpy as np

print(
    SimpleImputer(missing_values=np.nan, strategy='constant', fill_value=0)
      .fit(pl.DataFrame({"a": [10]}, schema={"a": pl.Int32}).to_pandas(use_pyarrow_extension_array=False))
      ._fit_dtype
)
# prints dtype('int32'), as expected

print(
    SimpleImputer(missing_values=np.nan, strategy='constant', fill_value=0)
      .fit(pl.DataFrame({"a": [10]}, schema={"a": pl.Int32}).to_pandas(use_pyarrow_extension_array=True))
      ._fit_dtype
)
# prints dtype('float64') (!!)

