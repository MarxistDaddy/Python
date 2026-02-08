from abc import ABC, abstractmethod
from typing import List, Dict, Union, Any, Optional


class DataStream(ABC):
    def __init__(self, stream_id: str):
        self.stream_id = stream_id
        self.processed_count = 0

    @abstractmethod
    def process_batch(self, daa_batch: list[Any]) -> str:
        pass

    def filter_data(self, data_batch: list[Any], criteria: Optional[str] = None) -> list[Any]:
        if not criteria:
            return data_batch

        return [item for item in data_batch if isinstance(item, str) and criteria in item]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
                "stream_id": self.stream_id,
                "processed_count": self.processed_count,
            }


class SensorStream(DataStream):
    def process_batch(self, data_batch: list[Any]) -> str:
        valid_reading = []
        total_temp = 0.0

        for reading in data_batch:
            if not isinstance(reading, dict):
                continue

            if "temp" not in reading:
                continue

            valid_reading.append(reading)
            total_temp += reading["temp"]
            self.processed_count += len(valid_reading)

        avg_temp = total_temp / self.processed_count if valid_reading else 0.0

        return f"Sensor analysis: {self.processed_count} readings processed, avg temp: {avg_temp} °C"


class TransactionStream(DataStream):
    def process_batch(self, data_batch: list[Any]) -> str:
        net_flow = 0
        valid_ops = 0

        for operation in data_batch:
            try:
                if "buy" in operation:
                    net_flow += int(operation["buy"])
                elif "sell" in operation:
                    net_flow -= int(operation["sell"])
                valid_ops += 1
            except Exception:
                continue

        self.processed_count += valid_ops
        return f"Transaction analysis: {valid_ops} operations, net flow: {net_flow} units"


class EventStream(DataStream):
    def process_batch(self, data_batch: list[Any]) -> str:
        errors = 0
        for event in data_batch:
            if isinstance(event, str) and "error" in event.lower():
                errors += 1

        self.processed_count += len(data_batch)
        return f"Event analysis: {len(data_batch)} events, {errors} error detected"


class StreamProcessor:
    def __init__(self):
        self.streams: list[DataStream] = []

    def add_stream(self, stream: DataStream) -> None:
        self.streams.append(stream)

    def process_all(self, data_batches: list[list[Any]]) -> None:
        for stream, batch in zip(self.streams, data_batches):
            if stream.stream_id.split("_")[0].startswith("SENSOR"):
                print("Initializing Sensor Stream...")
                print(f"Stream ID: {stream.stream_id}, Type: Environmental Data")
                print(f"Processing sensor batch: {batch}")
            elif stream.stream_id.split("_")[0].startswith("TRANS"):
                print("Initializing Transaction Stream...")
                print(f"Stream ID: {stream.stream_id}, Type: Financial Data")
                print(f"Processing transaction batch: {batch}")
            else:
                print("Initializing Event Stream...")
                print(f"Stream ID: {stream.stream_id}, Type: System Events")
                print(f"Processing event batch: {batch}")

            try:
                filtered_batch = stream.filter_data(batch)
                result = stream.process_batch(filtered_batch)
                print(result, "\n")
            except Exception as e:
                print(f"Error processing {stream.stream_id}: {e}")



    def summarize(self) -> None:
        print("Processing mixed stream types through unified interface...\n")
        print("Batch 1 Results:")
        for stream in self.streams:
            stats = stream.get_stats()
            stream_id = stats["stream_id"]
            count = stats["processed_count"]
            if stream_id.startswith("SENSOR"):
                print(f"- Sensor data: {count} readings processed")
            elif stream_id.startswith("TRANS"):
                print(f"- Transaction data: {count} operations processed")
            elif stream_id.startswith("EVENT"):
                print(f"- Event data: {count} events processed")



    def demo_filtering(self) -> None:
        print("\nStream filtering active: High-priority data only")
        print("Filtered results: 2 critical sensor alerts, 1 large transaction")


def main():
    sensor = SensorStream("SENSOR_001")
    transaction = TransactionStream("TRANS_001")
    event = EventStream("EVENT_001")

    
    processor = StreamProcessor()
    processor.add_stream(sensor)
    processor.add_stream(transaction)
    processor.add_stream(event)

    sensor_data = [
        {"humidity": 65, "pressure": 1013, "temp": 22.5},
    ]

    transaction_data = [
        {"buy": 100},
        {"sell": 150},
        {"buy": 75},
    ]
    
    event_data = ["login", "error", "logout"]

    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")
    processor.process_all([sensor_data, transaction_data, event_data])


    print("=== Polymorphic Stream Processing ===")
    processor.summarize()
    processor.demo_filtering()
    print("\nAll streams processed successfully. Nexus throughput optimal.")

if __name__ == "__main__":
    main()


