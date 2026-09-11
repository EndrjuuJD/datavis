# w37-2 Lab — pandas & plotly
#
# Guided, hands-on. A plain script — run it top-to-bottom in Positron, in the
# course uv environment.
# Fill in every `# TODO`. Finish with a `git commit` (last section).
#
# SETUP (once, in a terminal, from the shared project folder):
#     cd project
#     uv add pandas plotly
#     uv sync
# Then open THIS file and make sure Positron's Console uses the project's .venv.

# 1. Import your own module + the libraries  (objective 1)
import pandas as pd
import plotly.express as px

import saleslib                    # our own module (saleslib.py, next to this file)

sales = saleslib.load_sales()
print(sales.shape)
sales.head()

# TODO: look at the data before working with it. Print:
#   (a) the column names        -> sales.columns.tolist()
#   (b) the dtypes              -> sales.dtypes   (is `date` a datetime?)
#   (c) the first 3 rows        -> sales.head(3)


# 2. Select & filter with .loc  (objective 2)
sales[["region", "revenue_kdkk"]].head()

# TODO: using .loc[rows, cols], get the date, product and revenue_kdkk
# for the "West" region only. Assign to `west` and print west.head().


# TODO: filter for GADGETS days where units >= 40.
# Combine two conditions with & and wrap each in ( ). How many rows match?


# 3. groupby / aggregate  (objective 2)
by_region = sales.groupby("region")["revenue_kdkk"].sum().sort_values(ascending=False)
print(by_region)

# TODO: group by "product" and compute BOTH total units and total revenue,
# using .agg(total_units=("units","sum"), total_rev=("revenue_kdkk","sum")).
# Remember .reset_index() to get a flat table. Print it.


# 4. merge two tables  (objective 2)
regions = saleslib.load_regions()
print(regions)

# TODO:
#   (a) build `region_rev` = total revenue_kdkk per region
#       (groupby("region", as_index=False)["revenue_kdkk"].sum())
#   (b) merge it with `regions` on "region" -> `joined`
#   (c) add a column revenue_mdkk = revenue_kdkk / 1000  (round to 2)
#   (d) add pct_of_target = revenue_mdkk / q1_target_mdkk * 100  (round to 1)
#   (e) print region, manager, revenue_mdkk, q1_target_mdkk, pct_of_target


# 5. Time series: resample & rolling  (objective 2)
daily = sales.groupby("date")["revenue_kdkk"].sum().sort_index()
print(daily.head())

# TODO:
#   (a) resample `daily` to WEEKLY totals -> `weekly`  (daily.resample("W").sum())
#   (b) make a 7-day rolling mean of `daily` -> `smooth`  (daily.rolling(7).mean())
#   (c) print how many weekly points there are, and smooth.tail(3)


# 6. Chart it with plotly express  (objective 3)
# In Positron, fig.show() opens the plot.
region_daily = sales.groupby(["date", "region"], as_index=False)["revenue_kdkk"].sum()
fig = px.line(region_daily, x="date", y="revenue_kdkk", color="region",
              title="Daily revenue by region")
fig.show()

# TODO: make a horizontal BAR chart of total revenue per region.
#   - start from `by_region` (section 3) via by_region.reset_index()
#   - px.bar(..., x="revenue_kdkk", y="region", orientation="h")
#   - give it a title, then fig.show()


# TODO: make a SCATTER for a single day (e.g. sales["date"] == "2026-03-02"),
# mapping FOUR channels:
#   x="region", y="revenue_kdkk", color="product", size="units"
# Then fig.show(). Which channel encodes which column?


# 7. Save your work  (objective 4 — the git habit)
# In a terminal, from your project folder:
#
# git add -A
# git commit -m "Complete w37-2 lab: pandas wrangling and plotly charts"
