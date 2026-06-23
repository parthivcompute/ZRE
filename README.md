⚡ Zone Risk Engine (ZRE)

Zone Risk Engine (ZRE) is a simulation driven anomaly detection system for electrical distribution zones. It operates over simulated real time intervals, comparing aggregated household consumption with transformer level load to identify imbalances, abnormal usage patterns, and potential risks such as power theft, overload, and system faults.

What it does

ZRE continuously monitors multi house electrical activity within each zone and produces a normalized risk score between 0 and 1.

Instead of relying on a single method, the system combines multiple signals:

Statistical baseline tracking using adaptive smoothing
Isolation Forest for anomaly detection
DBSCAN for clustering irregularities
Temporal drift detection based on distribution changes over time
Lightweight LSTM for short term signal estimation using single feature prediction
Time aware feature encoding using hour of day context

These components work together to surface abnormal electrical behavior in near real time.


Risk Computation

The final risk score is computed through a fusion of multiple signals:

Anomaly signal from Isolation Forest classification
Deviation from baseline representing statistical drift
Clustering irregularity capturing density based outliers
Temporal drift representing changes in clustering distribution over time
Short term signal estimate from the LSTM component

These are combined using a bounded activation function:

risk = tanh(anomaly + deviation/10 + cluster + drift + future/6)

This produces a stable and normalized score that responds to both sudden anomalies and gradual behavioral shifts.


Why it matters

Electrical anomalies such as theft, illegal tapping, and overload are often detected late due to limited monitoring and poor interpretability.

ZRE transforms raw electrical signals into actionable risk insights, acting as an early warning layer that enables:

Faster inspection decisions
Improved grid reliability
Reduction of non technical losses


Core Features

Zone wise risk scoring using a simulation driven interval stream
Simulated transformer versus household load comparison
Adaptive statistical baseline modeling
Isolation Forest based anomaly detection
DBSCAN based irregularity detection
Temporal drift tracking using clustering shifts
LSTM based short term signal estimation
Time aware feature encoding
Persistent CSV logging of zone activity
FastAPI backend supporting real time ingestion with simulated input
Streamlit dashboard with tables, heatmaps, and time series
Automated email alerts when risk exceeds threshold


System Architecture

Backend

Python
NumPy and Pandas
FastAPI with Uvicorn
PyTorch for LSTM modeling
Scikit learn for Isolation Forest and DBSCAN
SMTP based alert system

Frontend

Streamlit dashboard
Zone status tables
Load heatmaps
Risk over time visualization


Screenshots

Backend Engine Running
Live WSL simulation generating continuous zone wise risk scores

API Health Check
FastAPI endpoint returning 200 OK confirming backend availability

Dashboard Overview
Real time zone table showing load distribution and highest risk zone

Load Heatmap
Visualization of house level consumption patterns across zones

Risk Over Time
Time series representation of risk evolution across zones

Email Alert System
Automated alert triggered when risk crosses the defined threshold


System Limitation (Critical Insight)

The system operates on aggregated energy measurements, which introduces a fundamental limitation.

After Meter Theft Problem

Grid flow

Transformer → Meter → House

Two cases

Before meter theft
Energy stolen before the meter
Creates imbalance
Detectable

After meter theft
Energy stolen after the meter
Meter still records full usage
No observable imbalance

Result

sum(loads) ≈ total

This creates an identifiability problem where different physical realities produce identical measurements.

This limitation is not due to model failure, but due to insufficient measurement granularity.



System Evolution: Line Level Sensing

Proposed extension

Transformer → Line Sensor → Meter → Line Sensor → House

This enables

Localization of energy loss
Differentiation between consumption and theft
Reduced ambiguity in anomaly interpretation
Transition from detection to precise fault identification


How to Run

Backend

python zre_backend.py

Dashboard

streamlit run dashboard.py


Project Structure

ZRE/
zre_backend.py
dashboard.py
requirements.txt
README.md
screenshots/


Notes

This project is a working prototype focused on

Risk signal fusion
Real time scoring using simulated intervals
Visualization
Alert generation

The current implementation uses simulated input streams to validate anomaly detection logic, temporal behavior, and system response before real world deployment.


Closing Note

ZRE is not a complete grid solution.

It demonstrates how anomaly detection can be applied to electrical infrastructure while explicitly identifying its limitations and the path forward.

This repository represents a transition

from detecting anomalies
to understanding where and why they occur
