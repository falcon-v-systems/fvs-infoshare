import sys
import argparse

def parse_file(file_name):
    with open(file_name, "r") as f:
            file_lines = f.readlines()
            result_list = [int(x) for x in file_lines]
    return result_list


parser = argparse.ArgumentParser()
parser.add_argument("file_name")
result_file = parser.parse_args().file_name

result_data = parse_file(result_file)
input_data = parse_file("numbers.txt")

if not set(input_data) == set(result_data):
      print("Set of result numbers is different from the input data")
      sys.exit()

nums1_sum = sum(result_data[::2])
nums2_sum = sum(result_data[1::2])
print(f"Your score: {nums1_sum - nums2_sum}")
