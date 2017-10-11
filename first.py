from Pregnancies import Pregnancies
import json
from stats import *

# def strify(number):
#     if number == 1:
#         return '1st Birth'
#     elif number == 2:
#         return '2nd Birth'
#     elif number == 3:
#         return '3rd Birth'
#     else:
#         return str(number) + 'th Birth'
#
#
# table = Pregnancies()
# table.ReadRecords()
#
# """ Total number of pregnancies """
# print("Number of pregnancies: %d" % len(table.records))
#
# #print(json.dumps(table.records[0].__dict__))
#
# """ Pregnancy record object:
#     {
#         "caseid": 1,
#         "nbrnaliv": 1,
#         "babysex": 1,
#         "birthwgt_lb": 8,
#         "birthwgt_oz": 13,
#         "prglength": 39,
#         "outcome": 1,
#         "birthord": 1,
#         "agepreg": 33.16,
#         "finalwgt": 6448.271111704751,
#         "totalwgt_oz": 141
#     }
# """
#
#
# """ Total live births """
# count = 0
# firstBirthLiveCount = 0
# otherBirthLiveCount = 0
# for record in table.records:
#     if record.outcome == 1:
#         count += 1
#         if record.birthord == 1:
#             firstBirthLiveCount += 1
#         else:
#             otherBirthLiveCount += 1
#
# print("Number of live births: %d" % count)
# print("Number of first baby live births: %d" % firstBirthLiveCount)
# print("Number of other baby live births: %d" % otherBirthLiveCount)
#
#
#
# """ Child birth histogram """
# histogram = {}
# for record in table.records:
#     if record.outcome == 1:
#         if strify(record.birthord) in histogram:
#             histogram[strify(record.birthord)] += 1
#         else:
#             histogram[strify(record.birthord)] = 1
#
# print("Histogram of child births: ", histogram)
#
#
#
# """ Difference between child births """
# firstBirthTime = 0
# otherBirthTime = 0
# firstBirthCount = 0
# otherBirthCount = 0
# for record in table.records:
#     if record.outcome == 1:
#         if record.birthord == 1:
#             firstBirthTime += record.prglength
#             firstBirthCount += 1
#         else:
#             otherBirthTime += record.prglength
#             otherBirthCount += 1
#
# print("Average first bith time: ", firstBirthTime/firstBirthCount)
# print("Average other bith time: ", otherBirthTime/otherBirthCount)



# STATISTICS
table = Pregnancies()
table.ReadRecords()

def Stat(r, birthorder=1):
    records = list(filter(lambda x: x.birthord != 'NA' and x.birthord > 2, r))
    records = [x.prglength for x in records]
    return MeanVar(records)

asd = Stat(table.records)
print(asd)

# (38.60095173351461, 7.792947202066306)
# (38.45566899516389, 7.083069689468648)