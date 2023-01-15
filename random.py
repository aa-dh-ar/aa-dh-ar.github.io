runTimes = []
runners = []
timeSecs = []
runTime = 0

def secsToMins(secs):
	mins = int(secs/60)
	remainingSecs = int(secs%60)

	return str(mins) + "mins" + str(remainingSecs) + "secs"
def printResult():
	averageTime = (sum(timeSecs)/len(timeSecs))

	if runTimeList == []:
		print("No data.")
	else:
		print("let's go\n")
		for i in range(len(runTimes) - 1):
			print(runTimes[i])
		print("Total runners = " + str(len(runners)))
		print("Average Time = " + secsToMins(averageTime))

		fastest = min(timeSecs)

		print("Fastest Time = " + secsToMins(fastest))
		print("Slowest Time = "+ secsToMins(max(timeSecs)))

		for i in range(len(timeSecs) - 1):
			if timeSecs[i] == fastest:
				print("Best Time Here = " + runners[i])

while runTime != "":
	runTime = input("Enter runTime: ")
	runTimes.append(runTime)

	runTimeList = runTime.split("::")
	print(runTimeList)
	if runTime != "":
		runner = runTimeList[0]
		runners.append(runner)

		timeSec = runTimeList[1]
		timeSecs.append(int(timeSec))
else:
	printResult()





