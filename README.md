# cloudfront-invalidation(python v3.3+)


## Running Logs
```logs
[Started check_invalidation_path]
test.txt
[Completed check_invalidation_path]
[Started create_invalidation]
{'ResponseMetadata': {'RequestId': '001efdbc-9142-11e8-9cd1-4de0061f6e0b', 'HTTPStatusCode': 201, 'HTTPHeaders': {'x-amzn-requestid': '001efdbc-9142-11e8-9cd1-4de0061f6e0b', 'location': 'https://cloudfront.amazonaws.com/2017-10-30/distribution/E12OX8RSSI1M70/invalidation/I2QDTZQZJSZSFM', 'content-type': 'text/xml', 'content-length': '366', 'date': 'Fri, 27 Jul 2018 02:08:48 GMT'}, 'RetryAttempts': 0}, 'Location': 'https://cloudfront.amazonaws.com/2017-10-30/distribution/E12OX8RSSI1M70/invalidation/I2QDTZQZJSZSFM', 'Invalidation': {'Id': 'I2QDTZQZJSZSFM', 'Status': 'InProgress', 'CreateTime': datetime.datetime(2018, 7, 27, 2, 8, 49, 102000, tzinfo=tzutc()), 'InvalidationBatch': {'Paths': {'Quantity': 1, 'Items': ['/test.txt']}, 'CallerReference': '1532704668.0'}}}
[Completed create_invalidation]
[Started check_invalidation]
Inprogress Invalidation... 0
Inprogress Invalidation... 5
Inprogress Invalidation... 10
Inprogress Invalidation... 15
Inprogress Invalidation... 20
Inprogress Invalidation... 25
Inprogress Invalidation... 30
Inprogress Invalidation... 35
Inprogress Invalidation... 40
{'ResponseMetadata': {'RequestId': '1936c917-9142-11e8-9cd1-4de0061f6e0b', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amzn-requestid': '1936c917-9142-11e8-9cd1-4de0061f6e0b', 'content-type': 'text/xml', 'content-length': '365', 'date': 'Fri, 27 Jul 2018 02:09:31 GMT'}, 'RetryAttempts': 0}, 'Invalidation': {'Id': 'I2QDTZQZJSZSFM', 'Status': 'Completed', 'CreateTime': datetime.datetime(2018, 7, 27, 2, 8, 49, 102000, tzinfo=tzutc()), 'InvalidationBatch': {'Paths': {'Quantity': 1, 'Items': ['/test.txt']}, 'CallerReference': '1532704668.0'}}}
[Completed Check_Invalidation]
Completed --- 44.67824721336365seconds ---
```
