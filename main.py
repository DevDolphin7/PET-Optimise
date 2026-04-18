import pandas as pd

desired_columns = map(
    lambda column_name: column_name.strip().lower().replace(" ", "_"),
    [
        "Product name",
        "House type code",
        "Number houses or apartment blocks plotted",
        # "% of homes on site (development mix)",
        # "nett_sales_area_ft²_per_plot_or_apt_block",
        # "net_salea_area_m²",
        # "house_or_apartment",
        # "number_of_houses_or_apartments",
        # "storeys",
        # "nr_of_apts_in_block",
        # "house_width_(m)",
        "Plotting format",
        "Parking format",
        # "total_plot_width_-_house_(m)",
        # "total_plot_depth_-_house,_not_inc_half_road_(m)",
        # "fog_footprint_inc_margins",
        # "off_plot_parking_(m²)_per_house_plot_or_apartment_block",
        # "site_specific_npa_(m2)_per_plot_or_appt_block",
        # "area_of_half_road_width_infront_of_plot(m²)",
        # "total_land_take_per_plot_or_apt_block:_npa+half_road_+_amenity_space_(m² )",
        # "total_land_take_agregated",
        # "houses/apt_blocks / acre based on total land take ",
        "Theoretical coverage based on total land take (ft²/acre)",
        # "total_theoretical_land_take (acres) per type",
        # "total_saleable_area for house type or appt block type",
        # "Sales value:  £ / house/apartment block",
        # "Agregated revenue by house or apt  type ",
        # "Cost of parking and or garages per plot or apt block",
        "Dwelling structures abnormals:  £/plot",
        "Dwelling structure cost / house plot or apartment block                                                                                                         (NB standard parking costs entered in House Type Database tab)",
        # "Total CIL per house plot or apt block",
        # "Total Build Cost: Dwelling structure + Dwelling structure abnormal + parking cost + CIL per plot or appt block",
        # "Build cost + CIL per house/apt  type agregated",
        # "Profit required per house or appt type at fixed margin",
        "Residual  value after plot build cost, CIL and contribution to profit per house or apartment block",
        "Residual value per acre for each house type or appt type at 100% utilisation of that type ",
        # "Cost of land per type agregated",
        "Residual (£) per house or apartment block after plot build cost, CIL and contribution to land cost",
        # "Residual margin agregated",
        "Residual margin (%) per type after plot build cost and contribution to land cost",
    ],
)


class PetOptimiser:
    def __init__(self, devMode=False) -> None:
        self.data = self.get_clean_data()

    def get_clean_data(self) -> pd.DataFrame:
        df: pd.DataFrame = pd.read_csv("__test__/test_data.csv")

        return self.clean_data(df)

    def clean_data(self, df) -> pd.DataFrame:
        df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

        df = df[desired_columns]

        df = df.dropna(subset=["house_type_code"])

        return df[~df["product_name"].str.startswith("#", na=False)]

    def show_data(self):
        return self.data.head()


print(PetOptimiser(devMode=True).show_data())
