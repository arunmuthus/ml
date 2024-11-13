def compute_crc(data: bytes, polynomial: int = 0x104C11DB7, initial_value: int = 0xFFFFFFFF) -> int:
    crc = initial_value
    for byte in data:
        crc ^= byte << 24
        for _ in range(8):
            if crc & 0x80000000:
                crc = (crc << 1) ^ polynomial
            else:
                crc <<= 1
            crc &= 0xFFFFFFFF
    return crc

def validate_crc(data: bytes, received_crc: int, polynomial: int = 0x104C11DB7) -> bool:
    return compute_crc(data, polynomial) == received_crc

def compute_checksum(data: bytes) -> int:
    return sum(data) % 256

def validate_checksum(data: bytes, received_checksum: int) -> bool:
    return compute_checksum(data) == received_checksum

def simulate_file_transfer(data: str):
    data_bytes = data.encode('utf-8')

    crc = compute_crc(data_bytes)
    checksum = compute_checksum(data_bytes)

    received_crc = crc
    received_checksum = checksum

    is_crc_valid = validate_crc(data_bytes, received_crc)
    is_checksum_valid = validate_checksum(data_bytes, received_checksum)

    print("CRC Check - Data is valid:", is_crc_valid)
    print("Checksum Check - Data is valid:", is_checksum_valid)

sample_data = "Hello, World!"
simulate_file_transfer(sample_data)