import pandas as pd


class PetDataPrep:
    """Get clean data from the Plotting Efficiency Tool"""

    def __init__(self, devMode=False) -> None:
        self.devMode = devMode

        self.inputs = self.define_inputs()
        self.site_efficiency_columns = self.define_site_efficiency_columns()

        self.outputs = {}

    def define_inputs(self):
        return {
            "site efficiency": (
                "__test__/test_data.csv"
                if self.devMode
                else xl("Site_efficiency", headers=True)
            ),
            "house types": (
                "__test__/ht_data.csv"
                if self.devMode
                else xl("House_Type_Database", headers=True)
            ),
            "plotting formats": (
                "__test__/plotting_vars.csv"
                if self.devMode
                else xl("plotting_format", headers=True)
            ),
            "parking formats": (
                "__test__/parking_vars.csv"
                if self.devMode
                else xl("Parking_format", headers=True)
            ),
        }

    def define_site_efficiency_columns(self):
        return map(
            lambda column_name: column_name.strip().lower().replace(" ", "_"),
            [
                "Product name",
                "House type code",
                "Number houses or apartment blocks plotted",
                "Plotting format",
                "Parking format",
                "Theoretical coverage based on total land take (ft²/acre)",
                "Dwelling structures abnormals:  £/plot",
                "Dwelling structure cost / house plot or apartment block                                                                                                         (NB standard parking costs entered in House Type Database tab)",
                "Residual  value after plot build cost, CIL and contribution to profit per house or apartment block",
                "Residual value per acre for each house type or appt type at 100% utilisation of that type ",
                "Residual (£) per house or apartment block after plot build cost, CIL and contribution to land cost",
                "Residual margin (%) per type after plot build cost and contribution to land cost",
            ],
        )

    def get_clean_data(self, source) -> pd.DataFrame:
        df: pd.DataFrame = (
            pd.read_csv(self.inputs[source]) if self.devMode else self.inputs[source]
        )

        return self.clean_data(df, source)

    def clean_data(self, df: pd.DataFrame, source: str) -> pd.DataFrame:
        if not self.devMode:
            df = df.convert_dtypes()
        df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

        if source == "site efficiency":
            df = df[self.site_efficiency_columns]
            df = df.dropna(subset=["house_type_code"])

        df = df[~df[df.columns[0]].str.startswith("#", na=False)]

        return df

    def show_site_efficiency(self):
        return self.outputs["site_efficiency"].head()

    def show_house_types(self):
        return self.house_types.head()

    def show_plotting_formats(self):
        return self.plotting_formats.head()

    def show_parking_formats(self):
        return self.parking_formats.head()

    def build(self):
        for input in self.inputs.keys():
            self.outputs[input] = self.get_clean_data(input)

        return self.outputs


class PetOptimise:
    """Optimisation algoritm for the Plotting Efficiency Tool"""

    def __init__(self, pet_data):
        self.pet_data = pet_data

    def show(self):
        print(self.pet_data)


pet_data = PetDataPrep(devMode=True).build()

PetOptimise = PetOptimise(pet_data)

PetOptimise.show()
