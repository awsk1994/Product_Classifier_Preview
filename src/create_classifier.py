import json
from ibm_watson import NaturalLanguageClassifierV1
from ibm_watson import ApiException
import Settings

try:
  natural_language_classifier = NaturalLanguageClassifierV1(
    iam_apikey=Settings.API_KEY,
    url=Settings.URL)

  with open(Settings.TRAINING_DATA_PATH, 'rb') as training_data:
      with open(Settings.METADATA_PATH, 'rb') as metadata:
        classifier = natural_language_classifier.create_classifier(
          training_data=training_data,
          metadata=metadata
        ).get_result()
  print(json.dumps(classifier, indent=2))
except ApiException as ex:
  print("Method failed with status code " + str(ex.code) + ": " + ex.message)

'''
Expected response:
{
  "name": "TutorialClassifier",
  "language": "en",
  "status": "Training",
  "url": "https://gateway.watsonplatform.net/natural-language-classifier/api/v1/classifiers/0e6935x475-nlc-2948",
  "classifier_id": "0e6935x475-nlc-2948",
  "created": "2018-12-10T17:42:31.823Z",
  "status_description": "The classifier instance is in its training phase, not yet ready to accept classify requests"
}
'''
