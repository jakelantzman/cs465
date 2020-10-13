from queue import PriorityQueue
import math




def main():
	# need to read the input here
	# hardcoding it for now

	# INPUT 1

	# num_vert = 4
	# num_edges = 7
	# source_num = 4

	#edges = [[4, 3, 3], [3, 4, 5], [1, 4, 3], [2, 1, 7], [3, 1, 9], [1, 2, 10], [4, 2, 4]]

	#input 2
	num_vert = 6
	num_edges = 10
	source_num = 3

	edges = [[4, 1, 4], [3, 5, 2], [3, 2, 5], [5, 2, 5], [4, 2, 6], [2, 4, 9], [2, 1, 3], [2, 6, 10], [1, 4, 5], [4, 3, 1]]


	# merge sort edges by first element of tuple?
	edges = sortEdges(edges, len(edges))
		#print(edges)
		# [[1, 2, 10], [1, 4, 3], [2, 1, 7], [3, 1, 9], [3, 4, 5], [4, 2, 4], [4, 3, 3]]


	# set all distances to infinity
	distances = []
	for i in range(1, num_vert + 1):
		distances.append((i, math.inf))

		# print(distances)
		# 	-->	[(1, inf), (2, inf), (3, inf), (4, inf)]
		# print(distances[0]) --> (1, inf)
		# print(distances[0][0]) --> 1
	

	# make empty q
	PQ = PriorityQueue()

	# for all verts insert(PQ, v) where priority = inf
	for vert in distances:
		# print(vert) --> (1, inf)
		if vert[1] == math.inf:
			PQ.put(vert[0])

	# set distance for source to 0
	distances[source_num - 1] = (source_num, 0)
		# print(distances) --> [(1, inf), (2, inf), (3, inf), (4, 0)]

	# decrease-key(PQ, s, 0)

	# while empty(PQ) == false
	while not PQ.empty():
		# u = findmin(PQ) --> popping first val
		#deletemin(PQ) --> is just .get()??
		u = PQ.get() 	#??
		#for each edge u,v: need better way then to loop thru edges[]
		for element in edges:
			if element[0] == u:
				# if dist[v] > dist[u]
				if distances[element[1] - 1][1] > distances[u - 1][1]:
					#dist[v] = dist[u] + l(u,v)
					print(f"distances before: {distances}")
					distances[element[1] - 1] = (element[1], distances[u - 1][1] + element[2])
					print(f"distances after: {distances}")
					#decrease key(PQ, v, dist[v])
					# instead of decreasing key, just remove the current distance and change it to actual distance

					### NEED TO MAKE SURE TO DO THIS

					###


			#end if
		#end for
	#end while
	# end algo


# just does merge sort to sort the input edges and distances array
def sortEdges(array, length):

    if length > 1:
        
        # splitting the input array in half per the merge-sort algo
        leftArray = []
        rightArray = []
        midpoint = length // 2
        x = 0
        while x < midpoint:
            leftArray.append(array[x])
            x += 1

        while x < length:
            rightArray.append(array[x])
            x += 1

        # recursive call on each half of the array
        sortEdges(leftArray, len(leftArray))
        sortEdges(rightArray, len(rightArray))
        
        # counter variables to track the index of the two separate halves
        left_count = 0
        right_count = 0

        # counter variable track index of output array
        total_count = 0

        # This is the code from mergeSortedArrays()
        # Loop through each array and evaluate at each index which integer to insert into the output array,
        # if the length of either array becomes zero throughout the loop, append all remaining integers from
        # the other array to the output array
        while len(leftArray) > left_count and len(rightArray) > right_count:

            if(leftArray[left_count] < rightArray[right_count]):
                array[total_count] = leftArray[left_count]
                left_count += 1
            else:
                array[total_count] = rightArray[right_count]
                right_count += 1
            total_count += 1

        # check for any elements left in each of the two halves that were not appended yet
        while len(leftArray) > left_count:
            array[total_count] = leftArray[left_count]
            left_count += 1 
            total_count += 1

        while len(rightArray) > right_count:
            array[total_count] = rightArray[right_count]
            right_count += 1
            total_count += 1
    return array



if __name__ == "__main__":
	main()



