import ast
import re


def get_request_file_parameters_from_onclick(onclick_string):
    # e.g: "mojarra.jsfcljs('document.getElementById('form'),{'form:j_idtXXX')"
    if not onclick_string:
        return None

    # e.g: {'form:j_idtXXX':'form:j_idtXXX'}
    extracted_parameters = re.findall(r'\{.+\}', onclick_string)
    if not extracted_parameters:
        return None

    return ast.literal_eval(extracted_parameters.pop())
