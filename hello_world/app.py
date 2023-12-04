import json

def lambda_handler(event, context):
    print("Change deployed with SAM Accelerate");
    return {
    "statusCode": 200,
    "body": json.dumps({
        "message": "I'm using canary deployments",
    }),
}



