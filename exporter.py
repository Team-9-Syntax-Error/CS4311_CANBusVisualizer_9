import csv


class Exporter:

    @staticmethod
    def export_to_csv():
        """
        Tester for Kali, finished code will have user select a project file instead of
        manually passing Python Dict() parameter
        """
        return

    @staticmethod
    def create_csv(py_dict, file_name, path):
        with open(path + "/" + file_name + ".csv", 'w') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=Exporter.create_field_names(py_dict))
            writer.writeheader()
            writer.writerow(py_dict)
        return 1

    @staticmethod
    def create_field_names(py_dict):
        key_list = []
        for key in py_dict:
            key_list.append(key)
        return key_list
