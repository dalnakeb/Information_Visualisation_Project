import dash
import warnings
from info_vis import callbacks, layout

app = dash.Dash(__name__, suppress_callback_exceptions=True)
app.title = "Dash App"
app.layout = layout.create_layout()
warnings.filterwarnings("ignore", category=DeprecationWarning)


if __name__ == '__main__':
    app.run(debug=True)
