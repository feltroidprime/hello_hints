STARK = 0x800000000000011000000000000000000000000000000000000000000000001


def to_int(value: str | int):
    if isinstance(value, str):
        value = value.strip()  # Trim whitespaces
        if value.lower().startswith("0x"):
            try:
                return int(value, 16)
            except ValueError:
                raise ValueError(f"Invalid hexadecimal value: {value}")
        else:
            try:
                return int(value)
            except ValueError:
                raise ValueError(f"Invalid decimal value: {value}")
    elif isinstance(value, int):
        return value
    else:
        raise TypeError(f"Expected str or int, got {type(value).__name__}")


def to_hex_str(value: str | int):
    if isinstance(value, str):
        value = value.strip()  # Trim whitespaces
        if value.lower().startswith("0x"):
            try:
                # Validate hexadecimal and return in lowercase
                return "0x" + hex(int(value, 16))[2:].lower()
            except ValueError:
                raise ValueError(f"Invalid hexadecimal value: {value}")
        else:
            try:
                # Convert decimal string to int then to hex
                return hex(int(value)).lower()
            except ValueError:
                raise ValueError(f"Invalid decimal value: {value}")
    elif isinstance(value, int):
        return hex(value).lower()
    else:
        raise TypeError(f"Expected str or int, got {type(value).__name__}")


def bigint_split(x: int, n_limbs: int, base: int):
    coeffs = []
    degree = n_limbs - 1
    for n in range(degree, 0, -1):
        q, r = divmod(x, base**n)
        coeffs.append(q)
        x = r
    coeffs.append(x)
    return coeffs[::-1]


def felt252_to_uint64(felt: int) -> list:
    assert 0 <= felt < STARK, f"felt252 must be less than {STARK}"
    return bigint_split(felt, 4, 2**64)


def felt252_array_to_uint64_array(felt_array: list) -> list:
    res = []
    for felt in felt_array:
        res.extend(felt252_to_uint64(felt))
    return res
