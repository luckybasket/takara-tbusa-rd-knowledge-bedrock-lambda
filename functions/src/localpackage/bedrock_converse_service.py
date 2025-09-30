import importlib


class BedrockConverseService:
  """Contains methods for processing the Bedrock converse service.
  """

  def __init__(self, logger):
    self.tbrs = importlib.import_module("localpackage.takara_bedrock_chat_service")
    self.takaraBedrockChat = self.tbrs.TakaraBedrockChatService()
    self.logger = logger
    return


  def converse(self, userMessage):
    conversation = [
      {
          "role": "user",
          "content": [{"text": userMessage}],
      }
    ]
    responseText = self.takaraBedrockChat.converse(conversation)
    return responseText

