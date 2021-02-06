## Metrics

- Event Data Loss
  - There are gaps in the event data/time-series
- Short Data History
  - Insufficient data for analysis
- Aggregated Data
  - If the recorded data is instantaneous or aggregated over time
- Data not-updated
  - Old data being recorded; sensors showing old values
- Inaccurate Measurement
  - Inaccurate value recorded which might result in wrong analysis
- Rounded Measurement Value
  - Resolution error in unit scale due to measurement techniques.
  


- Calculated Values
  - Values are calculated instead of real measurement value.
- Data Formats
  - Different data formats; floats v strings
- Timestamp Formats
  - Different formats used for representing timestamp 
- Divergent Measurement
  - Values which should be the same are different. Always or sometimes
- Different Accuracy
  - There is a different level of accuracy for the same type of data
- Wrong Timestamp
  -  Timestamps are wrong

- Signal Noise
  -  Small changes which are not in the process but result from inaccurate measurements, recognizable with low pass filter
- Diverging Sampling
  - Different sampling rates in the same time series can lead to problems
- Inconsistent Noise Level
  - The level of noise changes over time or from different data sources
- Class Imbalance
  - There is a bias in the sample as opposed to the population
- Heteroscedasticity
  - There are subpopulations that have different variabilities from others, detectable via Goldfeld-Quandt test
- Value Spikes
  - Spikes or sudden changes which are implausible for the domain
