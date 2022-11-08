# https://github.com/klarrieu/RiverREM
# https://www.sciencebase.gov/catalog/item/543e6b86e4b0fd76af69cf4c
# https://www.sciencebase.gov/catalog/item/606d07a4d34e670a7d5d6eda
# https://www.beautifulpublicdata.com/visualizing-rivers-and-floodplains/

from riverrem.REMMaker import REMMaker

DEM_FILE: str = "USGS_1M_18_x51y432_NJ_South_Jersey_Lidar_2018_B18.tif"

# Defaults:
# COLOR_PALETTE: str = "mako_r"
# Z_FACTOR: int = 4

# COLOR_PALETTE: str = "mako"
COLOR_PALETTE: str = "icefire_r"
# Z_FACTOR: int = 10
Z_FACTOR: int = 20

if __name__ == "__main__":
    # https://opentopography.github.io/RiverREM/remindex.html#riverrem.REMMaker.REMMaker
    rem_maker = REMMaker(dem=DEM_FILE, out_dir="./output")
    rem_maker.make_rem()

    # https://opentopography.github.io/RiverREM/remindex.html#riverrem.REMMaker.REMMaker.make_rem_viz
    # https://opentopography.github.io/RiverREM/vizindex.html
    # https://matplotlib.org/stable/gallery/color/colormap_reference.html
    # https://matplotlib.org/stable/gallery/color/colormap_reference.html#reverse-cmap
    # https://seaborn.pydata.org/tutorial/color_palettes.html#sequential-color-palettes
    rem_maker.make_rem_viz(cmap=COLOR_PALETTE, z=Z_FACTOR)
