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



def main() -> None:
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")
    


if __name__ == "__main__":
    main()
