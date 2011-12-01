Edit values in config.cfg to mirror your environment
	- megam_home -> location of megam
	- p2_home -> location of project folder

To run the various classifiers:

1. Run create_training_test_data.py for respective multiclass classifier
2. Run train_%s.py to train classifiers
3. Run %s_predict.py to generate predictions
4. Run eval_%s.py to evaluate classifier

tree-alt is the alternate tree that does the harder distinction first (WU9)