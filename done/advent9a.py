from utils import get_input_lines

def create_disk(input_data):
    i = 0
    disk = []
    data = True
    for sector in input_data:
        if data:
            for _file_block in range(int(sector)):
                disk.append(i)
            i += 1
            data = False
        else:
            for _empty_space in range(int(sector)):
                disk.append(".")
            data = True
    return disk

def print_disk(disk):
    for block in disk:
        print(block, end = "")
    print("")

def swap(empty_idx, full_idx, disk):
    data = disk[full_idx]
    disk[empty_idx] = data
    disk[full_idx] = "."
    return disk

def count_free_space(disk):
    free = 0
    for block in disk:
        free += block == "."
    return free

def fix_free_space(disk, free_spots):
    def get_last_full_block(disk):
        for block_idx, block in enumerate(reversed(disk)):
            if block == ".":
                pass
            else:
                return len(disk) - block_idx - 1

    def get_first_empty_block(disk):
        for block_idx, block in enumerate(disk):
            if block == ".":
                return block_idx
            else:
                pass

    for _free_spot in range(free_spots):
        first = get_first_empty_block(disk)
        last = get_last_full_block(disk)
        disk = swap(first, last, disk)
    return disk

def calculate_checksum(disk):
    checksum = 0
    for block_idx, block in enumerate(disk):
        if block == ".":
            return checksum
        checksum += block_idx * block

if __name__ == "__main__":
    test = True
    input_data = get_input_lines('9', test)
    disk = (create_disk(input_data[0]))
    cleaned = fix_free_space(disk, count_free_space(disk))
    print(calculate_checksum(cleaned))
