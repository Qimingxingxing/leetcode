class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        if not logs:
            return []
        s = [int(logs[0].split(":")[0])]
        res = [0 for _ in range(n)]
        for i in range(1, len(logs)):
            job, action, time = logs[i].split(":")
            lastJob, lastAction, lastTime = logs[i-1].split(":")
            job, time, lastJob, lastTime = int(job), int(time), int(lastJob), int(lastTime)
            if action == "start":
                if lastAction == "end":
                    if s:
                        res[s[-1]] += time - lastTime - 1
                else:
                    res[lastJob] += time - lastTime
                s.append(job)
            else:
                curJob = s.pop()
                if lastAction == "end":
                    res[curJob] += time - lastTime
                else:
                    res[job] += time - lastTime + 1
        return res
                
