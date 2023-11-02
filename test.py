import service, time

# set start time
# start_time = time.time()
# res = service.get_year("https://www.formula1.com/en/results.html/2023/races.html")
# end_time = time.time()

# print("Time taken: ", end_time - start_time)
# service.save_to_json(res, "2023")

for i in range(1950,2024):
    year = str(i)
    start_time = time.time()
    res = service.get_year(f"https://www.formula1.com/en/results.html/{i}/races.html")
    end_time = time.time()
    print("Time taken", str(i), ":", end_time - start_time)
    service.save_to_json(res, str(i))
    

# res = service.read_json("2010")
# print(res)