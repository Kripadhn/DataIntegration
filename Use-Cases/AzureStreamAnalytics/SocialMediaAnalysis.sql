WITH StreamInput AS (
  SELECT
      tweetText,
      System.Timestamp AS EventTime
  FROM
      TwitterInputStream
),
SentimentAnalysis AS (
  SELECT
      tweetText,
      Sentiment(tweetText) AS sentiment,
      EventTime
  FROM
      StreamInput
)
SELECT
    sentiment,
    COUNT(*)
INTO
    BlobOutput
FROM
    SentimentAnalysis
GROUP BY
    sentiment,
    TumblingWindow(minute, 5)
