from confluent_kafka import Consumer

consumer = Consumer({"bootstrap.servers": "kafka:9092", "group.id": "code_runner", "auto.offset.reset": "earliest"})

consumer.subscribe(["code_runner"])


while True:
    msg = consumer.poll(1.0)

    if msg is None:
        print(f"Msg is {msg}")
        continue
    if msg.error():
        print(f"Error {msg}")
        continue

    print(f"Message: {msg.value().decode('utf-8')}")
