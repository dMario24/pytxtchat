df = spark.read.option("multiline", "true").json("/home/diginori/code/mvstar/data/movies")

df.count()

from pyspark.sql.functions import explode_outer
edf = df.withColumn("company", explode_outer("companys"))
eedf = edf.withColumn("director", explode_outer("directors"))

eedf.printSchema()

from pyspark.sql.functions import col
sdf = eedf.withColumn("directorNm", col("director.peopleNm"))
sdf = sdf.withColumn("companyCd", col("company.companyCd"))
sdf = sdf.withColumn("companyNm", col("company.companyNm"))

sdf = sdf.drop('company', 'director', 'companys', 'directors')
sdf.printSchema()

sdf.count()
df_no_duplicates = sdf.drop_duplicates()
df_no_duplicates.count()

df_no_duplicates.coalesce(1).write.format("parquet").mode("append").save("/home/diginori/code/pytxtchat/src/pytxtchat/data/movies")