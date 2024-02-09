Section 10 : Lambda : 9 Feb 24

1. Set up working space

Author name proejct dir : "ghactivity-downloader", But I name it "Lambda"

cd ~/Projects/Internal/Lambda 
python3 -m venv ghad-venv		# Create Python Virtual Environment
source ghad-venv/bin/activate		# Change / Activate virtual env.
pip install requests 			# For example file download
pip install boto3
(dpkg --list | grep -i <package_name>)     	<-- to list installed package
pip list					<-- To check installed Python module
pip freeze (ก็ดูได้แต่ใช้อันบนดูง่าย เป็นระเบียบกว่า)

2. If we plan to upload to AWS Lambda console later, also need to prepare related libe in separate sub-dir too
pip install requests==2.25 -t ghalib  	# Pip install into target sub directory name "ghalib", need old version to be able to run
					# Sometimes (this time too), we even need to reduce Python version to 3.8	


3. Zip all file locally and then upload for AWS
zip -r Lambda.zip lambda_function.py	# -r = recursive into directory

Then goto lambda screen, there is "Upload from" button on upper left screen, use it ! 

4. To also upload the dependency into AWS Lambda

cd ghalib
zip -r ../Lambda.zip .					# Zip all file in library folder but save final result in parent folder
cd ..
zip -g Lambda.zip lambda_function.py download.py 	# Add our programs at the same directory level

-------------------------------------------------------

5. Working with S3 Bucket

aws s3api get-bucket-acl --bucket delab-github-mana00	# Check Bucket owner แต่ดูเหมือน S3 Owner จะเป็นของ Root  หมดเลย

{
    "Owner": {
        "DisplayName": "laiaddara",
        "ID": "709f2485bbc57aa0687e130826e0d8c48d3beaba7e7f08305a5a39db5536f4f3"
    },
    "Grants": [
        {
            "Grantee": {
                "DisplayName": "laiaddara",
                "ID": "709f2485bbc57aa0687e130826e0d8c48d3beaba7e7f08305a5a39db5536f4f3",
                "Type": "CanonicalUser"
            },
            "Permission": "FULL_CONTROL"
        }
    ]
}

6. Note : When updating .env file in VSCode, need to re-start VSCode to make it effective

7. The overall work flow is
  7.1 Set up aws configure [default] profile in local computer
  7.2 Use VS Code to develop the code and access via the above profile, use 
      - .env file for env. var ( Need to restart VS code to make it effective)
      - lambda_validate.py ask the trigger

	from lambda_function import lambda_handler
 
	res = lambda_handler(None, None)
	print(res)
   
  7.3 Zip all code and dependencies into 1 .zip file
  7.4 In AWS, Lamdbda GUI upload .zip file
  7.5 In Lambda Configuration > General Configuration menu
      - Select appropriate Memory and Timeout
      In Permission, make the least permission policy and attach to lambda execution role
      In Env. Variables, fill in the needed Env Var
  7.6 Run it ! 


8. To see the help related to boto3 function, e.g. .get_object, make .py in VSCode and run,

import boto3
s3_client = boto3.client('s3')
help(s3_client.get_object )

9. We used .encode to change String --> ByteStream and 
           .decode to change ByteStream --> String 

10. Main Component for this section

    - Middle : Lambda to read from source and write to S3
               + Using Local development env
    - Source : File name (String vs date) alchemy
    - Target : Bookmark management (Read / Write / Error detection)
