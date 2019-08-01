

<hr/>
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "logs:CreateLogGroup",
        "logs:CreateLogStream",
        "logs:PutLogEvents",
        "logs:DescribeLogGroups",
        "logs:DescribeLogStreams"
    ],
      "Resource": [
        "arn:aws:logs:*:*:*"
    ]
  }
 ]
}


Policy : AWSDC-APNE2-IAM-PO-Cloudwatch-Logs

Role : AWSDC-APNE2-IAM-RO-Cloudwatch-Logs



Assign Role to EC2

sudo yum install -y awslogs

ec2-user@ip-172-31-25-217:/home/ec2-user> sudo vi /etc/awslogs/awscli.conf 
ec2-user@ip-172-31-25-217:/home/ec2-user> sudo cat  /etc/awslogs/awscli.conf
[plugins]
cwlogs = cwlogs
[default]
region = ap-northeast-2


ec2-user@ip-172-31-25-217:/home/ec2-user> sudo cat /etc/awslogs/awslogs.conf
[general]
state_file = /var/lib/awslogs/agent-state
[application_logs]
region = ap-northeast-2
datetime_format = %b %d %H:%M:%S
file = /var/log/application.log
buffer_duration = 5000
log_stream_name = {instance_id}
initial_position = start_of_file
log_group_name = application_logs


ec2-user@ip-172-31-25-217:/home/ec2-user> sudo service awslogs start
Starting awslogs:   

ec2-user@ip-172-31-25-217:/home/ec2-user> sudo su -
[root@ip-172-31-25-217 ~]# cd /var/log
[root@ip-172-31-25-217 log]# echo 'Staring application!!' > application.log
[root@ip-172-31-25-217 log]# cat application.log
Staring application!!
[root@ip-172-31-25-217 log]# echo '2nd line log' >> application.log

CloudWatch LOGS 확인 

root@ip-172-31-17-17:/var/log# cat dummy.sh 
for ((i=0;i<10;i++)); do
echo $i >> application.log
done

Filter DEMO
Create Filter - 1분 주기
Creat Alarm
Accept notification

for ((i=0;i<100;i++)); do
echo $i >> application.log
done

root@ip-172-31-17-17:/var/log# echo 'ORA-00600' >> application.log 
root@ip-172-31-17-17:/var/log# echo 'ORA-00600' >> application.log 
root@ip-172-31-17-17:/var/log# echo 'ORA-00600' >> application.log 
root@ip-172-31-17-17:/var/log# echo 'ORA-00600' >> application.log 
root@ip-172-31-17-17:/var/log# echo 'ORA-00600' >> application.log 
root@ip-172-31-17-17:/var/log# echo 'ORA-00600' >> application.log

>> 기다리면 Alarm 발생


