import matplotlib.pyplot as plt
import numpy as np
from shiny.express import ui, input, render

ui.page_opts(title="Brett's PyShiny App with Plot",fillable=True)

with ui.sidebar():
    ui.input_slider("selected_number_of_bins", "Number of Bins", 5, 50, 25)

@render.plot(alt="A histogram")
def histogram():
    count_of_points: int = 437
    np.random.seed(3)
    random_data_array = 100 + 15 * np.random.randn(count_of_points)
    plt.hist(random_data_array, input.selected_number_of_bins(), density=True)
