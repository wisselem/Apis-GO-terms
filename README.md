# Apis-GO-terms

## Filtering GO Terms

### Beginner Friendly

Created by Emily Wissel

6 / 14 / 2018

1.  First, you need to create a file with the GO terms you want included for your analysis. This file has to be formatted properly or the whole pipeline doesn’t work (see below). It would be best to use a .txt file (with no encoding), but a .csv or .tsv will work as well. 
    - Each term (example term - GB40006) must be its own row. In other words, the input file must be one column, where each row has a single GB term and nothing else. Look at *example_input.txt* if you need clarification.
    - Save this file in the same folder you will put the other pieces of this pipeline. This is very important!!

2.  Download the second input file downloaded in the same folder as your reference input file. I use the *go_id.txt* file included above. I recommend not changing the name or format of the file - you’ll only create more work for yourself if you do.

3.  Download the python script *pipeline_GO_terms.py*, and save it to the same folder as the other files. If your input file from step one has a name other than 'input.txt', you need to either change the name of the file to 'input.txt' or change the first line of the script to the proper name. 

4. Save any changes you may have made to the script, and you are now ready to run it! You can run if in your terminal by typing `python pipeline_GO_terms.py`. A list of your filtered GB:GO terms will be created in the new file *filtered_gbid_to_go.tab*. 
    - If you get the error message 'No such file or directory', then you need to change your current working directory in terminal to the directory where you saved all these files. For example, if you are on your desktop and need to go to a subfolder on your desktop, type `cd subfolder/` to enter that directory. 
