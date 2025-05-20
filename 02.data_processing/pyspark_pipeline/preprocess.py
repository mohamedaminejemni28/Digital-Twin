from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg, window

spark = SparkSession.builder.appName("AthletePreprocessing").getOrCreate()

def preprocess_data(input_path, output_path):
    df = spark.read.json(input_path)

    df_clean = df.dropna().withColumn("heart_rate", col("heart_rate").cast("int"))

    df_agg = df_clean.groupBy(window("timestamp", "1 minute"))\
                     .agg(avg("heart_rate").alias("avg_heart_rate"))

    df_agg.write.mode("overwrite").json(output_path)

if __name__ == "__main__":
    preprocess_data("data/raw/", "data/processed/")