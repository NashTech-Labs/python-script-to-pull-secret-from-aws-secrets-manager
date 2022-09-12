from subprocess import Popen, PIPE

import os
import yaml
import json
import boto3
import argparse

"""
Retrieves github process account info (user/key)
returns: tuple first element username, second element api key
"""
def get_secret():
    secrets = boto3.client("secretsmanager")
    secret_arn = ""
    secret_response = secrets.get_secret_value(
        SecretId=secret_arn
    )

    jsonbody = json.loads(secret_response["SecretString"])
    username = jsonbody["username"]
    key = jsonbody["api_key"]

    return username, key