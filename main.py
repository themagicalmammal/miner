import matplotlib.pyplot as plt
from stock_analysis import (
    AssetGroupVisualizer,
    StockModeler,
    StockReader,
    StockVisualizer,
)
from stock_analysis.utils import describe_group, group_stocks


def miner(Date_start, Date_end, currency_var, z):

    reader = StockReader(Date_start, Date_end)

    bitcoin = reader.get_bitcoin_data(currency_var)

    fb, aapl, amzn, nflx, goog = (
        reader.get_ticker_data(ticker)
        for ticker in ["FB", "AAPL", "AMZN", "NFLX", "GOOG"])

    # get S&P 500 data
    # print(reader.available_tickers)
    sp = reader.get_index_data("NASDAQ")

    # Grouping Data

    faang = group_stocks({
        "Facebook": fb,
        "Apple": aapl,
        "Amazon": amzn,
        "Netflix": nflx,
        "Google": goog
    })

    # describe the group
    describe_group(faang)

    # Visualizing Data
    netflix_viz = StockVisualizer(nflx)
    facebook_viz = StockVisualizer(fb)
    apple_viz = StockVisualizer(aapl)
    amazon_viz = StockVisualizer(amzn)
    google_viz = StockVisualizer(goog)
    bitcoin_viz = StockVisualizer(bitcoin)

    if z == 1:
        ax = netflix_viz.evolution_over_time(
            "close",
            figsize=(10, 4),
            legend=False,
            title="Netflix closing price over time",
        )
        netflix_viz.add_reference_line(
            ax,
            x=nflx.high.idxmax(),
            color="k",
            linestyle=":",
            label=f"highest value ({nflx.high.idxmax():%b %d})",
            alpha=0.5,
        )
        netflix_viz.after_hours_trades()
        decomposition = StockModeler.decompose(nflx, 20)
        fig = decomposition.plot()

    elif z == 2:
        bx = facebook_viz.evolution_over_time(
            "close",
            figsize=(10, 4),
            legend=False,
            title="Facebook closing price over time",
        )
        facebook_viz.add_reference_line(
            bx,
            x=fb.high.idxmax(),
            color="k",
            linestyle=":",
            label=f"highest value ({fb.high.idxmax():%b %d})",
            alpha=0.5,
        )
        facebook_viz.after_hours_trades()
        decomposition = StockModeler.decompose(fb, 20)
        fig = decomposition.plot()

    elif z == 3:
        cx = apple_viz.evolution_over_time(
            "close",
            figsize=(10, 4),
            legend=False,
            title="Apple closing price over time",
        )
        apple_viz.add_reference_line(
            cx,
            x=aapl.high.idxmax(),
            color="k",
            linestyle=":",
            label=f"highest value ({aapl.high.idxmax():%b %d})",
            alpha=0.5,
        )
        apple_viz.after_hours_trades()
        decomposition = StockModeler.decompose(aapl, 20)
        fig = decomposition.plot()

    elif z == 4:
        dx = amazon_viz.evolution_over_time(
            "close",
            figsize=(10, 4),
            legend=False,
            title="Amazon closing price over time",
        )
        amazon_viz.add_reference_line(
            dx,
            x=amzn.high.idxmax(),
            color="k",
            linestyle=":",
            label=f"highest value ({amzn.high.idxmax():%b %d})",
            alpha=0.5,
        )
        amazon_viz.after_hours_trades()
        decomposition = StockModeler.decompose(amzn, 20)
        fig = decomposition.plot()

    elif z == 5:
        ex = google_viz.evolution_over_time(
            "close",
            figsize=(10, 4),
            legend=False,
            title="Google closing price over time",
        )
        google_viz.add_reference_line(
            ex,
            x=goog.high.idxmax(),
            color="k",
            linestyle=":",
            label=f"highest value ({goog.high.idxmax():%b %d})",
            alpha=0.5,
        )
        google_viz.after_hours_trades()
        decomposition = StockModeler.decompose(goog, 20)
        fig = decomposition.plot()

    elif z == 6:
        fx = bitcoin_viz.evolution_over_time(
            "close",
            figsize=(10, 4),
            legend=False,
            title="Bitcoin closing price over time",
        )
        bitcoin_viz.add_reference_line(
            fx,
            x=bitcoin.high.idxmax(),
            color="k",
            linestyle=":",
            label=f"highest value ({bitcoin.high.idxmax():%b %d})",
            alpha=0.5,
        )
        bitcoin_viz.after_hours_trades()
        decomposition = StockModeler.decompose(bitcoin, 20)
        fig = decomposition.plot()

    elif z == 7:
        faang_viz = AssetGroupVisualizer(faang)
        faang_viz.heatmap(True)

    plt.show()
