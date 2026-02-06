from typing import Any, List, Dict, Union, Optional
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    """
    abstract class that functions as processing interface for classes that inherit from it
    """

    @abstractmethod
    def process(self, data: any) -> str:
        """
        process the given data and return a string result
        """
        raise NotImplementedError


    @abstractmethod
    def validate(self, data: any) -> bool:
        """
        validate whether the given data is appropriate for this processor.
        """
        raise NotImplementedError


    def format_output(self, result: str) -> str:
        """
        default output formatting
        """
        return f"Outout: {result}"



class NumericProcessor(DataProcessor):
    """
    class to process numeric data
    """
    def process(self, data: any) -> str:
        if not self.validate(data):
            raise ValueError("Invalud numeric data")

        total = sum(data)
        avg = total / len(data)

        return f"Processed {len(data)} numeric values, sum={total}, ave={avg}"


    def validate(self, data: any) -> bool:

        if type(data) != list:
            return False

        if len(data) == 0:
            return False

        for value in data:
            if type(value) != int and type(value) != float:
                return False

        return True


    def format_output(self, result: str) -> str:
        return result


class TextProcessor(DataProcessor):
    """
    class to handle text data
    """
    def process(self, data: any) -> str:
        if not self.validate(data):
            raise ValueError("Invalid text data")

        txt: str = data.split()
        char_len = len(data)
        
        word_count = 0
        for word in txt:
            word_count += 1

        return f"Processed text: {char_len} characters, {word_count} words"

    def validate(self, data: any) -> bool:
        return type(data) == str


    def format_output(self, result: str) -> str:
        return result


class LogProcessor(DataProcessor):
    """
    class to process log data
    """
    def process(self, data: any) -> str:
        if not self.validate(data):
            raise ValueError("Invalid log entry")

        log: str = data.strip()
        level = ""

        if log.startswith("ERROR"):
            level = "ERROR"
        elif log.startswith("WARNING"):
            level = "WARNING"
        if log.startswith("INFO"):
            level = "INFO"

        parts = log.split(":", 1)
        message = parts[1].strip()

        return f"[ALERT]: {level} level detected: {message}"

    def validate(self, data: any) -> bool:
        if type(data) != str:
            return False

        if ":" not in data:
            return False

        return True

    def format_output(self, result: str) -> str:
        return result


def main() -> None:
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")
    
    data_test: List[data] = [
        [1, 2, 3, 4, 5],
        "Hello Nexus World",
        "Error: Connection timeout",
    ]

    class_processors: List[classes] = [
        NumericProcessor(),
        TextProcessor(),
        LogProcessor(),
    ]
    
    for process_class, data in zip(class_processors, data_test):
        print(f"Initializing {process_class.__class__.__name__}...")
        print(f"Processing data: {data}")
        try:
            result = process_class.process(data)
            print("Validaion: Data verified")
            print(f"Output: Processed {process_class.format_output(result)}\n")
        except Exception as e:
            print(f"Processing failed: {e}")



if __name__ == "__main__":
    main()









