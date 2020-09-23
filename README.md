# Auto Shutdown EC2 instances.
Automatically Stopping EC2 Instances with a tag Using Lambda and CloudWatch

## Step 1: Create an IAM rule
Create a role that can access EC2 instances from the Lambda function. Follow the steps below 
1) Go to IAM dashboard.
2) Under the access managment click on "Roles".
3) Click on Create Role and select Lambda in "Choose a use case".
4) Click "Next: Permissions" button.
5) Select "AmazonEC2FullAccess" policy from the list and click "Next". 
6) Add Tags is an optional step and one can choose to skip this.
7) Give a name to the role like "LambdaFullAccessEC2" and create the role.

## Step 2: Create Lambda functions that stops your EC2 instances 
1) In the Lambda console, choose Create function.
2) Choose Author from scratch.
3) Under Basic information, add the following:
        - Function name: StopEC2Instances
        - For Runtime, choose Python 3.7.
        - Under Execution role, choose Use an existing role.
        - Under Existing role, choose the IAM role that you created("LambdaFullAccessEC2") .
4. Choose Create function.
5. Copy the code given in lambda_shutdown.py. This code stops the EC2 instances according to the given tag name on line number 
6. Just replace the development tag with the required tag.
7. Click on Deploy.
8. To test the working of lambda function click on "Test" and don't worry about editing the boiler-plate JSON string shown.

## Step 3: Create rules that trigger your Lambda functions

1) Open the CloudWatch console.
2) In the left navigation pane, under Events, choose Rules.
3) Choose Create rule.
4) Under Event Source, choose Schedule.
5) Do either of the following:
For fixed rate of, enter an interval of time in minutes, hours, or days.
For Cron expression, enter an expression that tells Lambda when to stop your instances. For information on the syntax of expressions, click on Learn More.
Note: Cron expressions are evaluated in UTC. Be sure to adjust the expression for your preferred time zone.
For 6:30pm EST enter "30 22 * * ? *" 
6) Under Targets, choose Add target.
7) Choose Lambda function.
8) For Function, choose the function that we created to stop EC2 instance(StopEC2Instances).
9) Choose Configure details.
10) Under Rule definition, do the following:
     - Name: "StopEC2Instances"<br>
     - (Optional) For Description, describe your rule. For example, "Stops EC2 instances every night at 10 PM."
     - For State, select the Enabled check box.
11) Choose Create rule.

References: 
1) https://aws.amazon.com/premiumsupport/knowledge-center/start-stop-lambda-cloudwatch/
2) https://medium.com/@Hironsan/save-aws-ec2-cost-by-automatically-stopping-idle-instance-using-lambda-and-cloudwatch-759edd62b27d
