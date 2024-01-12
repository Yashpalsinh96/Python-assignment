def parse_encoded_string(encoded_string):
    parts = encoded_string.split('0+')

    first_name = parts[0]
    last_name = parts[1]
    student_id = parts[2].lstrip('0')

    result_dict = {
        "first_name": first_name,
        "last_name": last_name,
        "id": student_id
    }

    return result_dict

encoded_string = "Robert000Smith000123"
result = parse_encoded_string(encoded_string)
print(result)