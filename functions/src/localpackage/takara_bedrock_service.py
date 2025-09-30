import boto3
import json


class TakaraBedrockService:
  """Contains methods for managing the takara aws Bedrock api.
  """

  def __init__(self):
    self.bedrockClient = boto3.client(service_name='bedrock-runtime', region_name='us-east-2')
    self.authCode = r')j9ju\=+ui"WuQ]=7G8s'
    self.modelId = 'us.anthropic.claude-3-5-sonnet-20240620-v1:0'
    self.inferenceConfig = {"maxTokens": 512, "temperature": 0.5, "topP": 0.9}

  def converse(self, messages):
    response = self.bedrockClient.converse(
      modelId=self.modelId,
      messages=messages,
      inferenceConfig=self.inferenceConfig
    )
    responseText = response["output"]["message"]["content"][0]["text"]
    return responseText