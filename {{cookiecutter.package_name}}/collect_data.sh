pip install kaggle --upgrade
export KAGGLE_USERNAME={{cookicutter.kaggle_username}}
export KAGGLE_KEY={{cookicutter.kaggle_key}}

kaggle competitions download -c {{cookicutter.competition_slug}} --path {{cookicutter.path_to_data}}