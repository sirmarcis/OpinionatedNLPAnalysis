import sys

from json_helper import get_old_alchemy_data, get_test_json, get_single_json_to_play_with
from article_data_extraction import perform_article_theme_extraction, get_alchemy_langauge_obj

######################################################################################
# Main function

def main():
	## We have a main function instead of just having the code in the main if statement so we can return early in case of error
	if len(sys.argv) < 2:
		print "error: usage. Please input AlchemyAPI key to use."
		exit(1)
	alchemy_language, err_code = get_alchemy_langauge_obj(sys.argv[1])
	if err_code == 1 or err_code == 2:
		if err_code == 1:
			print "Alchemy error: Incorrect API key! (dumbass)"
		else:
			print "Alchemy error: out of API calls for the day! (rip)"
		return 

	all_json_files_dir = get_test_json()
	old_alchemy_data = get_old_alchemy_data()
	# print "loaded all test files"

	# loop to go over all articles and extract article themes and sentiment
	for i, json_filename in enumerate(all_json_files_dir.keys()):
		json_file_data = all_json_files_dir[json_filename]["Data"]
		if json_filename in old_alchemy_data:
			print "already extracted data for article: ", json_filename
		else:
			print "on article[", i, "] article name:", json_filename
			can_continue_p = perform_article_theme_extraction(json_file_data, json_filename, alchemy_language)
			if not can_continue_p:
				print "ran out of API calls on article: " + json_filename + ", exiting program.."
				return
	print "finished all articles!"

	#test_file, test_filename = get_single_json_to_play_with(all_json_files_dir)
	#test_file_data = test_file["Data"] # this gives us the actual article text
	#perform_article_theme_extraction(test_file_data, test_filename.split('.')[0], alchemy_language)

if __name__ == "__main__":
	main()

	

######################################################################################
