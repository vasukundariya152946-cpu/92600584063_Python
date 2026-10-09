def generate_report(event,part):
    print("\n ---- Event Name :",event["name"])
    print("\n ----Date :",event["date"])
    print("\n ---- Time :",event["time"])
    print("\n ----- Participats :",len(part))
    for part in part:
        print("--",part)
        