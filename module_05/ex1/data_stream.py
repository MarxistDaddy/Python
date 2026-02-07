from abc import ABC, abstractmethod
from typing import List, Dict, Union, Any, Optional


#this is our abstract method, its an interface that subclasses have to follow if they inherit from
#this!
class DataStream(ABC):
    #initliaze steam id thats a string, and count for processed
    def __init__(self, stream_id: str):
        self.stream_id = stream_id
        self.processed_count = 0

    @abstractmethod
    def process_batch(self, daa_batch: list[Any]) -> str:
        pass
        #raise notimeplementerror | choose how to implemnet it 

    #default filtering data, it filters data: optional to use! can be overriden
    def filter_data(self, data_batch: list[Any], criteria: Optional[str] = None) -> list[Any]:
        if not criteria:    #check if cirecor has a value or not to filter!
            return data_batch

        #we return the filtered criteria!
        return [item for item in data_batch if isinstance(item, str) and criteria in item]


    #optional methods that takes nothing but returns a dict!
    #==> its supposed to return a value union made up of 3 elements!
    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        #return a dict that contains, stream_id and count reference!
        return {
                "stream_id": self.stream_id,
                "processed_count": self.processed_count,
            }


#sunclass of abstract class, stream for sensor data!
class SensorStream(DataStream):

    #override abtract method:
    def process_batch(self, data_batch: list[Any]) -> str:
        # Expecting data like [{'temp': 22.5, 'humidity': 65, 'pressure': 1013}, ...]
        # a list of dictionareoes, takes type of climate, and its value!
        valid_reading = []
        totam_temp = 0.0

        #for vvalue which is a dict in the data_batch list, count the total tempru in tmp
        for reading in data_batch:
            try:
                temp = reading.get("temp", 0)   #this will raise an error!
                total_temp += temp
                valid_reading += [reading]      #add reading to the valid
            except Exception:
                continue                        #skip non "temp" values that dont exit in dict
        
        #this belongs to the abstract class! how did it come here?? when was it createde!
        self.processed_count += len(valid_reading)

        #count only the avg temp if we have a valid_reading is full
        #means we have value of temp in dict!
        avg_temp = total_temp / len(valid_reading) if valid_reading else 0.0

        return f"Sensor anysis: {len(valid_reading)} readings processed, avg temp: {avg_temp} °C"


class TransactionStream(DataStream):
    #list of dicts that contains transction: [{'buy': 100}, {'sell': 150}]...
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
    
    #list of strings: "logic", "error", "logout"
    def process_batch(self, data_batch: list[Any]) -> str:
        errors = 0
        for event in data_batch:
            if isinstance(event, str) and "error" in event.lower():
                errors += 1

        self.processed_count += len(data_batch)
        return f"Event anasys: {len(data_batch)} events, {errors} error (s) detected"


#handles multiple streams polymorphosically!
class StreamProcessor:
    #initialize an empty list, that will later contain all stream processors
    def __init__(self):
        #empty list!
        self.streams: list[DataStream] = []

    #function to add a stream to the empty list we have initliazed
    def add_stream(self, stream: DataStream) -> None:
        self.streams.append(stream)

    #process all streams
    def process_all(self, data_batches: list[list[Any]]) -> None:
        print("=== Polymorphic Stream Processing ===\n")
        print("Processing mixed stream types through unified interface...")
        
        #for every stream that we add to self.streans abd data_batches!
        for stream, batch in zip(self.streams, data_batches):
            #stream.stream_id, got iniwlized when we passed when we create the sesonr object strm
            print(f"\nProcessing stream {stream.stream_id} ")
            try:
                #filter this data!, we dont need to override this because its not a abstract method
                filtered_batch = stream.filtered_data(batch)
                #process only the data that didnt get filterd!
                result = stream.process_batch(filtered_batch)
                print(result)
            except Exception as e:
                print(f"Error processing {stream.stream_id}: {e}")


def main():
    #we pass strean_id to the class upon instantiating it!
    sensor = SensorStream("SENSOR_001")
    transaction = TransactionStream("TRANS_001")
    event = EventStream("EVENT_001")

    
    #streamprocessor that wil handle all the streams at once!
    processor = StreamProcessor()
    processor.add_stream(sensor)
    processor.add_stream(transaction)
    processor.add_stream(event)

    sensor_data = [
        {"temp": 22.5, "humidity": 65, "pressure": 1013},
        {"temp": 23.0, "humidity": 60, "pressure": 1010},
    ]

    transaction_data = [
        {"buy": 100},
        {"sell": 150},
        {"buy": 75},
    ]
    
    event_data = ["login", "error", "logout"]
    processor.process_all([sensor_data, transaction_data, event_data])

if __name__ == "__main__":
    main()


