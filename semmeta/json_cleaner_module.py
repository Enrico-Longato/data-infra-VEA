import json


class JsonCleaner:
    def __init__(self, input_path):
        self.input_path = input_path
        self.output_path = input_path.replace("_raw.json", "_cleaned.json")

    def clean_json(self):
        with open(self.input_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        cleaned_data = {}
        for key, value in data.items():
            if value is not None and value != "null":
                cleaned_data[key] = value

        with open(self.output_path, "w", encoding="utf-8") as f:
            json.dump(cleaned_data, f, indent=4, ensure_ascii=False)

        print(f"File successfully saved in: {self.output_path}")

 


