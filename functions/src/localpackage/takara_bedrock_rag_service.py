import boto3
import json


class TakaraBedrockRAGService:
  """Contains methods for managing the takara aws Bedrock RAG api.
  """

  def __init__(self, modelARN, knowledgeBaseID, sessionID):
    self.bedrockClient = boto3.client(service_name='bedrock-agent-runtime', region_name='us-east-2')
    self.authCode = r')j9ju\=+ui"WuQ]=7G8s'
    self.modelARN = modelARN
    self.knowledgeBaseID = knowledgeBaseID
    self.sessionID = sessionID
    self.responseContent = None
    self.responseCitationsList = []
    self.isSuccess = False


  def query(self, queryText):
    try:
      if self.sessionID is None:
        response = self.bedrockClient.retrieve_and_generate(
          input={
              'text': queryText
          },
          retrieveAndGenerateConfiguration={
              'type': 'KNOWLEDGE_BASE',
              'knowledgeBaseConfiguration': {
                  'knowledgeBaseId': self.knowledgeBaseID,
                  'modelArn': self.modelARN
              }
          }
        )
      else:
        response = self.bedrockClient.retrieve_and_generate(
          input={
              'text': queryText
          },
          retrieveAndGenerateConfiguration={
              'type': 'KNOWLEDGE_BASE',
              'knowledgeBaseConfiguration': {
                  'knowledgeBaseId': self.knowledgeBaseID,
                  'modelArn': self.modelARN
              }
          },
          sessionId=self.sessionID
        )
      self.sessionID = response.get('sessionId')
      self.responseContent = response['output']['text']
      citations = response['citations']
      self.responseCitationsList = []
      for citation in citations:
        self.responseCitationsList.append(
          citation['retrievedReferences'][0]['location']['s3Location']['uri']
        )
      self.isSuccess = True
      return
    except Exception as e:
      self.responseContent = f"Error querying Bedrock: {e}"
      self.isSuccess = False
      return