# Notes/Advices
  - In "./results/cv_compare_results/*", for the products with mismatch between predicted and actual answer, a more detailed json is displayed. In the json, **'category' key means the actual answer and 'confidence' key is confidence level for top guesses, whereby the highest confidence is chosen as the final prediction**.
 - Remember to remove API_KEY when you are done (if you are commiting to a public repo)
 - Delete classifier when classifier is no longer needed (to prevent more billing)
 - To see all classifiers, run src/list_classifiers.py

# Flow
1. Create Classifier Project on IBM Cloud
2. Organize data. 
 - Process raw data into training, cross-validation and cross-validation-answer set.
3. Create/Train classifier (using training set).
4. Test classifier with Cross Validation set.
5. Compare predicted and actual answers.
 - Compare and Analyze results using results from step 4 and the cross-validation-answer set.
6. Review and Improvements as necessary.

# Step 1: Create Classifier Project on IBM Cloud
1. You need to go to IBM Cloud, create an account and create a classifier project.
2. Get API_KEY and url from your classifier project. 
3. Input API_KEY to Credentials.py
4. Input url to Settings.py's URL

# Step 2: Organize Data
 - Code stored in "./Data/*" (refactoring folder name is risky at this point).
 - Run "./Data/create_simple_training_set.py" to start this process.

## Files
 - ./Data/Cross_Validation/*
   - Stores Cross Validation set's product name only.

 - ./Data/Cross_Validation_Ans/*
   - Stores Cross Validation set's product name and answer.

 - ./Data/Processed/*
    - Stores training set.

 - ./Data/Raw/*
    - Stores raw data - product category of 1source database and some products from 1source database.

 - ./Data/create_simple_training_set.py
   - is the main method
   - group_products(): group products into their category groups
   - process_input(products_by_category, max_item_count_per_category, cv_ratio): 
      - for each group, we need to split it into training and cross validation set (based on cv ratio). However, due to inconsistency sizes between groups, max_item_count_per_category is necessary as well, otherwise the classifier will be skewed torwards a particular category group.
   - output_processed_data_file(): write the data into files accordingly.
   - output_most_recent_processed_data_path(): write to "most_recent_output_paths.txt"

# Step 3: Create/Train Classifier.
 - Code stored in "./src/*"
 - First step is to modify INPUT_FILES section of "./src/Settings.py" You can directly copy the content of "./Data/most_recent_output_paths.txt" to INPUT_FILES section of Settings.py.
 - Also change NOTE accodingly.
 - Then, run "./src/create_classifier.py" to start the process. The output/response from API will give you the credential id. Remember it to track your classifier for future purposes.

# Step 4: Test Classifier
 - Code stored in "./src/*"
 - If you forgot your classifier, you can use "./src/list_classifiers.py" to see all the classifiers.
 - If it is still in "Training" status, you can keep checking it's progress by running something like "./src/check_classifier_status.py <classifier_id>"
 - Remember your classifier id and run something like "./src/classify_text.py <classifier_id>"
 - The results are outputted to "./results". 

# Step 5: Compare predicted and actual answers.
  - Code stored in "./results/*"
  - In "./results/*", the classify_output is just the predicted answers. The cv_compare_results is usually what I look at.
  - In "./results/cv_compare_results/*", for the products with mismatch between predicted and actual answer, a more detailed json is displayed. In the json, **'category' key means the actual answer and 'confidence' key is confidence level for top guesses, whereby the highest confidence is chosen as the final prediction**.
  - The tricky part about is:
	  1. classifier is there are 483 categories. That's actually a lot of categories for the typical classifier projects I have seen. (usually, they only have 4-5 categories)
	  2. Even for me, some products are not 'wrong' if it doesn't match the actual answer. For example, the actual category for "Red Bull Blue Edition, Blueberry Energy Drink" is "Energy & Healthy Drink", but the classifier predicted "Bottled Beverages & Drink Mixes". Is the classifier wrong? Not really. Given that this is only a classifier with no general knowledge in it, I think the classifier is doing pretty well here.

# Step 6: 
  - Code: I modified "./Data/create_simply_training.py" a bit in this step.
  - In this step, I tried different combinations of "key_identifier" (basically the inputs when I train the classifier) and assessed which type of key_identifier resulted in the best result. The combinations are tried are:
  	 - name + description
  	 - name + ingredients (up to the max character limit)
  	 - name only
   - My conclusion is key_identifier as "name only" had the best results - technically, it's "more understandable" results.

# Other Files:
"./src/delete_classifier.py": deletes classify. Must input classify id as input argument.

# Last Updated: 2019-08-04 05:18pm
