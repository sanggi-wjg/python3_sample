import json

sample = {
    "in_queue": [
        "2020-05-29 17:40:05",
        ""
    ],
    "in_log"  : [
        "2020-05-28 10:31:11",
        "8888"
    ],
    "out_log" : [
        "2020-05-28 10:31:11",
        "8888"
    ]
}

sample = sorted(sample.items(), key = lambda x: x[1][0], reverse = True)
print(sample)
