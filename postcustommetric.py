import boto3
import random
client = boto3.client('cloudwatch', region_name='ap-northeast-2')
#client.put_metric_data(namespace="LGCNS70in70",name="testmetric",unit="Count",value=3.0)
value = float(random.randint(1,100))
print(value)
# Put custom metrics
client.put_metric_data(
    MetricData=[
        {
            'MetricName': 'LGCNS70in70',
            'Dimensions': [
                {
                    'Name': 'Instance Name',
                    'Value': 'i-12345'
                },
            ],
            'Unit': 'None',
            'Value': value
        },
    ],
    Namespace='OpsNameSpace'
)
 
