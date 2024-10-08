import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Script generated for node Amazon S3
AmazonS3_node1721734293776 = glueContext.create_dynamic_frame.from_options(format_options={"multiline": False}, connection_type="s3", format="json", connection_options={"paths": ["s3://dataplanegluejobdatasource"], "recurse": True}, transformation_ctx="AmazonS3_node1721734293776")

# Script generated for node Amazon S3
AmazonS3_node1721734507620 = glueContext.write_dynamic_frame.from_options(frame=AmazonS3_node1721734293776, connection_type="s3", format="csv", connection_options={"path": "s3://dataplanegluejobdatatarget", "partitionKeys": []}, transformation_ctx="AmazonS3_node1721734507620")

job.commit()