import botocore
from flask import Flask
import boto3

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!!!"
@app.route("/whoami")
def getsts():
    try:
        sts = boto3.client('sts')
        response = sts.get_caller_identity()
        response = response.get('Arn').split('/')[1]
    except botocore.exceptions.ClientError as e:
        response = e
    except botocore.exceptions.ProfileNotFound as e:
        response = e
    return "Hello, World! You are {}".format(response)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=80)
