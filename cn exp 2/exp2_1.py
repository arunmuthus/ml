def compute_crc(data: bytes, polynomial: int = 0x104C11DB7, initial_value: int = 0xFFFFFFFF) -> int:
    crc = initial_value
    for byte in data:
        crc ^= byte << 24
        for _ in range(8):
            crc = (crc << 1) ^ polynomial if crc & 0x80000000 else crc << 1
            crc &= 0xFFFFFFFF
    return crc

def compute_checksum(data: bytes) -> int:
    return sum(data) % 256

def simulate_file_transfer(file_path: str):
    try:
        with open(file_path, 'rb') as file:
            data = file.read()

        crc = compute_crc(data)
        checksum = compute_checksum(data)

        crc_valid = crc == compute_crc(data)
        checksum_valid = checksum == compute_checksum(data)

        print(f"CRC Check - Data is valid: {crc_valid}")
        print(f"Checksum Check - Data is valid: {checksum_valid}")

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")

file_path = "file.txt"
simulate_file_transfer(file_path)