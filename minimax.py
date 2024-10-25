import math

def minimax(curDepth, nodeIndex, maxTurn, scores, targetDepth):
    # Base case : targetDepth reached
    if curDepth == targetDepth:
        return scores[nodeIndex]

    if maxTurn:
        return max(minimax(curDepth + 1, nodeIndex * 2, False, scores, targetDepth),
                   minimax(curDepth + 1, nodeIndex * 2 + 1, False, scores, targetDepth))

    else:
        return min(minimax(curDepth + 1, nodeIndex * 2, True, scores, targetDepth),
                   minimax(curDepth + 1, nodeIndex * 2 + 1, True, scores, targetDepth))


scores = [3,5,17,8,-2,5,-1,7]
treeDepth = math.log(len(scores),2)
print("Optimal Value: ",end="")
print(minimax(0,0,True, scores, treeDepth))