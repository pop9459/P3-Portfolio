import re
import os

def read_ips():
	# read all content of file as string
	file_path = os.path.join(os.path.dirname(__file__), "ips.txt")
	ips_raw_lines = open(file_path, "r").read()
	
	# put all ips in a list
	ips = ips_raw_lines.split(" ")
	
	# filter out double ips, only unique ips in the list
	filtered_ips = list()
	for ip in ips:
		if ip not in filtered_ips:
			filtered_ips.append(ip)
	
	# return list
	return filtered_ips


def get_pattern():
	# see https://cs50.harvard.edu/python/2022/psets/7/numb3rs/
	# uses regex to determine of IP address is a valid IP in the range:
	# 47.82.11.0 - 47.82.11.255
    # return the pattern, so something like r"^47.....$"
	return r"^47\.82\.11\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])$"


def filter_ips(all_ips):
	correct = list()
	# receives a list with a lot of possible IP addresses
	ips = read_ips()

	# filters out only valid addresses using the function: get_pattern()
	regex_pattern = get_pattern()
	for ip in ips:
		if re.match(regex_pattern, ip) is not None:
			correct.append(ip)

	# returns a list with valid IP addresses
	# the list contains no identical IP's, so filter for doubles.
	return correct


def main():
	# do not change below code
	all_ips = read_ips()
	correct_ips = filter_ips(all_ips)
	for p in correct_ips:
		print(p)
	print(len(correct_ips))


if __name__ == "__main__":
	main()
