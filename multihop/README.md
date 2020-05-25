## Forked from Databricks demo

This folder the original set of workooks the Scheduled multihop repo is derived from.  The original talk was basically
a demo of some features that distinguish DeltaLake from plain spark, and emphasized how Databricks's platform
can cater to three "hats" -- Data Engineer, ML Practitioner, Business User.

This fork is more about the DataEngineer Ops aspects: we look at using the code here on Databbricks as a
job, and scheduling the acquisition of data from NASA and feeding it to the system.

It remains a demo with a setup and teardown -- as a streaming service, it could stay up as a long running
service, but the costs in 2020 are still prohibitive for that.

On the other hand, it could run as a batch, and that is more easily simulated.

Basic architecture we are aiming for in the streaming scenario

      Spark is set running "manually"
      Transactions are written one at a time into the S3 bucket "sensor"
      S3 notifies SQL
      Spark picks up message

To add to scenario:
   Duplicate records are discarded
   Incomplete records are written to a repair queue
      