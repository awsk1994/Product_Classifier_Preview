import json
from ibm_watson import NaturalLanguageClassifierV1
import Settings

natural_language_classifier = NaturalLanguageClassifierV1(
	iam_apikey=Settings.API_KEY,
	url=Settings.URL)

classifiers = natural_language_classifier.list_classifiers().get_result()
print(json.dumps(classifiers, indent=2))