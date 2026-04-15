# Taxi Demand Prediction and Dispatch Planning

A short machine learning project that predicts NYC taxi trip duration and converts predictions into a zone-wise taxi dispatch plan.

## What this project does

- Trains and compares 7 regression models on NYC taxi trip data.
- Uses engineered temporal and distance features to improve prediction quality.
- Evaluates models with RMSE, R2, MAE, and training time.
- Builds a 20-zone dispatch strategy and allocates a 500-taxi fleet by predicted demand.
- Publishes results in a simple local website dashboard.

## Best model snapshot

From `results/metrics.csv`:

- Best RMSE: Gradient Boosting (0.3514)
- Near-best but much faster: XGBoost (0.3515, ~1.34s train time)

## Project workflow

Run notebooks in this order:

1. `01_EDA_and_Modeling.ipynb`  
   Cleans data, engineers features, trains models, writes metrics and plots.
2. `02_Results_Summary.ipynb`  
   Summarizes and prepares final result artifacts for presentation.
3. `03_Dispatch_Planning.ipynb`  
   Clusters pickup zones, computes demand labels, and generates taxi allocation plan.

## Repository structure

- `Data/NYC.csv`: input dataset
- `results/`: generated CSV, JS, and plot artifacts
- `website/index.html`: dashboard UI that reads `results/results_data.js` and `results/dispatch_data.js`
- `serve.py`: local server entry point for the dashboard
- `Project File/mini_project_report.tex`: LaTeX report source


## Run and reproduce

1. Start Jupyter and run all notebook cells in sequence:

```bash
jupyter notebook
```

2. Launch the website locally from project root:

```bash
python serve.py
```

Then open `http://localhost:8000/website/`.

## Main outputs

- `results/metrics.csv`: model comparison table
- `results/test_predictions.csv`: test-set predictions
- `results/dispatch_plan.csv`: ranked zone-wise dispatch plan
- `results/plots/*.png`: EDA, model, and dispatch visualizations
