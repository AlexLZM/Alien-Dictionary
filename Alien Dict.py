
def AlienDict(words):
    '''
    Take list of strings and return a string represents the order of letters
    '''
    # initiate data structres
    letters = ''.join(words)
    indegree = {c:0 for c in letters}
    graph = {c:set() for c in letters}
    
    def get_edge(word1, word2):
        '''
        Helper function to add edge to the graph
        Also indicates abnormal case like 'ab' and 'a'
        '''
        i = 0
        # find first letter that is not equal
        while i < min(len(word1), len(word2)) and word1[i] == word2[i]:
            i += 1

        if i == len(word2) and len(word1) > len(word2): # abnormal case
            return False

        if i < len(word1) and i < len(word2) and word2[i] not in graph[word1[i]]:
            indegree[word2[i]] += 1
            graph[word1[i]].add(word2[i])
        return True
    
    # parse the word and build graph
    for i, word1 in enumerate(words[:-1]):
        word2 = words[i+1]
        if not get_edge(word1, word2):
            return ''
    
    # filter nodes with 0 indegree
    stack = [c for c in indegree if indegree[c] == 0]
    
    # topological sort
    res = ''
    while stack:
        letter  = stack.pop()
        res += letter
        for child in graph[letter]:
            indegree[child] -= 1
            if indegree[child] == 0:
                stack.append(child)
        indegree.pop(letter) 
    return res if len(indegree) == 0 else '' # if loop exists, there will be letters remain in indegree dictionary
    
    

    
    
    
    
    
    
    
    
    
    
