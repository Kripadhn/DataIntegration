WITH StreamInput AS (
  SELECT
      deviceId,
      temperature,
      humidity
  FROM
      IoTInputStream
),
Anomalies AS (
  SELECT
      deviceId,
      temperature,
      humidity,
      System.Timestamp AS EventTime
  FROM
      StreamInput
  WHERE
      temperature > 35 OR
      humidity > 75
)
SELECT
    *
INTO
    EventHubOutput
FROM
    Anomalies
