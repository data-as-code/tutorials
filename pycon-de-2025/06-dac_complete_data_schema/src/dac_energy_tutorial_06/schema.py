import pandera as pa
from pandera.typing import Series
import pandas as pd
import logging


class Schema(pa.DataFrameModel):
    source: Series[str] = pa.Field(
        isin=[
            "Solid fossil fuels",
            "Manufactured gases",
            "Electricity",
            "Natural gas",
            "Heat",
            "Nuclear heat",
            "Oil and petroleum products (excluding biofuel portion)",
            "Peat and peat products",
            "Renewables and biofuels",
            "Oil shale and oil sands",
            "Total",
            "Non-renewable waste",
        ],
        nullable=False,
        alias="siec_name",
        description="Source of energy",
    )
    location: Series[str] = pa.Field(
        isin=[
            "AL",
            "AT",
            "BA",
            "BE",
            "BG",
            "CY",
            "CZ",
            "DE",
            "DK",
            "EA19",
            "EE",
            "EL",
            "ES",
            "EU27_2020",
            "EU28",
            "FI",
            "FR",
            "GE",
            "HR",
            "HU",
            "IE",
            "IS",
            "IT",
            "LT",
            "LU",
            "LV",
            "MD",
            "ME",
            "MK",
            "MT",
            "NL",
            "NO",
            "PL",
            "PT",
            "RO",
            "RS",
            "SE",
            "SI",
            "SK",
            "TR",
            "UA",
            "UK",
            "XK",
        ],
        nullable=False,
        alias="geo",
        description="Location code, either two-digit ISO 3166-1 alpha-2 code or "
        "'EA19', 'EU27_2020', 'EU28' for the European Union",
    )
    year: Series[int] = pa.Field(
        ge=1990,
        le=3000,
        nullable=False,
        alias="TIME_PERIOD",
        description="Year of observation",
    )
    value_in_gwh: Series[float] = pa.Field(
        nullable=True,
        alias="OBS_VALUE",
        description="Gross available energy in GWh",
    )

    @pa.dataframe_check
    def total_ge_other_sources(cls, df: pd.DataFrame) -> bool:
        df_pivoted = df.pivot(
            index=[cls.location, cls.year],
            columns=cls.source,
            values=cls.value_in_gwh,
        ).reset_index()
        is_check_successful = True
        for col in df[cls.source].unique():
            if col != "Total":
                is_total_smaller = df_pivoted[col] > df_pivoted["Total"]
                if (is_total_smaller).any():
                    relevant_cols = [cls.location, cls.year, "Total", col]
                    logging.error(
                        "Error: {col} is greater than Total in:\n"
                        f"{df_pivoted[is_total_smaller].loc[:, relevant_cols]}"
                    )
                    is_check_successful = False
        return is_check_successful
