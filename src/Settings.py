import Credentials
import datetime
now_time = datetime.datetime.now().strftime("%Y%m%d_%H%M")

# IBM Cloud Classifier Project Information
URL = "https://gateway-tok.watsonplatform.net/natural-language-classifier/api"
METADATA_PATH = './metadata.json'
API_KEY = Credentials.API_KEY

# INPUT FILES:
# !!CHANGED OFTEN!! Update whenever you run data/create_simple_training_set.py
# Replace content of "most_recent_output_paths.txt" here:
NOTE = "normalized1_and_only_name_without_chinese"
TRAINING_DATA_PATH = "../Data/Processed/training_set_20190707_1904_normalized1_and_only_name_without_chinese.csv"
CROSS_VALIDATION_DATA_PATH = "../Data/Cross_Validation/Cross_Validation_Selected_20190707_1904_normalized1_and_only_name_without_chinese.txt"
CROSS_VALIDATION_ANS_PATH = "../Data/Cross_Validation_Ans/Cross_Validation_Selected_Ans_20190707_1904_normalized1_and_only_name_without_chinese.csv"

# OUTPUT Files:
CLASSIFY_OUTPUT_PATH = "../results/classify_output/classify_text_log_{}_{}.json".format(now_time, NOTE)
CV_COMPARE_OUTPUT_PATH = "../results/cv_compare_results/cv_compare_results_{}_{}.json".format(now_time, NOTE)
