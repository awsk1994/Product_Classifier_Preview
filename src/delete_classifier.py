import json
import sys
from ibm_watson import NaturalLanguageClassifierV1
import Settings

if len(sys.argv) < 2:
    print("Please enter classifier id to delete")

else:
    CLASSIFIER_ID = sys.argv[1]
    natural_language_classifier = NaturalLanguageClassifierV1(
        iam_apikey=Settings.API_KEY,
        url=Settings.URL)

    status = natural_language_classifier.delete_classifier(CLASSIFIER_ID).get_result()
    print(json.dumps(status, indent=2))
