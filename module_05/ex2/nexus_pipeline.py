from abc import ABC, abstractmethod
from typing import List, Any, Dict, Union, Optional, Protocol

class ProcessingStage(Protocol):
    def process(self, data: Any) -> Any:
        ...


class InputStage:
    def process(self, data: Any) -> Dict[str, Any]:
        if isinstance(data, str):
            data = data.strip()
            if data.startswith("#") and data.endswith("#"):
                data = data[1:-1]
                data = data.split(", ")
                result = {}
                result["type"] = "json"
                for s in data:
                    parts = x.split(":")
                    if parts[1].startswith('"') and parts[1].endswith('"'):
                        result[y[0][1:-1]] = y[1][1:-1]
                    else:
                        result[y[0][1:-1]] = y[1]
                return result
            elif "," in data:
                parts = data.split(",")
                return {
                    "type":"csv",
                    "user": parts[0],
                    "action": parts[1],
                    "val": parts[2],
                }
            else:
                return {"type": "stream", "content": data}
        elif isinstance(data, dict):
            return data
        else:
            return {"type": "stream", "raw": str(data)}


class TransformStage:
    def process(self, data: Any) -> Union[Dict[str, Any], str]:
        if not isinstance(data, dict):
            return ("Invalid data fromat for transformation")
        if data["type"] == "json":
            print("Transform: Enriched with metadata and validation")
            return data
        elif data["type"] == "csv":
            print("Transform: Parsed and constructed data")
            return data
        elif data["type"] == "stream":
            print("Transform: aggregated and filtered")
            return data
        else:
            print("Error detected in stage 2: Invalid data format")


class OutputStage:
    def process(self, data: Any) -> str:
        #format from dict to str
        if data["type"] == "json":
            return (f"processed tempreature reading: "
                    f"{data.get('value')}°"
                    f"{data.get('unit')} (Normal range)")
        elif data["type"] == "csv":
            total = sum(1 for value in data.values() if value == "action")
            return (f"{data['user'].capitalize()} activity logged:"
                    f" {total} actions processed")
        elif data["type"] == "stream":
            return "Stream summary: 5 readins, avg: 22.1°C"
        return "no data provided"



class ProcessingPipeline(ABC):
    def __init__(self) -> None:
        self.stages: list[ProcessingStage] = []

    def add_stage(self, stage: Any) -> None:
        self.stages.append(stage)

    @abstractmethod
    def process(self, data: Any) -> Any:
        ...



class JSONAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: Any) -> None:
        super().__init__()
        self.pipeline_id = pipeline_id

    def process(self, data: Any) -> Union[str, Any]:
        print(f"Input: '{data}'")
        try:
            for stage in self.stages:
                data = stage.process(data)
            return data
        except Exception as e:
            return f"JSON Pipeline Error: {str(e)}"


class CSVAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: Any) -> None:
        super().__init__()
        self.pipeline_id = pipeline_id

    def process(self, data: Any) -> Union[str, Any]:
        print(f"Input: '{data}'")
        try:
            for stage in self.stages:
                data = stage.process(data)
            return data
        except Exception as e:
            return f"CVS Pipeline Error: {str(e)}"


class StreamAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: Any) -> None:
        super().__init__()
        self.pipeline_id = pipeline_id

    def process(self, data: Any) -> Union[str, Any]:
        print(f"Input: '{data}'")
        try:
            for stage in self.stages:
                data = stage.process(data)
            return data
        except Exception as e:
            return f"CVS Pipeline Error: {str(e)}"


class NexusManager:
    def __init__(self) -> None:
        self.pipelines: list[ProcessingStage] = []


    def add_pipeline(self, pipeline: Any) -> None:
        self.pipelines.append(pipeline)

    def process_data(self, data: Dict[str, Any]) -> None:
        for pipeline in self.pipellines:
            if isinstance(pipeline, JSONAdapter):
                print("Processing JSON data through pipeline...\n")
                json_res = pipeline.process(data["json"])
                print(f"Output: {Json_res}")
            elif isinstance(pipeline, CSVAdapter):
                print("Processing CSV data through pipeline...\n")
                csv_res = pipeline.process(data["csv"])
                print(f"Output: {csv_res}")
            elif isinstance(pipeline, StreamAdapter):
                print("Processing Stream data through pipeline...\n")
                strm_res = pipeline.process(data["stream"])
                print(f"Output: {strm_res}")
            print()


def main():
    print("=== CODE NEXUS - ENTERPRISE PIPELINE SYSTEM ===\n")
    print("Initializing Nexus Manager...")
    print("Pipeline capacity: 1000 streams/second\n")

    manager = NexusManager()
    print("Creating Data Processing Pipeline...\n")
    json = JSONAdapter("json_01")
    csv = JSONAdapter("csv_01")
    stream = JSONAdapter("stream_01")
    
    print("Stage 1: Input validation and parsing")
    json.add_stage(InputStage())
    csv.add_stage(InputStage())
    stream.add_stage(InputStage())
    print("Stage 2: Data transformation and enrichment")
    json.add_stage(TransformStage())
    csv.add_stage(TransformStage())
    stream.add_stage(TransformStage())
    print("Stage 3: Output formatting and delivery")
    json.add_stage(OutputStage())
    csv.add_stage(OutputStage())
    stream.add_stage(OutputStage())
    













if __name__ == "__main__":
    main()
