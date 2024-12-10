from dataclasses import dataclass
from typing import Optional
from utils import get_input_lines
from advent9a import calculate_checksum

@dataclass
class FileBlock:
    file_id: str
    length: int
    empty_space: Optional[int] = 0

def create_disk(input_data):
    i = 0
    disk = []
    data = True
    for sector in input_data:
        if data:
            block = FileBlock(file_id=i, length=int(sector))
            disk.append(block)
            data = False
        else:
            disk[i].empty_space = int(sector)
            i += 1
            data = True
    return disk

def print_disk(disk):
    output_string = ""
    for file in disk:
        for _spot in range(file.length):
            output_string += str(file.file_id)
        for _empty_space in range(file.empty_space):
            output_string += "."
    return output_string

def find_leftmost_space(disk, file_candidate):
    for file_idx, file in enumerate(disk):
        if file.file_id == file_candidate.file_id:
            return -1
        if file.empty_space >= file_candidate.length:
            return file_idx
    return -1

def swap(good_spot_idx, move_file_idx, disk):
    preceding_file = disk[good_spot_idx]
    moving_file = disk[move_file_idx]
    total_space = preceding_file.empty_space
    preceding_file.empty_space = 0
    freed_space = moving_file.length + moving_file.empty_space
    moving_file.empty_space = total_space - moving_file.length
    # this is now the prior file that preceded moving file
    disk.insert(good_spot_idx + 1,moving_file)
    disk.pop(move_file_idx + 1)
    disk[move_file_idx].empty_space += freed_space
    return disk

def find_file(disk, file_id):
    # maybe make an index
    for file_idx, file in enumerate(disk):
        if file.file_id == file_id:
            return file_idx

def fix_space(disk):
    disk_length = len(disk)
    for i in range(disk_length - 1):
        file_id = disk_length - 1 - i
        file = find_file(disk, file_id)
        available_spot = find_leftmost_space(disk, disk[file])
        if available_spot >= 0:
            disk = swap(available_spot, file, disk)
    return disk

def calculate_checksum(disk):
    checksum = 0
    location = 0
    for block in disk:
        for i in range(block.length):
            checksum += location * block.file_id
            location += 1
        location += block.empty_space
    return checksum


if __name__ == "__main__":
    test = False
    input_data = get_input_lines('9', test)
    disk = create_disk(input_data[0])
    # print_disk(disk)
    fixed_disk = fix_space(disk)
    # print_disk(fixed_disk)
    print(calculate_checksum(fixed_disk))
