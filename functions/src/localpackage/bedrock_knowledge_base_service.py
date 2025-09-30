import importlib


class BedrockKnowledgeBaseService:
  """Contains methods for processing the Bedrock knowledge base service.
  """

  def __init__(self, knowledgeBaseID, modelARN, sessionID, logger):
    self.tbrs = importlib.import_module("localpackage.takara_bedrock_rag_service")
    self.takaraBedrockRAG = self.tbrs.TakaraBedrockRAGService(modelARN, knowledgeBaseID, sessionID)
    self.logger = logger
    return


  def query(self, queryText):
    self.takaraBedrockRAG.query(queryText)
    isSuccess = self.takaraBedrockRAG.isSuccess
    responseContent = self.takaraBedrockRAG.responseContent
    responseCitationsList = self.takaraBedrockRAG.responseCitationsList
    sessionID = self.takaraBedrockRAG.sessionID
    return isSuccess, responseContent, responseCitationsList, sessionID

