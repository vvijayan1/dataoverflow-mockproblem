import unittest
from tempfile import TemporaryDirectory
from csv import reader, writer
import os
import sys
sys.path.append(os.path.realpath("code/"))
from script import location_aggregation


def read_output_file(output_file):
    if not os.path.isfile(output_file):
        raise FileNotFoundError(f"File {output_file} doesn't exist")
    data = {}
    num_rows = 0
    with open(output_file) as ifh:
        csv_reader = reader(ifh, delimiter="\t")
        for row in csv_reader:
            if len(row) != 2:
                raise Exception(f"Output file expected to have only 2 columns, {len(row)} found!")
            locations = sorted(list(map(lambda x: int(x.strip()), row[1].split(","))))
            data[int(row[0])] = locations
            num_rows += 1
    return data, num_rows
     

class TestLocationAggregation(unittest.TestCase):

    def test_single_file(self):
        with TemporaryDirectory() as tmp_dir:
            dir_path = tmp_dir
            input_file_path = os.path.join(dir_path, "input_file")
            with open(input_file_path, "w") as ifh:
                csv_writer = writer(ifh, delimiter="\t")
                csv_writer.writerow(["USER_ID", "LOCATION_ID"])
                csv_writer.writerow(["1234", "1"])
                csv_writer.writerow(["1234", "1"])
                csv_writer.writerow(["1234", "3"])
                csv_writer.writerow(["1201", "2"])
            output_file_path = os.path.join(dir_path, "output_file")
            location_aggregation([input_file_path], output_file_path)
            data, num_rows = read_output_file(output_file_path)
            expected_results = {1234 : [1,3], 1201 : [2]}
            self.assertEqual(len(expected_results), num_rows)
            self.assertEqual(data, expected_results)


    def test_empty_input_file(self):
        with TemporaryDirectory() as tmp_dir:
            dir_path = tmp_dir
            input_file_path = os.path.join(dir_path, "input_file")
            with open(input_file_path, "w") as ifh:
                csv_writer = writer(ifh, delimiter="\t")
                csv_writer.writerow(["USER_ID", "LOCATION_ID"])
            output_file_path = os.path.join(dir_path, "output_file")
            location_aggregation([input_file_path], output_file_path)
            data, num_rows = read_output_file(output_file_path)
            expected_results = {}
            self.assertEqual(len(expected_results), num_rows)
            self.assertEqual(data, expected_results)


    def test_multiple_input_file(self):
        with TemporaryDirectory() as tmp_dir:
            dir_path = tmp_dir
            input_file_path_one = os.path.join(dir_path, "input_file_1")
            with open(input_file_path_one, "w") as ifh:
                csv_writer = writer(ifh, delimiter="\t")
                csv_writer.writerow(["USER_ID", "LOCATION_ID"])
                csv_writer.writerow(["1234", "1"])
                csv_writer.writerow(["1234", "1"])
                csv_writer.writerow(["1234", "3"])
                csv_writer.writerow(["1201", "2"])
            input_file_path_two = os.path.join(dir_path, "input_file_2")
            with open(input_file_path_two, "w") as ifh:
                csv_writer = writer(ifh, delimiter="\t")
                csv_writer.writerow(["USER_ID", "LOCATION_ID"])
                csv_writer.writerow(["1234", "3"])
                csv_writer.writerow(["1201", "3"])
                csv_writer.writerow(["1201", "2"])
            output_file_path = os.path.join(dir_path, "output_file")
            location_aggregation([input_file_path_one, input_file_path_two], output_file_path)
            data, num_rows = read_output_file(output_file_path)
            expected_results = {1234 : [1,3], 1201 : [2,3]}
            self.assertEqual(len(expected_results), num_rows)
            self.assertEqual(data, expected_results)


if __name__ == "__main__":
    unittest.main()
    
    



