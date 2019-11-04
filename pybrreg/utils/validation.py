import datetime


def multiply_reduce(aval, bval):
    return sum([(a * b) for (a, b) in zip(aval, bval)])


def validate_party(value):
    if len(value) == 11:
        return validate_ssn(value)
    elif len(value) == 9:
        return validate_org_no(value)
    else:
        err_msg = "{} is not a valid SSN or organisation number".format(value)
        raise ValueError(err_msg)


def validate_ssn(value):
    if int(value[0]) >= 4:
        value = str(int(value[0]) - 4) + value[1:]

    day = int(value[:2])
    month = int(value[2:4])
    year2 = int(value[4:6])
    inum = int(value[6:9])
    try:
        if 000 <= inum < 500:
            datetime.date(1900 + year2, month, day)
        if 500 <= inum < 750 and year2 > 54:
            datetime.date(1800 + year2, month, day)
        if 500 <= inum < 1000 and year2 < 40:
            datetime.date(2000 + year2, month, day)
        if 900 <= inum < 1000 and year2 > 39:
            datetime.date(1900 + year2, month, day)
    except ValueError:
        raise ValueError('invalid!')

    digits = map(int, list(value))
    weight_1 = [3, 7, 6, 1, 8, 9, 4, 5, 2, 1, 0]
    weight_2 = [5, 4, 3, 2, 7, 6, 5, 4, 3, 2, 1]

    if multiply_reduce(digits, weight_1) % 11 != 0:
        raise ValueError('invalid!')
    if multiply_reduce(digits, weight_2) % 11 != 0:
        raise ValueError('invalid!')
    return value


def validate_org_no(value):
    digits, checksum = map(int, list(value)[:8]), int(value[-1])
    weights = [3, 2, 7, 6, 5, 4, 3, 2]
    mr = multiply_reduce(digits, weights)
    result = mr % 11
    if result == 0:
        calculated_checksum = 0
    else: 
        calculated_checksum = 11 - result
    if calculated_checksum == 10 or calculated_checksum != checksum:
        raise ValueError("{} is not a valid organisation number".format(value))
    return value

