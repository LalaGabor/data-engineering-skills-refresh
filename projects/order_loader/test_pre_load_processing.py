from pre_load_processing import clean_records

def test_clean_records():
    list_guy = []
    dict_guy = {}
    dict_guy["name"] = " Alice "
    dict_guy["email"] = " bob@gmail.COM   "
    dict_guy["username"] = " chickkerTT "
    list_guy.append(dict_guy)
    test_item = clean_records(list_guy)
    assert test_item[0]["name"] == "alice"

#test_clean_records()