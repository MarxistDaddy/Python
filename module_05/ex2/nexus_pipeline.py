from abc import ABC, abstractmethod
from typing import List, Any, Dict, Union, Optional, Protocol


#protocol class!
class ProcessingStage(Protocol):
    def process(self, data: Any) -> Any:
        ...

#abstract class that initliazes, name, list of processes, and stats variable that will be returned!
class ProcessingPieline(ABC):
    def __init__(self, pipeline_id: str):
        #self.piepline_id = pipeline_id
        self.stages: list[ProcessingStage] = []
        self.stats: Dic[str, int] = {
                "processed": 0,
                "errors": 0,
                "time": 0.0,
            }

    def add_stage(self, stage: ProcessingStage) -> None:
        self.stage.append(stage)

    def process(self, data: Any) -> Any:
        start = time.time()

        try:
            for stage in self.stages:
                data = stage.process(data)
            self.stats["processed"] += 1
            return data

        except Exception as e:
            self.stats["errors"] += 1
            print(f"[PIPELINE ERROR] {e}")
            return None

        finally:
            self.stats["time"] += time.time() - start


    @abstractmethod
    def process(self, data: Any) -> Union[str, Any]:
        ...

#create 3subclas of procotol
#returns dict
class InputStage:
    def process(self, data: Any) -> Dict[str, Any]:
        return {
            "raw": data,
            "status": "received"
        }


#returns dict
def TransformStage:
    def process(self, data: dict[str, Any]) -> Dict[str, Any]:
        data["length"] = len(str(data["raw"]))
        data["transformed"] = True
        return data


#returns str
def OutputStage:
    def process(self, data: dict) -> str:
        return f"Final Output: {data}"


#adapters these are the subclasses of abstract class!

class JSONAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: int)
        super().__init__()
        self.pipeline_id = pipeline_id


    def process(self, data: Any) -> str:
        result = self.run(data)
        return f"[JSON PIPELINE {self.pipeline_id}] {result}"

class CSVAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: int):
        super().__init__()
        self.pipeline_id = pipeline_id

    def process(self, data: Any) -> str:
        result = self.run(data)
        return f"CSV PIPELINE {self.pipeline_id}] {result}"

class StreamAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: int)
        super().__init__()
        self.pipeline_id = pipeline_id

    def process(self, data: Any) -> str:
        result = self.

        
def main():
    



if __name__ == "__main__":
    main()

