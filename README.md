⚡ Zone Risk Engine (ZRE)

Zone Risk Engine (ZRE) is a simulation driven anomaly detection system for electrical distribution zones, operating in simulated real time intervals. It compares aggregated household consumption against simulated transformer level load to identify imbalance, abnormal usage patterns, and potential risks such as power theft, overload, and system faults.

What it does

ZRE continuously analyzes multi house electrical activity within each zone and produces a normalized risk score in the range 0 → 1.

The system integrates:

* Statistical baseline tracking (adaptive smoothing)
* Isolation Forest anomaly detection
* DBSCAN based clustering irregularity detection
* Temporal drift detection (distribution shift tracking)
* Lightweight LSTM based short term signal estimation (single feature prediction)
* Time aware feature encoding (hour of day context)
* Automated email alerting

to surface abnormal electrical behavior in simulated real-time intervals.


Risk Computation

The final risk score is computed through a fusion of multiple signals:

* Anomaly Signal (Isolation Forest classification)
* Deviation from Baseline (statistical drift from expected behavior)
* Clustering Irregularity (density based outlier patterns)
* Temporal Drift (change in clustering distribution over time)
* Short Term Signal Estimate (LSTM based component)

These components are combined and passed through a bounded activation function:

risk = tanh(anomaly + deviation/10 + cluster + drift + future/6)

This produces a stable, normalized risk score that reacts to both sudden anomalies and gradual behavioral shifts.

Why it matters

Electrical anomalies such as theft, illegal tapping, and overload are often detected late due to lack of continuous monitoring and interpretability.

ZRE transforms raw electrical signals into actionable risk insights, acting as an early warning layer that supports:

* Faster inspection decisions
* Improved grid reliability
* Reduction of non technical losses


Core Features

* Zone wise risk scoring (simulation driven interval stream)
* Simulated transformer vs household load comparison
* Adaptive statistical baseline modeling
* Isolation Forest anomaly detection
* DBSCAN based pattern irregularity detection
* Temporal drift detection using clustering shifts
* LSTM based short-term signal estimation
* Time aware feature encoding (hour-based context)
* Persistent CSV logging of zone activity
* FastAPI backend supporting real-time ingestion (currently simulated input stream)
* Streamlit dashboard (tables, heatmaps, time-series)
* Automated email alerts when risk exceeds threshold


System Architecture

Backend

* Python
* NumPy / Pandas
* FastAPI + Uvicorn
* PyTorch (LSTM model)
* Scikit-learn (Isolation Forest, DBSCAN)
* SMTP (alert system)

Frontend

* Streamlit dashboard
* Zone status tables
* Load heatmaps
* Risk over time visualization



Screenshots

1. Backend Engine Running
   Live WSL simulation generating continuous zone wise risk scores.

2. API Health Check
   FastAPI/Uvicorn endpoint returning "200 OK", confirming backend availability.

3. Dashboard Overview
   Real time zone table showing total load, per house values, and highest risk zone.

4. Load Heatmap
   Visualization of house level consumption patterns across zones.

5. Risk Over Time
   Time series representation of risk evolution across zones.

6. Email Alert System
   Automated alert triggered when risk crosses the defined threshold.



System Limitation (Critical Insight)

The current system operates on aggregated energy measurements, which introduces a fundamental limitation.

After Meter Theft Problem

Grid flow:

Transformer → Meter → House

Two cases:

1. Before-Meter Theft

* Energy stolen before meter
* Creates imbalance
* Detected successfully

2. After-Meter Theft

* Energy stolen after meter
* Meter still records full consumption
* No observable imbalance

Result

Both normal usage and after meter theft produce identical observations:

sum(loads) ≈ total

This creates an identifiability problem, where different physical realities map to the same measured data.

This limitation is not due to model failure, but due to insufficient measurement granularity.



System Evolution: Line Level Sensing

To resolve this, the system can be extended with multi point sensing:

Transformer
→ Line Sensor (before meter)
→ Meter
→ Line Sensor (after meter)
→ House

This enables:

* Localization of energy loss
* Differentiation between user consumption and theft
* Reduced ambiguity in anomaly interpretation
* Transition from detection → precise fault identification



How to Run

Backend

python zre_backend.py

Dashboard

streamlit run dashboard.py



Project Structure

ZRE/
├── zre_backend.py
├── dashboard.py
├── requirements.txt
├── README.md
└── screenshots/


Notes

This project is a working prototype focused on:

* Risk signal fusion
* Real time scoring (simulated intervals)
* Visualization
* Alert generation

The current implementation uses simulated input streams and validates anomaly detection logic, temporal behavior, and system response before real world deployment.



Closing Note

ZRE is not a complete grid solution.

It is a system that demonstrates how anomaly detection can be applied to electrical infrastructure while explicitly identifying its own limitations and the path required to overcome them.

This repository represents a transition point:

from detecting anomalies
to understanding where and why they occur.
