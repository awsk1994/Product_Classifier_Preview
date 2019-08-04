import json
import sys
from ibm_watson import NaturalLanguageClassifierV1
import Settings
import csv

results = []

def write_to_json_file(path, data):
    with open(path, mode='w') as file:
        json.dump(data, file, indent=4)

def classify(classifier_id, text, natural_language_classifier):
    classes = natural_language_classifier.classify(classifier_id, text).get_result()
    return classes

def compare_results(in_results, ans_path):
    answers = []
    with open(ans_path) as fp:
        reader = csv.reader(fp, delimiter=',')
        for _, [name, category] in enumerate(reader):
            json = {
                "name": name,
                "category": category
            }
            answers.append(json)

    compare_res_out = []
    count = 0
    for result in in_results:
        name, category = answers[count]['name'], answers[count]['category']
        compare_ans = (result['top_class'] == category)
        if compare_ans == True:
            compare_json = {
                "correct?": compare_ans,
                "name": name,
                "category": category
            }
        else:
            compare_json = {
                "correct?": compare_ans,
                "name": name,
                "category": category,
                "confidence": result['classes']
            }
        compare_res_out.append(compare_json)
        count += 1
    return compare_res_out

if len(sys.argv) < 2:
    print("Please enter classifier id to run classification.")
else:
    # Set up classifier.
    CLASSIFIER_ID = sys.argv[1]
    natural_language_classifier = NaturalLanguageClassifierV1(
        iam_apikey=Settings.API_KEY,
        url=Settings.URL)

    # Read cv file and classify
    cv_file = open(Settings.CROSS_VALIDATION_DATA_PATH)
    cv_texts = [line.replace("\n", "") for line in cv_file.readlines()]

    count = 0
    for cv_text in cv_texts:
        results.append(classify(CLASSIFIER_ID, cv_text, natural_language_classifier))
        count += 1
        print("count={} out of {}".format(count, len(cv_texts)))

    # write to output
    write_to_json_file(Settings.CLASSIFY_OUTPUT_PATH, results)
    print("Classify results={}".format(Settings.CLASSIFY_OUTPUT_PATH))

    # Compare results
    compare_res = compare_results(results, Settings.CROSS_VALIDATION_ANS_PATH)
    write_to_json_file(Settings.CV_COMPARE_OUTPUT_PATH, compare_res)
    print("Compare CV results={}".format(Settings.CROSS_VALIDATION_ANS_PATH))
