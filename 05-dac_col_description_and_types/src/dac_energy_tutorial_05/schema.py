import pandera as pa
from pandera.typing import Series


class Schema(pa.DataFrameModel):
    source: Series[str] = pa.Field(
        alias="siec_name",
        description="Source of energy",
    )
    location: Series[str] = pa.Field(
        alias="geo",
        description="Location code, either two-digit "
        "ISO 3166-1 alpha-2 code or "
        "'EA19', 'EU27_2020', 'EU28' for the European Union",
    )
    year: Series[int] = pa.Field(
        alias="TIME_PERIOD",
        description="Year of observation",
    )
    value_in_gwh: Series[float] = pa.Field(
        alias="OBS_VALUE",
        description="Gross available energy in GWh",
    )
