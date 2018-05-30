from json import load as json_load

"""
Supports swagger v2
"""


def get_dict_from_json(file_path):
    with open(file_path) as json_data:
        return json_load(json_data)


def tag_section(text, level):
    return " ".join(["#"*level, text])


def tag_bold(text):
    return "**".join(["", text, ""])


def tag_italic(text):
    return "*".join(["", text, ""])


def tag_code(text, lang_name=""):
    return "\n".join([
        "```{}".format(lang_name),
        text,
        "```"])


def build_section_info(info_dict):

    res = []
    res.append(tag_section(info_dict["title"], 1))
    for key in ["description", "version"]:
        res.append(tag_section(key, 2))
        res.append(info_dict[key])
        res.append("\n")
    return res


REST_VERBS = ["get", "post", "put", "patch", "delete"]


def get_table_responses(responses_dict):

    res = []
    res.append("| Code | Description |")
    res.append("| --- | --- |")
    for key, sub_dict in responses_dict.items():
        res.append("|".join(["", key, sub_dict["description"], ""]))
    res.append("\n")
    return res


def get_parameters_table(prm_list_of_dict):

    res = []
    key_list = ["name", "required", "in", "description", "type"]
    if prm_list_of_dict:
        res.append("|".join(["", "|".join(key_list), ""]))
        res.append(" --- ".join(["|"]*(len(key_list)+2)))
        for prm_dict in prm_list_of_dict:
            res.append("|".join(["", "|".join([str(prm_dict[key]) for key in key_list]),""]))
    else:
        res = ["none"]
    res.append("\n")
    return res


def get_list_italic(word_list, default="None"):

    if word_list:
        var_list = ", ".join(word_list)
    else:
        var_list = default
    return tag_italic(var_list)


def get_section_with_val(src_dict, key, level, default="None"):

    res = []
    res.append(tag_section(key.capitalize(), level))
    if not isinstance(src_dict.get(key), str):
        res.append(default)
    elif isinstance(src_dict.get(key), str):
        res.append(src_dict.get(key, default))
    elif isinstance(src_dict.get(key), list):
        res.append(get_list_italic(src_dict.get(key)))
    res.append("\n")

    return res


def get_verb_md(verb_dict):

    res = []

    res.extend(get_section_with_val(verb_dict, "summary", 4))
    res.extend(get_section_with_val(verb_dict, "description", 4))
    res.extend(get_section_with_val(verb_dict, "operationId", 4))

    res.append(tag_section("Parameters", 4))
    res.extend(get_parameters_table(verb_dict["parameters"]))

    res.append(tag_section("Responses", 4))
    res.extend(get_table_responses(verb_dict["responses"]))

    res.extend(get_section_with_val(verb_dict, "tags", 4))

    return res


def build_path_section(path_name, path_dict):
    res = []

    res.append(tag_section(path_name, 2))
    for verb in REST_VERBS:
        if path_dict.get(verb):
            res.append(tag_section(verb, 3))
            res.extend(get_verb_md(path_dict[verb]))
            res.append("\n")

    return res


def build_api_desc(sw_dict):
    # TODO : host key
    # TODO : security

    md = []

    md.extend(build_section_info(sw_dict["info"]))
    md.append(tag_section("Routes", 1))
    for path_name, path_dict in sw_dict["paths"].items():
        md.extend(build_path_section(path_name, path_dict))

    return "\n".join(md)


def sw_to_md(file_in, file_out="swagger.md"):
    file_content = build_api_desc(get_dict_from_json(file_in))
    with open(file_out, "w") as f:
        f.write(file_content)
