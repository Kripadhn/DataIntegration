WITH StreamInput AS (
  SELECT
      creditCardNumber,
      transactionAmount,
      transactionLocation,
      System.Timestamp AS EventTime
  FROM
      CreditCardTransactionInputStream
),
Anomalies AS (
  SELECT
      creditCardNumber,
      transactionAmount,
      transactionLocation,
      EventTime
  FROM
      StreamInput
  WHERE
      transactionAmount > 1000 OR
      transactionLocation != 'US'
)
SELECT
    *
INTO
    EventHubOutput
FROM
    Anomalies
