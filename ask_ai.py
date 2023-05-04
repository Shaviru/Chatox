import requests
import json

def get_prediction(input_user):
  data = {"sentence": input_user}
  url = 'https://askai.aiclub.world/25a6be60-8c54-4809-b5bf-aeafccbd0766'
  r = requests.post(url, data=json.dumps(data))
  response = getattr(r, '_content').decode("utf-8")
  prediction = json.loads(json.loads(response)['body'])['predicted_label']
  return prediction
