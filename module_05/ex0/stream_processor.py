from typing import Any, List, Dict, Union, Optional
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: any) -> str:
        raise NotImplementedError


    @abstractmethod
    def validate(self, data: any) -> bool:
        raise NotImplementedError


    def format_output(self, result: str) -> str:
        return f"Outout: {result}"


class NumericProcessor(DataProcessor):
    def process(self, data: any) -> str:
        if not self.validate(data):
            raise ValueError("Invalud numeric data")

        total = sum(data)
        avg = total / len(data)

        return f"Processed {len(data)} numeric values, sum={total}, avg={avg}"


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
    def process(self, data: any) -> str:
        if not self.validate(data):
            raise ValueError("Invalid log entry")

        log: str = data.strip()
        level = ""

        if log.startswith("ERROR"):
            level = "ALERT"
        elif log.startswith("WARNING"):
            level = "WARNING"
        elif log.startswith("INFO"):
            level = "INFO"

        parts = log.split(":", 1)
        message = parts[1].strip()

        return f"[{level}]: {parts[0].strip()} level detected: {message}"

    def validate(self, data: any) -> bool:
        if type(data) != str:
            return False

        if ":" not in data:
            return False

        word = data.split(":", 1)[0].strip()
        if not word.startswith(("ERROR", "WARN", "INFO")):
            return False

        return True

    def format_output(self, result: str) -> str:
        return result


def main() -> None:
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")
    
    data_test: List[data] = [
        [1, 2, 3, 4, 5],
        "Hello Nexus World",
        "ERROR: Connection timeout",
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
            if process_class.__class__.__name__.startswith("Numeric"):
                print("Validation: Numeric data verified")
            if process_class.__class__.__name__.startswith("Text"):
                print("Validation: Text data verified")
            if process_class.__class__.__name__.startswith("Log"):
                print("Validation: Log entry verified")
            print(f"Output: {process_class.format_output(result)}\n")
        except Exception as e:
            print(f"Processing failed: {e}")


    print("=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface...")

    #we are creating object out of the basetype which is DataProcessor
    #to illistrutate that we are create differnt object that follow the same interfecet
    #but to each its own implmenetnation, this is what polymorphiscm is about
    #we do this to show that we are following the interface, and that we actully understand polym
    #otherwise we would be creating, simple object that may work as the supposed object that inherit
    #from the base type, but not actually following the interface of the base class!


    Processors = [NumericProcessor(), TextProcessor(), LogProcessor()]

    demo_data = [
        [1, 2, 3],
        "Hello Nexus",
        "INFO: System ready",
    ]

    i = 1
    for processor, data in zip(Processors, demo_data):
        print(f"Result {i}: {processor.process(data)}")
        i += 1

    print("\nFoundation systems online. Nexus ready for advanced streams.")


if __name__ == "__main__":
    main()

