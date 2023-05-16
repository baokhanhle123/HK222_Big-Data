from pyspark.sql import SparkSession

def main():
    # Khởi tạo SparkSession
    spark = SparkSession.builder.appName("SimpleApp").getOrCreate()

    # Tạo một DataFrame từ danh sách các số
    numbers = [1, 2, 3, 4, 5]
    df = spark.createDataFrame(numbers, "integer").toDF("number")

    # Thực hiện phép nhân với 2 trên cột "number"
    multiplied_df = df.select(df.number * 2)

    # Hiển thị kết quả
    multiplied_df.show()

    # Dừng SparkSession
    spark.stop()

if __name__ == "__main__":
    main()
